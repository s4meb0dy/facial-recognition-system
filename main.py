from PyQt5 import QtWidgets, QtGui, QtCore
from main_ui import Ui_MainWindow 
from add_info_ui import AddInfo_Form
from facerec_from_webcam_faster import recognize
from webcamsave import takePhoto
import sys, os, cv2, datetime, pymysql, face_recognition, shutil
from functools import partial
import constants
import json
import numpy as np
 
class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)

class mainwindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mainwindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.dialogs = list()
        # подключение клик-сигнал к слоту btnClicked
        self.ui.pushButton_startRecognition.clicked.connect(self.on_pushButton_startRecognition_click)
        self.ui.pushButton_addToDB.clicked.connect(self.on_pushButton_addToDB_click)

    def on_pushButton_startRecognition_click(self):
            recognize()

    def on_pushButton_addToDB_click(self):
        dialog = addInfoWindow()
        self.dialogs.append(dialog)
        dialog.show()

class addInfoWindow(QtWidgets.QWidget, AddInfo_Form):
    
   
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.photo_filePath = ""
        self.pushButton_uploadPhoto.clicked.connect(self.on_pushButton_uploadPhoto_click)
        self.pushButton_takePhoto.clicked.connect(self.on_pushButton_takePhoto_click)
        self.pushButton_insert.clicked.connect(self.on_pushButton_insertInfo_click)


    def on_pushButton_uploadPhoto_click(self):
        filePath, condition = QtWidgets.QFileDialog.getOpenFileName(self, 'OpenFile', "", "Image files (*.jpg *.gif *.jpeg *.png)")
        filePath = os.path.normpath(filePath)
        if filePath != "":
            self.label_imageView.setPixmap(QtGui.QPixmap(filePath).scaled(QtCore.QSize(351, 261), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
        self.photo_filePath = filePath
        print(self.photo_filePath)

    def on_pushButton_takePhoto_click(self):
        currentFrame = takePhoto()
        taken_photo_path = os.getcwd()+'/temp/temp_im.jpg'
        cv2.imwrite(taken_photo_path, currentFrame)
        if taken_photo_path != "":
            self.label_imageView.setPixmap(QtGui.QPixmap(taken_photo_path).scaled(QtCore.QSize(351, 261), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
        self.photo_filePath = taken_photo_path
        print(self.photo_filePath)

    def on_pushButton_insertInfo_click(self):
        name = self.lineEdit_name.text()
        age = self.lineEdit_age.text()
        sex = self.lineEdit_sex.text()
        nationality = self.lineEdit_nationality.text()
        print(name,age,sex,nationality)
        print(self.photo_filePath)

        if not name or not age or not sex or not nationality or not self.photo_filePath:
            print("Error")
                # Display error message
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setWindowIcon(QtGui.QIcon("images/AR_icon.ico"))
            msg.setText("Please fill in all the fields and take/choose your photo")
            msg.setWindowTitle("Mandatory info missing")
            msg.addButton(QtWidgets.QMessageBox.Ok)
            msg.exec_()
        
        else:
            photoPath = os.getcwd()+"/known_faces/"+name+("_")+datetime.datetime.now().strftime('%d_%m_%Y %H_%M_%S')+".jpg"
            shutil.copy(self.photo_filePath, photoPath)
            known_face_image = face_recognition.load_image_file(os.path.normpath(photoPath))
            face_encoding = face_recognition.face_encodings(known_face_image)[0]
            str_face_encoding = json.dumps(face_encoding, cls=NumpyEncoder)

            db, cursor = init_db_connection()

            sql = """INSERT INTO people(id_person, name, age,sex,nationality) 
                VALUES (DEFAULT, %s, %s, %s, %s)"""
            try:
                cursor.execute(sql, (name, age, sex, nationality))
                db.commit()
                # Display success message
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setWindowIcon(QtGui.QIcon("images/AR_icon.ico"))
                msg.setText("Your info was successfully added to the DB")
                msg.setWindowTitle("Success")
                msg.addButton(QtWidgets.QMessageBox.Ok)
                msg.button(QtWidgets.QMessageBox.Ok).clicked.connect(self.resetUI)
                msg.exec_()
            except pymysql.Error as e:
                print("Error while connecting to MySQL", e)
                db.rollback()  
                # Display error message
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setWindowIcon(QtGui.QIcon("images/AR_icon.ico"))
                msg.setText("There was an error during insert. Please try again.")
                msg.setWindowTitle("Error")
                msg.addButton(QtWidgets.QMessageBox.Ok)
                msg.button(QtWidgets.QMessageBox.Ok).clicked.connect(self.resetUI)
                msg.exec_() 
            
            person_id = cursor.lastrowid
            print(person_id)
            print(str_face_encoding)
            sql = """INSERT INTO face_encodings(id_face_encoding, id_person, face_encoding) 
                VALUES (DEFAULT, %s, %s)"""
            try:
                cursor.execute(sql, (person_id, str_face_encoding))
                db.commit()
            except pymysql.Error as e:
                print("Error while connecting to MySQL", e)
                db.rollback()      

        
    def resetUI(self):
        self.lineEdit_name.clear()
        self.lineEdit_age.clear()
        self.lineEdit_sex.clear()
        self.lineEdit_nationality.clear()
        self.label_imageView.clear()


def init_db_connection():
     db = pymysql.connect(host=constants.HOST, port=constants.PORT, user=constants.USER, passwd=constants.PASSWORD, db=constants.DATABASE)
     cursor = db.cursor()
     return db, cursor

def main():        
    app = QtWidgets.QApplication([])
    application = mainwindow()
    application.show()

    sys.exit(app.exec())

if __name__ == '__main__':
    main()