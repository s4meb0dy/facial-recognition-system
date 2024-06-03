import face_recognition
import cv2
import numpy
import json
import pymysql
import constants

def recognize():
    db = pymysql.connect(host=constants.HOST, port=constants.PORT, user=constants.USER, passwd=constants.PASSWORD, db=constants.DATABASE)
    cursor = db.cursor(pymysql.cursors.DictCursor)
    rows = []
    sql = """SELECT f.face_encoding, p.name, p.age, p.sex, p.nationality
        FROM face_encodings f JOIN people p
        ON f.id_person = p.id_person"""
    try:
        cursor.execute(sql)
        rows = cursor.fetchall()
        db.commit()
    except pymysql.Error as e:
        print("Error while connecting to MySQL", e)
        db.rollback()  

    for row in rows:
        deserialized_encoding = json.loads(row["face_encoding"])
        row["face_encoding"] = numpy.array(deserialized_encoding)
    
    video_capture = cv2.VideoCapture(0)

    video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1366)
    video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 1366)

    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True

    while True:
        ret, frame1 = video_capture.read()
        frame = frame1.copy()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = numpy.ascontiguousarray(small_frame[:, :, ::-1])

        if process_this_frame:
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces([row["face_encoding"] for row in rows], face_encoding)
                name = "Unknown"

                if face_encodings:
                    face_distances = face_recognition.face_distance([row["face_encoding"] for row in rows], face_encoding)
                    if face_distances.size > 0:  # Change this line
                        best_match_index = numpy.argmin(face_distances)
                        if matches[best_match_index]:
                            name = rows[best_match_index].get("name")

                face_names.append(name)

        process_this_frame = not process_this_frame

        font = cv2.FONT_HERSHEY_DUPLEX

        for (top, right, bottom, left), name in zip(face_locations, face_names):
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            cv2.rectangle(frame, (left, top), (right, bottom), (128, 0, 128), 2)

            if name != "Unknown":
                for i, row in enumerate(rows):
                    if row.get("name") == name:
                        cv2.putText(frame, row.get("name"), (left - 265, top + 30 + i*30), font, 0.75, (255,255,255), 2)
                        cv2.putText(frame, "Age: " + str(row.get("age")), (left - 265, top + 60 + i*30), font, 0.75, (255,255,255), 1)
                        cv2.putText(frame, "Sex: " + row.get("sex"), (left - 265, top + 90 + i*30), font, 0.75, (255,255,255), 1)
                        cv2.putText(frame, "Nationality: " + row.get("nationality"), (left - 265, top + 120 + i*30), font, 0.75, (255,255,255), 1)
            else:
                cv2.putText(frame, "Unknown", (left - 265, top + 30), font, 0.75, (255,255,255), 1)

        cv2.imshow('ARecognize', frame)
        key = cv2.waitKey(1)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()
