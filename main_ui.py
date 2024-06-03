# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(727, 437)
        MainWindow.setMinimumSize(QtCore.QSize(727, 437))
        MainWindow.setMaximumSize(QtCore.QSize(727, 437))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/AR1_icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_startRecognition = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_startRecognition.setGeometry(QtCore.QRect(40, 120, 171, 71))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(9)
        self.pushButton_startRecognition.setFont(font)
        self.pushButton_startRecognition.setStyleSheet("")
        self.pushButton_startRecognition.setAutoRepeatDelay(300)
        self.pushButton_startRecognition.setAutoDefault(False)
        self.pushButton_startRecognition.setDefault(True)
        self.pushButton_startRecognition.setObjectName("pushButton_startRecognition")
        self.pushButton_addToDB = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_addToDB.setGeometry(QtCore.QRect(40, 30, 171, 71))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(9)
        self.pushButton_addToDB.setFont(font)
        self.pushButton_addToDB.setStyleSheet("")
        self.pushButton_addToDB.setAutoDefault(False)
        self.pushButton_addToDB.setDefault(True)
        self.pushButton_addToDB.setFlat(False)
        self.pushButton_addToDB.setObjectName("pushButton_addToDB")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 791, 431))
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/background.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label.raise_()
        self.pushButton_startRecognition.raise_()
        self.pushButton_addToDB.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ARecognize"))
        self.pushButton_startRecognition.setText(_translate("MainWindow", "Start Recognition"))
        self.pushButton_addToDB.setText(_translate("MainWindow", "Add to Database"))
