# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_info.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class AddInfo_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(729, 438)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/AR_icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 791, 441))
        self.label.setMinimumSize(QtCore.QSize(791, 441))
        self.label.setMaximumSize(QtCore.QSize(791, 441))
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/background.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")


        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(30, 20, 301, 301))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(9)
        self.groupBox.setFont(font)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")

        self.pushButton_insert = QtWidgets.QPushButton(Form)
        self.pushButton_insert.setGeometry(QtCore.QRect(40, 340, 281, 51))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(9)
        self.pushButton_insert.setFont(font)
        self.pushButton_insert.setStyleSheet("")
        self.pushButton_insert.setAutoDefault(False)
        self.pushButton_insert.setDefault(True)
        self.pushButton_insert.setFlat(False)
        self.pushButton_insert.setObjectName("pushButton_insert")

        self.lineEdit_name = QtWidgets.QLineEdit(Form)
        self.lineEdit_name.setGeometry(QtCore.QRect(40, 50, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(9)
        self.lineEdit_name.setFont(font)
        self.lineEdit_name.setStyleSheet("padding: 3px")
        self.lineEdit_name.setInputMask("")
        self.lineEdit_name.setText("")
        self.lineEdit_name.setObjectName("lineEdit_name")
        

        self.lineEdit_age = QtWidgets.QLineEdit(Form)
        self.lineEdit_age.setGeometry(QtCore.QRect(40, 100, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(9)
        self.lineEdit_age.setFont(font)
        self.lineEdit_age.setStyleSheet("padding: 3px")
        self.lineEdit_age.setInputMask("")
        self.lineEdit_age.setText("")
        self.lineEdit_age.setObjectName("lineEdit_age")

        self.lineEdit_sex = QtWidgets.QLineEdit(Form)
        self.lineEdit_sex.setGeometry(QtCore.QRect(40, 150, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(9)
        self.lineEdit_sex.setFont(font)
        self.lineEdit_sex.setStyleSheet("padding: 3px")
        self.lineEdit_sex.setInputMask("")
        self.lineEdit_sex.setText("")
        self.lineEdit_sex.setObjectName("lineEdit_sex")

        self.lineEdit_nationality = QtWidgets.QLineEdit(Form)
        self.lineEdit_nationality.setGeometry(QtCore.QRect(40, 200, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(9)
        self.lineEdit_nationality.setFont(font)
        self.lineEdit_nationality.setStyleSheet("padding: 3px")
        self.lineEdit_nationality.setInputMask("")
        self.lineEdit_nationality.setText("")
        self.lineEdit_nationality.setObjectName("lineEdit_nationality")

        self.pushButton_takePhoto = QtWidgets.QPushButton(Form)
        self.pushButton_takePhoto.setGeometry(QtCore.QRect(40, 260, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(9)
        self.pushButton_takePhoto.setFont(font)
        self.pushButton_takePhoto.setStyleSheet("")
        self.pushButton_takePhoto.setAutoDefault(False)
        self.pushButton_takePhoto.setDefault(True)
        self.pushButton_takePhoto.setFlat(False)
        self.pushButton_takePhoto.setObjectName("pushButton_takePhoto")

        self.pushButton_uploadPhoto = QtWidgets.QPushButton(Form)
        self.pushButton_uploadPhoto.setGeometry(QtCore.QRect(190, 260, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(9)
        self.pushButton_uploadPhoto.setFont(font)
        self.pushButton_uploadPhoto.setStyleSheet("")
        self.pushButton_uploadPhoto.setAutoDefault(False)
        self.pushButton_uploadPhoto.setDefault(True)
        self.pushButton_uploadPhoto.setFlat(False)
        self.pushButton_uploadPhoto.setObjectName("pushButton_uploadPhoto")

        self.label_imageView = QtWidgets.QLabel(Form)
        self.label_imageView.setGeometry(QtCore.QRect(350, 50, 351, 261))
        self.label_imageView.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_imageView.setText("")
        self.label_imageView.setStyleSheet("background-color: rgba(0, 0, 0, 150);")
        self.label_imageView.setScaledContents(False)
        self.label_imageView.setSizePolicy(QtWidgets.QSizePolicy.Fixed,QtWidgets.QSizePolicy.Fixed)
        self.label_imageView.setObjectName("label_imageView")
        self.label_imageView.setAlignment(QtCore.Qt.AlignCenter)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "ARecognize - Add Info to Database"))
        self.lineEdit_name.setPlaceholderText(_translate("Form", "Enter your name"))
        self.pushButton_insert.setText(_translate("Form", "Insert Info to Database"))
        self.lineEdit_age.setPlaceholderText(_translate("Form", "Enter your age"))
        self.lineEdit_sex.setPlaceholderText(_translate("Form", "Enter your sex"))
        self.lineEdit_nationality.setPlaceholderText(_translate("Form", "Enter your nationality"))
        self.pushButton_takePhoto.setText(_translate("Form", "Take photo"))
        self.pushButton_uploadPhoto.setText(_translate("Form", "Upload photo"))
        self.groupBox.setTitle(_translate("Form", "Your Data"))

    def __init__(self):
        super(AddInfo_Form, self).__init__()


