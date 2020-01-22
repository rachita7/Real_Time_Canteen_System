# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Desktop/ICT/screen1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
import time

#Home Screen
class Ui_MainWindow(object):        

    #Clock Function
    def realTimeClock(self, MainWindow):
        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000)
        self.dClock = QtWidgets.QLabel(self.centralwidget)
        self.dClock.setGeometry(QtCore.QRect(1000, 10, 190, 20))
        self.dClock.setObjectName("dClock")
        self.dClock.setStyleSheet('QLabel{color: white;}')
        self.timer.timeout.connect(self.displayTime)
        self.timer.start()

    #Display Clock Function
    def displayTime(self):
        self.currentDateTime = QtCore.QDateTime.currentDateTime()
        self.strCurrentDateTime = (self.currentDateTime.toString("ddd d/MMM/yy hh:mm:ss"))
        self.dClock.setText(self.currentDateTime.toString("ddd d/MMM/yy hh:mm:ss"))
    
    #Set Date Function
    def setDateBtn(self):
        self.main = SetDate()
        self.main.setupUi(self.main)
        self.main.show()
   
    #Today Button Function
    def todayBtn(self):
        TodayWindow.show()
        MainWindow.hide()

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1200, 800)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #background image
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1200, 800))
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("background-image:url(img_6710.jpg)")
        self.label.setObjectName("label")

        #wWelcome Sign
        self.welcome = QtWidgets.QLabel(self.centralwidget)
        self.welcome.setGeometry(QtCore.QRect(350, 10, 500, 200))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.welcome.setFont(font)
        self.welcome.setObjectName("welcome")

        #Calling Clock Function
        self.realTimeClock(MainWindow)

        self.today = QtWidgets.QPushButton(self.centralwidget)
        self.today.setGeometry(QtCore.QRect(450, 450, 250, 50))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.today.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.today.setStyleSheet("""
             QPushButton {
                border-radius: 10px;
                background-color: white;
             }
             QPushButton:focus:pressed {
                 background-color: rgb(100,100,100);  
             }
             QPushButton:hover {
                 background-color: rgb(200,200,200);
             }
        """)
        self.today.setFont(font)
        self.today.setObjectName("today")
        self.today.clicked.connect(self.todayBtn)

        #set date button
        self.setdate = QtWidgets.QPushButton(self.centralwidget)
        self.setdate.setGeometry(QtCore.QRect(450, 550, 250, 50))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.setdate.setFont(font)
        self.setdate.setObjectName("setdate")
        self.setdate.clicked.connect(self.setDateBtn)
        self.setdate.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.setdate.setStyleSheet("""
             QPushButton {
                border-radius: 10px;
                background-color: white;
             }
             QPushButton:focus:pressed {
                 background-color: rgb(100,100,100);     
             }
             QPushButton:hover {
                 background-color: rgb(200,200,200);
             }
        """)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    #function to translate certain ui contents into main set up
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Makan @ NorthSpine"))
        MainWindow.setWindowIcon(QtGui.QIcon('icon.png'))
        self.label.setText(_translate("MainWindow", ""))
        self.welcome.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; color:#ffffff;\">Welcome to <br/></span><span style=\" font-size:28pt; color:#e80003;\">North</span><span style=\" font-size:28pt; color:#9e9e9e;\">Spine</span><span style=\" font-size:28pt; color:#ffffff;\">!</span></p></body></html>"))
        self.today.setText(_translate("MainWindow", "VIEW TODAY'S STALLS"))
        self.setdate.setText(_translate("MainWindow", "VIEW STALLS BY DATE"))

#Set Date and Time Widget
class SetDate(QtWidgets.QWidget):

    def submitButton(self):
        self.chosenDateTime()
        self.hide()
        self.main = Ui_StallsWindow()
        self.main.setupUi(self.main)
        self.main.show()

    #Function to save the user input into an external text file for handling at a later time
    def chosenDateTime(self):

        f = open("cdt.txt", "w+")
        self.chosenDate = str(self.dateEdit.text())
        self.chosenTime = self.timeEdit

        #assigns the day of the week in accordance to file handling format (e,g. 1 = 'mon')
        if self.dateEdit.date().dayOfWeek() == 1:
            self.day = "mon"
        elif self.dateEdit.date().dayOfWeek() == 2:
            self.day = "tue"
        elif self.dateEdit.date().dayOfWeek() == 3:
            self.day = "wed"
        elif self.dateEdit.date().dayOfWeek() == 4:
            self.day = "thu"
        elif self.dateEdit.date().dayOfWeek() == 5:
            self.day = "fri"
        elif self.dateEdit.date().dayOfWeek() == 6:
            self.day = "sat"
        elif self.dateEdit.date().dayOfWeek() == 7:
            self.day = "sun"

        #writes chosen Date and Time into text file
        f.write(self.chosenTime.time().toString("HHmm") + "," + self.chosenDate + "," + self.day)
        f.close()

    def setupUi(self, Form):

        Form.setObjectName("Form")
        Form.setFixedSize(500, 300)

        #submit button
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(210, 200, 80, 30))
        self.pushButton.setStyleSheet("font: 63 8pt \"Bahnschrift SemiBold\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setObjectName("setdate")
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.clicked.connect(self.submitButton)
        self.pushButton.setStyleSheet("""
             QPushButton {
                font: 63 10pt \"Bahnschrift SemiBold\";
                border-radius: 10px;
                background-color: white;
             }
             QPushButton:focus:pressed {
                 background-color: rgb(100,100,100);   
             }
             QPushButton:hover {
                 background-color: rgb(200,200,200);  
             }
        """)

        #Date Label
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(30, 40, 300, 100))
        self.label_7.setStyleSheet("font: 63 8pt \"Bahnschrift SemiBold\";")
        self.label_7.setObjectName("label_7")

        #Time Label
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(170, 40, 300, 100))
        self.label_8.setStyleSheet("font: 63 8pt \"Bahnschrift SemiBold\";")
        self.label_8.setObjectName("label_8")
        #Time Input
        self.timeEdit = QtWidgets.QTimeEdit(Form)
        self.timeEdit.setGeometry(QtCore.QRect(270, 120, 120, 30))
        self.timeEdit.setStyleSheet("font: 9pt \"Bahnschrift SemiBold\";")
        self.timeEdit.setObjectName("timeEdit")
        self.timeEdit.setTime(QtCore.QTime.currentTime())

        #Date Input
        self.dateEdit = QtWidgets.QDateEdit(Form)
        self.dateEdit.setGeometry(QtCore.QRect(130, 120, 120, 30))
        self.dateEdit.setStyleSheet("font: 9pt \"Bahnschrift SemiBold\";")
        self.dateEdit.setMaximumDate(QtCore.QDate(2021, 12, 31))
        self.dateEdit.setMinimumDate(QtCore.QDate.currentDate())
        self.dateEdit.setObjectName("dateEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Set Date & Time"))
        Form.setWindowIcon(QtGui.QIcon('icon.png'))
        self.pushButton.setText(_translate("Form", "Submit"))
        self.label_7.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Date:</span></p></body></html>"))
        self.label_8.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Time:</span></p></body></html>"))

#View Today's Stall Window
class Ui_SetToday(object):

    def realTimeClock(self, Form):
        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000)
        self.dClock = QtWidgets.QLabel(Form)
        self.dClock.setGeometry(QtCore.QRect(1000, 10, 190, 20))
        self.dClock.setObjectName("dClock")
        self.dClock.setStyleSheet('QLabel{color: black;}')
        self.timer.timeout.connect(self.displayTime)
        self.timer.start()

    def displayTime(self):
        self.currentDateTime = QtCore.QDateTime.currentDateTime()
        self.strCurrentDateTime = (self.currentDateTime.toString("ddd d/MMM/yy hh:mm:ss"))
        self.dClock.setText(self.currentDateTime.toString("ddd d/MMM/yy hh:mm:ss"))

    #Back button to go to main window while exiting current window
    def backBtn(self):
        MainWindow.show()
        TodayWindow.hide()

    #Button Function to set Custom time
    def customBtn(self):
        self.main = SetTime()
        self.main.setupUi(self.main)
        self.main.show()

    #Button Function to set to Current Time
    def currentBtn(self):
        f = open("cdt.txt", "w+")
        self.chosenDate = QtCore.QDateTime.currentDateTime().toString("dd/MM/yyyy")
        self.chosenDay = QtCore.QDateTime.currentDateTime().toString("ddd")
        self.chosenTime = QtCore.QDateTime.currentDateTime().toString("HHmm")
        f.write(self.chosenTime + "," + self.chosenDate + "," + self.chosenDay)
        f.close()
        self.main = Ui_CurrentStallsWindow()
        self.main.setupUi(self.main)
        self.main.show()

    def setupUi(self, TodayWindow):
        TodayWindow.setObjectName("TodayWindow")
        TodayWindow.setFixedSize(1200, 800)

        self.realTimeClock(TodayWindow)

        self.centralwidget = QtWidgets.QWidget(TodayWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1200, 41))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        #NTU LABEL
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")

        self.verticalLayout.addWidget(self.label)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(-1, 39, 1200, 41))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        #NORTH SPINE LABEL
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setStyleSheet("font: 87 8pt \"Bahnschrift SemiBold\";")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)

        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(0, 140, 1200, 61))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        #Today's Date Label
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_3.setStyleSheet("font: 87 8pt \"Bahnschrift SemiBold\";")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)

        self.label_3.setText("TODAY'S DATE: "+ QtCore.QDateTime.currentDateTime().toString("dd/MM/yyyy"))
        self.label_3.setStyleSheet("""font: 63 20pt \"Bahnschrift SemiBold\";""")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)

        #Current Time Button
        self.currentTime = QtWidgets.QPushButton(self.centralwidget)
        self.currentTime.setGeometry(QtCore.QRect(400, 350, 400, 50))
        self.currentTime.setStyleSheet("font: 63 12pt \"Bahnschrift SemiBold\";")
        self.currentTime.setObjectName("currentTime")
        self.currentTime.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.currentTime.setStyleSheet("""
             QPushButton {
                font: 63 10pt \"Bahnschrift SemiBold\";
                border-radius: 10px;
                background-color: white;
             }
             QPushButton:focus:pressed {
                 background-color: rgb(100,100,100);   
             }
             QPushButton:hover {
                 background-color: rgb(200,200,200);  
             }
        """)
        self.currentDateTime = QtCore.QDateTime.currentDateTime()
        self.strCurrentDateTime = (self.currentDateTime.toString("ddd d/MMM/yy hh:mm:ss"))
        self.currentTime.clicked.connect(self.currentBtn)

        #Custom Time Button
        self.customTime = QtWidgets.QPushButton(self.centralwidget)
        self.customTime.setGeometry(QtCore.QRect(400, 450, 400, 50))
        self.customTime.setStyleSheet("font: 63 12pt \"Bahnschrift SemiBold\";")
        self.customTime.setObjectName("customTime")
        self.customTime.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.customTime.setStyleSheet("""
             QPushButton {
                font: 63 10pt \"Bahnschrift SemiBold\";
                border-radius: 10px;
                background-color: white;
             }
             QPushButton:focus:pressed {
                 background-color: rgb(100,100,100);   
             }
             QPushButton:hover {
                 background-color: rgb(200,200,200);  
             }
        """)
        self.customTime.clicked.connect(self.customBtn)

        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(900, 700, 200, 40))
        self.backButton.setObjectName("backButton")
        self.backButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.backButton.setStyleSheet("""
             QPushButton {
                font: 63 10pt \"Bahnschrift SemiBold\";
                border-radius: 10px;
                background-color: white;
             }
             QPushButton:focus:pressed {
                 background-color: rgb(100,100,100);   
             }
             QPushButton:hover {
                 background-color: rgb(200,200,200);  
             }
        """)
        self.backButton.clicked.connect(self.backBtn)

        self.image = QtWidgets.QLabel(TodayWindow)
        self.image.setGeometry(QtCore.QRect(0, 0, 1200, 800))
        self.image.setStyleSheet("background-image: url(img1.jpg);")
        self.image.setText("")
        self.image.setObjectName("image")
        self.image.lower()

        self.verticalLayoutWidget.raise_()
        self.verticalLayoutWidget_2.raise_()
        self.verticalLayoutWidget_3.raise_()
        self.currentTime.raise_()
        self.customTime.raise_()
        self.backButton.raise_()
        TodayWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(TodayWindow)
        QtCore.QMetaObject.connectSlotsByName(TodayWindow)

    def retranslateUi(self, TodayWindow):
        _translate = QtCore.QCoreApplication.translate
        TodayWindow.setWindowTitle(_translate("TodayWindow", "TodayWindow"))
        self.label.setText(_translate("TodayWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">N A N Y A N G    &nbsp;    T E C H O L O G I C A L    &nbsp;     U N I V E R S I T Y </span></p></body></html>"))
        self.label_2.setText(_translate("TodayWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">NORTH SPINE CANTEEN</span></p></body></html>"))
        self.currentTime.setText(_translate("TodayWindow", "VIEW STALLS BY CURRENT TIME"))
        self.customTime.setText(_translate("TodayWindow", "VIEW STALLS BY CUSTOM TIME"))
        self.backButton.setText(_translate("TodayWindow", "BACK TO MAIN"))

#Custom Time Window for Today's Menu
class SetTime(QtWidgets.QWidget):

    def submitButton(self):
        self.chosenDateTime()
        self.hide()
        self.stall = Ui_CustomStallsWindow()
        self.stall.setupUi(self.stall)
        self.stall.show()

    def realTimeClock(self, Form):
        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000)
        self.dClock = QtWidgets.QLabel(Form)
        self.dClock.setGeometry(QtCore.QRect(300, 10, 190, 20))
        self.dClock.setObjectName("dClock")
        self.dClock.setStyleSheet('QLabel{color: grey;}')
        self.timer.timeout.connect(self.displayTime)
        self.timer.start()

    def displayTime(self):
        self.currentDateTime = QtCore.QDateTime.currentDateTime()
        self.strCurrentDateTime = (self.currentDateTime.toString("ddd d/MMM/yy hh:mm:ss"))
        self.dClock.setText(self.currentDateTime.toString("ddd d/MMM/yy hh:mm:ss"))

    def chosenDateTime(self):
        f = open("cdt.txt", "w+")
        self.chosenDate = QtCore.QDateTime.currentDateTime().toString("dd/MM/yyyy")
        self.chosenDay = QtCore.QDateTime.currentDateTime().toString("ddd")
        self.chosenTime = self.timeEdit
        f.write(self.chosenTime.time().toString("HHmm") + "," + self.chosenDate + "," + self.chosenDay)
        f.close()
        print(self.chosenDate)
        print(self.chosenTime)

    def setupUi(self, Form):

        #submit button
        Form.setObjectName("Form")
        Form.setFixedSize(500, 300)

        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        #self.isClicked = False  
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(210, 200, 80, 30))
        self.pushButton.setStyleSheet("font: 63 8pt \"Bahnschrift SemiBold\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setObjectName("setdate")
        self.pushButton.clicked.connect(self.submitButton)

        #Time Label
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(90, 40, 335, 100))
        self.label_8.setStyleSheet("font: 63 8pt \"Bahnschrift SemiBold\";")
        self.label_8.setObjectName("label_8")
        #Time Input
        self.timeEdit = QtWidgets.QTimeEdit(Form)
        self.timeEdit.setGeometry(QtCore.QRect(190, 130, 120, 30))
        self.timeEdit.setStyleSheet("font: 9pt \"Bahnschrift SemiBold\";")
        self.timeEdit.setObjectName("timeEdit")
        self.timeEdit.setTime(QtCore.QTime.currentTime())

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Set Time"))
        Form.setWindowIcon(QtGui.QIcon('icon.png'))
        self.pushButton.setText(_translate("Form", "Submit"))
        self.label_8.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">SELECT THE TIME:</span></p></body></html>"))

class Ui_CurrentStallsWindow(QtWidgets.QWidget):

    def realTimeClock(self, Form):
        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000)
        self.dClock = QtWidgets.QLabel(Form)
        self.dClock.setGeometry(QtCore.QRect(1000, 10, 190, 20))
        self.dClock.setObjectName("dClock")
        self.dClock.setStyleSheet('QLabel{color: black;}')
        self.dClock.raise_()
        self.timer.timeout.connect(self.displayTime)
        self.timer.start()

    def displayTime(self):
        self.currentDateTime = QtCore.QDateTime.currentDateTime()
        self.strCurrentDateTime = (self.currentDateTime.toString("ddd d/MMM/yy hh:mm:ss"))
        self.dClock.setText(self.currentDateTime.toString("ddd d/MMM/yy hh:mm:ss"))

    def chosenStall(self, stall):

        #new function
        fChosen = open("chosenStall.txt", "w+")
        fChosen.write(stall)
        fChosen.close()

        self.main = Ui_MenuWindow()
        self.main.setupUi(self.main)
        self.main.show()

    def backBtn(self):
        TodayWindow.show()
        MainWindow.hide()
        self.hide()

    def homeBtn(self):
        MainWindow.show()
        TodayWindow.hide()
        self.hide()

    def setupUi(self, Form):
        
        Form.setObjectName("Form")
        Form.setFixedSize(1200, 800)

        self.realTimeClock(Form)

        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(250, 120, 741, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold\";")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.centralwidget = QtWidgets.QWidget(Form)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget1.setGeometry(QtCore.QRect(0, 0, 1200, 41))
        self.verticalLayoutWidget1.setObjectName("verticalLayoutWidget1")
        self.verticalLayout1 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget1)
        self.verticalLayout1.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout1.setObjectName("verticalLayout1")

        self.label1 = QtWidgets.QLabel(self.verticalLayoutWidget1)
        self.label1.setStyleSheet("")
        self.label1.setObjectName("label")
        self.verticalLayout1.addWidget(self.label1)

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(-1, 39, 1200, 41))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setStyleSheet("font: 87 8pt \"Bahnschrift SemiBold\";")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)

        self.image = QtWidgets.QLabel(Form)
        self.image.setGeometry(QtCore.QRect(0, 0, 1200, 800))
        self.image.setStyleSheet("background-image: url(img2.jpg);")
        self.image.setText("")
        self.image.setObjectName("image")
        self.image.lower()

        #Stalls
        self.label.setText("PICK A STALL TO VIEW THIER MENU :")
        self.label.setStyleSheet("""
                    font: 63 20pt \"Bahnschrift SemiBold\";
                 """)
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        #Reads stalls text file to assign the stalls to a list
        fStalls = open("stalls.txt", "r")
        readlines = fStalls.read()
        fSLines = readlines.split(",")
        self.buttons = []
        self.stallChosen = ""

        #Assigning each stall item as a button widget
        for i in range(len(fSLines)):
            #Replacing "_" in stalls files with a " " (E.g, from 'Western_Food' to 'Western Food')
            fSLines[i] = fSLines[i].replace("_"," ")
            self.buttons.append(fSLines[i])

            #Creating Stalls' button Widget
            self.buttons[i] = QtWidgets.QPushButton(Form)
            self.buttons[i].setGeometry(QtCore.QRect(450, 250+(i*70), 300, 50))
            self.buttons[i].setStyleSheet("font: 63 8pt \"Bahnschrift SemiBold\";")
            self.buttons[i].setObjectName(str(self.buttons[i]))
            self.buttons[i].setText(fSLines[i])
            self.buttons[i].setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.buttons[i].setStyleSheet("""
                 QPushButton {
                    font: 63 10pt \"Bahnschrift SemiBold\";
                    border-radius: 10px;
                    background-color: white;
                 }
                 QPushButton:focus:pressed {
                     background-color: rgb(100,100,100);   
                 }
                 QPushButton:hover {
                     background-color: rgb(200,200,200);  
                 }
            """)
  
            self.buttons[i].setCheckable(True)
            self.buttons[i].setEnabled(True)

        #Assigning texts to each button as it's Stall Name
        if len(fSLines) == 6:
            self.buttons[0].clicked.connect(lambda: self.chosenStall(self.buttons[0].text()))
            self.buttons[1].clicked.connect(lambda: self.chosenStall(self.buttons[1].text()))
            self.buttons[2].clicked.connect(lambda: self.chosenStall(self.buttons[2].text()))
            self.buttons[3].clicked.connect(lambda: self.chosenStall(self.buttons[3].text()))
            self.buttons[4].clicked.connect(lambda: self.chosenStall(self.buttons[4].text()))
            self.buttons[5].clicked.connect(lambda: self.chosenStall(self.buttons[5].text()))

        self.backButton = QtWidgets.QPushButton(Form)
        self.backButton.setGeometry(QtCore.QRect(100, 700, 200, 40))
        self.backButton.setObjectName("backButton")
        self.backButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.backButton.setText("BACK")
        self.backButton.setStyleSheet("""
             QPushButton {
                font: 63 10pt \"Bahnschrift SemiBold\";
                border-radius: 10px;
                background-color: white;
             }
             QPushButton:focus:pressed {
                 background-color: rgb(100,100,100);   
             }
             QPushButton:hover {
                 background-color: rgb(200,200,200);  
             }
        """)
        self.backButton.clicked.connect(self.backBtn)

        self.homeButton = QtWidgets.QPushButton(Form)
        self.homeButton.setGeometry(QtCore.QRect(900, 700, 200, 40))
        self.homeButton.setObjectName("homeButton")
        self.homeButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.homeButton.setText("BACK TO MAIN")
        self.homeButton.setStyleSheet("""
             QPushButton {
                font: 63 10pt \"Bahnschrift SemiBold\";
                border-radius: 10px;
                background-color: white;
             }
             QPushButton:focus:pressed {
                 background-color: rgb(100,100,100);   
             }
             QPushButton:hover {
                 background-color: rgb(200,200,200);  
             }
        """)
        self.homeButton.clicked.connect(self.homeBtn)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowIcon(QtGui.QIcon('icon.png'))
        self.label1.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">N A N Y A N G    &nbsp;    T E C H O L O G I C A L    &nbsp;     U N I V E R S I T Y </span></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">NORTH SPINE CANTEEN</span></p></body></html>"))
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setWindowTitle(_translate("Form", "Available Stalls"))

#Stalls Window
class Ui_CustomStallsWindow(QtWidgets.QWidget):

    def realTimeClock(self, Form):
        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000)
        self.dClock = QtWidgets.QLabel(Form)
        self.dClock.setGeometry(QtCore.QRect(1000, 10, 190, 20))
        self.dClock.setObjectName("dClock")
        self.dClock.setStyleSheet('QLabel{color: black;}')
        self.dClock.raise_()
        self.timer.timeout.connect(self.displayTime)
        self.timer.start()

    def displayTime(self):
        self.currentDateTime = QtCore.QDateTime.currentDateTime()
        self.strCurrentDateTime = (self.currentDateTime.toString("ddd d/MMM/yy hh:mm:ss"))
        self.dClock.setText(self.currentDateTime.toString("ddd d/MMM/yy hh:mm:ss"))

    def chosenStall(self, stall):

        fChosen = open("chosenStall.txt", "w+")
        fChosen.write(stall)
        fChosen.close()

        self.main = Ui_MenuWindow()
        self.main.setupUi(self.main)
        self.main.show()

    def backBtn(self):
        MainWindow.hide()
        TodayWindow.show()
        self.hide()

    def homeBtn(self):
        MainWindow.show()
        TodayWindow.hide()
        self.hide()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(1200, 800)

        self.realTimeClock(Form)

        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(250, 120, 741, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold\";")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.centralwidget = QtWidgets.QWidget(Form)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget1.setGeometry(QtCore.QRect(0, 0, 1200, 41))
        self.verticalLayoutWidget1.setObjectName("verticalLayoutWidget1")
        self.verticalLayout1 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget1)
        self.verticalLayout1.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout1.setObjectName("verticalLayout1")

        self.label1 = QtWidgets.QLabel(self.verticalLayoutWidget1)
        self.label1.setStyleSheet("")
        self.label1.setObjectName("label")
        self.verticalLayout1.addWidget(self.label1)

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(-1, 39, 1200, 41))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setStyleSheet("font: 87 8pt \"Bahnschrift SemiBold\";")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)

        self.image = QtWidgets.QLabel(Form)
        self.image.setGeometry(QtCore.QRect(0, 0, 1200, 800))
        self.image.setStyleSheet("background-image: url(img3.jpg);")
        self.image.setText("")
        self.image.setObjectName("image")
        self.image.lower()
        
        self.label.setText("PICK A STALL TO VIEW THEIR MENU:")
        self.label.setStyleSheet("""
                    font: 63 20pt \"Bahnschrift SemiBold\";
                 """)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        
        fStalls = open("stalls.txt", "r")
        readlines = fStalls.read()
        fSLines = readlines.split(",")
        self.buttons = []
        self.stallChosen = ""
        for i in range(len(fSLines)):
            fSLines[i] = fSLines[i].replace("_"," ")
            self.buttons.append(fSLines[i])
            #print (self.buttons[i])
            self.buttons[i] = QtWidgets.QPushButton(Form)
            self.buttons[i].setGeometry(QtCore.QRect(450, 250+(i*70), 300, 50))
            self.buttons[i].setStyleSheet("font: 63 8pt \"Bahnschrift SemiBold\";")
            self.buttons[i].setObjectName(str(self.buttons[i]))
            self.buttons[i].setText(fSLines[i])
            self.buttons[i].setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.buttons[i].setStyleSheet("""
                 QPushButton {
                    font: 63 10pt \"Bahnschrift SemiBold\";
                    border-radius: 10px;
                    background-color: white;
                 }
                 QPushButton:focus:pressed {
                     background-color: rgb(100,100,100);   
                 }
                 QPushButton:hover {
                     background-color: rgb(200,200,200);  
                 }
            """)

            self.btn_grp = QtWidgets.QButtonGroup()
           # print(self.btn_grp)
            self.buttons[i].setCheckable(True)
            self.buttons[i].setEnabled(True)
            self.btn_grp.addButton(self.buttons[i])  
            self.btn_grp.setExclusive(True) 

        if len(fSLines) == 6:
            self.buttons[0].clicked.connect(lambda: self.chosenStall(self.buttons[0].text()))
            self.buttons[1].clicked.connect(lambda: self.chosenStall(self.buttons[1].text()))
            self.buttons[2].clicked.connect(lambda: self.chosenStall(self.buttons[2].text()))
            self.buttons[3].clicked.connect(lambda: self.chosenStall(self.buttons[3].text()))
            self.buttons[4].clicked.connect(lambda: self.chosenStall(self.buttons[4].text()))
            self.buttons[5].clicked.connect(lambda: self.chosenStall(self.buttons[5].text()))

        self.backButton = QtWidgets.QPushButton(Form)
        self.backButton.setGeometry(QtCore.QRect(100, 700, 200, 40))
        self.backButton.setObjectName("backButton")
        self.backButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.backButton.setText("BACK")
        self.backButton.setStyleSheet("""
             QPushButton {
                font: 63 10pt \"Bahnschrift SemiBold\";
                border-radius: 10px;
                background-color: white;
             }
             QPushButton:focus:pressed {
                 background-color: rgb(100,100,100);   
             }
             QPushButton:hover {
                 background-color: rgb(200,200,200);  
             }
        """)
        self.backButton.clicked.connect(self.backBtn)

        self.homeButton = QtWidgets.QPushButton(Form)
        self.homeButton.setGeometry(QtCore.QRect(900, 700, 200, 40))
        self.homeButton.setObjectName("homeButton")
        self.homeButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.homeButton.setText("BACK TO MAIN")
        self.homeButton.setStyleSheet("""
             QPushButton {
                font: 63 10pt \"Bahnschrift SemiBold\";
                border-radius: 10px;
                background-color: white;
             }
             QPushButton:focus:pressed {
                 background-color: rgb(100,100,100);   
             }
             QPushButton:hover {
                 background-color: rgb(200,200,200);  
             }
        """)
        self.homeButton.clicked.connect(self.homeBtn)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setWindowTitle(_translate("Form", "Available Stalls"))
        Form.setWindowIcon(QtGui.QIcon('icon.png'))
        self.label1.setText(_translate("TodayWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">N A N Y A N G    &nbsp;    T E C H O L O G I C A L    &nbsp;     U N I V E R S I T Y </span></p></body></html>"))
        self.label_2.setText(_translate("TodayWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">NORTH SPINE CANTEEN</span></p></body></html>"))

#Stalls Window
class Ui_StallsWindow(QtWidgets.QWidget):

    def realTimeClock(self, Form):
        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000)
        self.dClock = QtWidgets.QLabel(Form)
        self.dClock.setGeometry(QtCore.QRect(1000, 10, 190, 20))
        self.dClock.setObjectName("dClock")
        self.dClock.setStyleSheet('QLabel{color: black;}')
        self.dClock.raise_()
        self.timer.timeout.connect(self.displayTime)
        self.timer.start()

    def displayTime(self):
        self.currentDateTime = QtCore.QDateTime.currentDateTime()
        self.strCurrentDateTime = (self.currentDateTime.toString("ddd d/MMM/yy hh:mm:ss"))
        self.dClock.setText(self.currentDateTime.toString("ddd d/MMM/yy hh:mm:ss"))

    def chosenStall(self, stall):

        fChosen = open("chosenStall.txt", "w+")
        fChosen.write(stall)
        fChosen.close()

        self.main = Ui_MenuWindow()
        self.main.setupUi(self.main)
        self.main.show()

    def backBtn(self):
        MainWindow.show()
        TodayWindow.hide()
        self.hide()

    def homeBtn(self):
        MainWindow.show()
        TodayWindow.hide()
        self.hide()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(1200, 800)

        self.realTimeClock(Form)

        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(250, 120, 741, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold\";")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.centralwidget = QtWidgets.QWidget(Form)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget1.setGeometry(QtCore.QRect(0, 0, 1200, 41))
        self.verticalLayoutWidget1.setObjectName("verticalLayoutWidget1")
        self.verticalLayout1 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget1)
        self.verticalLayout1.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout1.setObjectName("verticalLayout1")

        self.label1 = QtWidgets.QLabel(self.verticalLayoutWidget1)
        self.label1.setStyleSheet("")
        self.label1.setObjectName("label")
        self.verticalLayout1.addWidget(self.label1)

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(-1, 39, 1200, 41))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setStyleSheet("font: 87 8pt \"Bahnschrift SemiBold\";")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)

        self.image = QtWidgets.QLabel(Form)
        self.image.setGeometry(QtCore.QRect(0, 0, 1200, 800))
        self.image.setStyleSheet("background-image: url(img3.jpg);")
        self.image.setText("")
        self.image.setObjectName("image")
        self.image.lower()
        
        self.label.setText("PICK A STALL TO VIEW THEIR MENU:")
        self.label.setStyleSheet("""
                    font: 63 20pt \"Bahnschrift SemiBold\";
                 """)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        
        fStalls = open("stalls.txt", "r")
        readlines = fStalls.read()
        fSLines = readlines.split(",")
        self.buttons = []
        self.stallChosen = ""
        for i in range(len(fSLines)):
            fSLines[i] = fSLines[i].replace("_"," ")
            self.buttons.append(fSLines[i])
            #print (self.buttons[i])
            self.buttons[i] = QtWidgets.QPushButton(Form)
            self.buttons[i].setGeometry(QtCore.QRect(450, 250+(i*70), 300, 50))
            self.buttons[i].setStyleSheet("font: 63 8pt \"Bahnschrift SemiBold\";")
            self.buttons[i].setObjectName(str(self.buttons[i]))
            self.buttons[i].setText(fSLines[i])
            self.buttons[i].setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.buttons[i].setStyleSheet("""
                 QPushButton {
                    font: 63 10pt \"Bahnschrift SemiBold\";
                    border-radius: 10px;
                    background-color: white;
                 }
                 QPushButton:focus:pressed {
                     background-color: rgb(100,100,100);   
                 }
                 QPushButton:hover {
                     background-color: rgb(200,200,200);  
                 }
            """)

            self.btn_grp = QtWidgets.QButtonGroup()
           # print(self.btn_grp)
            self.buttons[i].setCheckable(True)
            self.buttons[i].setEnabled(True)
            self.btn_grp.addButton(self.buttons[i])  
            self.btn_grp.setExclusive(True) 

        if len(fSLines) == 6:
            self.buttons[0].clicked.connect(lambda: self.chosenStall(self.buttons[0].text()))
            self.buttons[1].clicked.connect(lambda: self.chosenStall(self.buttons[1].text()))
            self.buttons[2].clicked.connect(lambda: self.chosenStall(self.buttons[2].text()))
            self.buttons[3].clicked.connect(lambda: self.chosenStall(self.buttons[3].text()))
            self.buttons[4].clicked.connect(lambda: self.chosenStall(self.buttons[4].text()))
            self.buttons[5].clicked.connect(lambda: self.chosenStall(self.buttons[5].text()))

        self.backButton = QtWidgets.QPushButton(Form)
        self.backButton.setGeometry(QtCore.QRect(100, 700, 200, 40))
        self.backButton.setObjectName("backButton")
        self.backButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.backButton.setText("BACK")
        self.backButton.setStyleSheet("""
             QPushButton {
                font: 63 10pt \"Bahnschrift SemiBold\";
                border-radius: 10px;
                background-color: white;
             }
             QPushButton:focus:pressed {
                 background-color: rgb(100,100,100);   
             }
             QPushButton:hover {
                 background-color: rgb(200,200,200);  
             }
        """)
        self.backButton.clicked.connect(self.backBtn)

        self.homeButton = QtWidgets.QPushButton(Form)
        self.homeButton.setGeometry(QtCore.QRect(900, 700, 200, 40))
        self.homeButton.setObjectName("homeButton")
        self.homeButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.homeButton.setText("BACK TO MAIN")
        self.homeButton.setStyleSheet("""
             QPushButton {
                font: 63 10pt \"Bahnschrift SemiBold\";
                border-radius: 10px;
                background-color: white;
             }
             QPushButton:focus:pressed {
                 background-color: rgb(100,100,100);   
             }
             QPushButton:hover {
                 background-color: rgb(200,200,200);  
             }
        """)
        self.homeButton.clicked.connect(self.homeBtn)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setWindowTitle(_translate("Form", "Available Stalls"))
        Form.setWindowIcon(QtGui.QIcon('icon.png'))
        self.label1.setText(_translate("TodayWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">N A N Y A N G    &nbsp;    T E C H O L O G I C A L    &nbsp;     U N I V E R S I T Y </span></p></body></html>"))
        self.label_2.setText(_translate("TodayWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">NORTH SPINE CANTEEN</span></p></body></html>"))
   
class Ui_MenuWindow(QtWidgets.QWidget):

    def realTimeClock(self, Form):
        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000)
        self.dClock = QtWidgets.QLabel(Form)
        self.dClock.setGeometry(QtCore.QRect(1000, 10, 190, 20))
        self.dClock.setObjectName("dClock")
        self.dClock.setStyleSheet('QLabel{color: black;}')
        self.dClock.raise_()
        self.timer.timeout.connect(self.displayTime)
        self.timer.start()

    def displayTime(self):
        self.currentDateTime = QtCore.QDateTime.currentDateTime()
        self.strCurrentDateTime = (self.currentDateTime.toString("ddd d/MMM/yy hh:mm:ss"))
        self.dClock.setText(self.currentDateTime.toString("ddd d/MMM/yy hh:mm:ss"))

    def backBtn(self):
        MainWindow.hide()
        self.hide()

    def homeBtn(self):
        MainWindow.show()
        TodayWindow.hide()
        self.hide()

    #Function for wait time button
    def waitTimeBtn(self):
        self.main = Ui_Queue()
        self.main.setupUi(self.main)
        self.main.show()

    #function to check operating hours
    def opHoursBtn(self):
        self.main = Ui_OpHours()
        self.main.setupUi(self.main)
        self.main.show()

    #Function to Get Stalls text file info
    def getFile(self):

        #reassigning stalls variable to match textfile format (e.g, 'Western Food' to 'Western_Food')
        self.stalls = self.stalls.replace(" ", "_")
        
        #Opening the text file with date and time that user has input
        self.dateTimeFile = open("cdt.txt", "r")
        self.dateTimelines = self.dateTimeFile.read()
        self.dateTimeList = self.dateTimelines.split(",")

        #declaring a dictionary to handle stall information
        self.stallDict = {}

        #opening the individual stall file and splitting into list
        self.menuFile = open(self.stalls + ".txt", "r")
        self.menulines = self.menuFile.read()
        self.menuList = self.menulines.split("\n")

        #declaring days of week as a list for future reference
        self.dayWeek = [0, 1, 2, 4, 5, 6]
        #declaring menu list for the chosen date
        self.dayMenuList = []
        #declaring label for each item of the meu
        self.label=[]
        self.foodList = []
        self.stallList = []
        self.menuDict = {}

        #declaring list for breakfast, lunch and dinner menu
        self.newList = [[],[],[]]

        #creating file to write user input for waiting time
        minFile = open("wait_time.txt", "w+") 
        minFile.write(self.menuList[-1])
        minFile.close()

        for i in range(7):
            #assigning each day's items as a dictionary
            self.dayMenuList.append(self.menuList[i])
            self.stallDict[self.dayMenuList[i][:3]] = self.dayMenuList[i][3:].split("/")
        
    #defining function to convert short form of days in textfile into full length
    def convertDayFormat(self, day):
        if day == "mon":
            day = "Monday"
        elif day == "tue":
            day = "Tuesday"
        elif day == "wed":
            day = "Wednesday"
        elif day == "thu":
            day = "Thursday"
        elif day == "fri":
            day = "Friday"
        elif day == "sat":
            day = "Saturday"
        else:
            day = "Sunday"
        return day

    #Defining function to get operating hours of each stall and assigning them to a list depending on which meal times they belong to
    def getOpHours(self):
        self.allDayList = []
        self.bfastList = []
        self.brunchList = []
        self.lunchList = []
        self.lunnerList = []
        self.dinnerList = []
        self.closeList = []

        for i in self.stallDict:
            if self.stallDict[i][0] == "08301930":
                i = self.convertDayFormat(i)
                self.allDayList.append(i)
            elif self.stallDict[i][0] == "08301230":
                i = self.convertDayFormat(i)
                self.bfastList.append(i)
            elif self.stallDict[i][0] == "08301630":
                i = self.convertDayFormat(i)
                self.brunchList.append(i)
            elif self.stallDict[i][0] == "12301630":
                i = self.convertDayFormat(i)
                self.lunchList.append(i)
            elif self.stallDict[i][0] == "12301930":
                i = self.convertDayFormat(i)
                self.lunnerList.append(i)
            elif self.stallDict[i][0] == "16301930":
                i = self.convertDayFormat(i)
                self.dinnerList.append(i)
            elif self.stallDict[i][0] == "00000000":
                i = self.convertDayFormat(i)
                self.closeList.append(i)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(1200, 800)

        self.realTimeClock(Form)

        self.centralwidget = QtWidgets.QWidget(Form)
        self.centralwidget.setObjectName("centralwidget")

        fStalls = open("chosenStall.txt", "r")
        print (fStalls)
        self.stalls = fStalls.read()
        fStalls.close()

        self.stallName = QtWidgets.QLabel(self.centralwidget)
        self.stallName.setGeometry(QtCore.QRect(0, 20, 1200, 50))
        self.stallName.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold\";")
        self.stallName.setObjectName("stallName")
        self.stallName.setText(self.stalls)
        self.stallName.setAlignment(QtCore.Qt.AlignCenter)
        self.stallName.raise_()

        self.image = QtWidgets.QLabel(Form)
        self.image.setGeometry(QtCore.QRect(0, 0, 1200, 800))
        self.image.setStyleSheet("background-image: url(img4.jpg);")
        self.image.setObjectName("image")
        self.image.lower()

       # print (readlines)
        print("1")
        print(self.stalls)

        self.getFile()
        self.getOpHours()
        print(self.bfastList)
        print(self.lunchList)
        print(self.dinnerList)

        #operating hours button
        self.opHoursButton = QtWidgets.QPushButton(Form)
        self.opHoursButton.setGeometry(QtCore.QRect(620, 700, 300, 40))
        self.opHoursButton.setStyleSheet("font: 63 16pt \"Bahnschrift SemiBold\";")
        self.opHoursButton.setObjectName("opHoursButton")

        self.opHoursButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.opHoursButton.setStyleSheet("""
             QPushButton {
                font: 63 10pt \"Bahnschrift SemiBold\";
                border-radius: 10px;
                background-color: white;
             }
             QPushButton:focus:pressed {
                 background-color: rgb(100,100,100);   
             }
             QPushButton:hover {
                 background-color: rgb(200,200,200);  
             }
        """)
        self.opHoursButton.clicked.connect(self.opHoursBtn)
        self.opHoursButton.setText("CHECK OPERATING HOURS")

        self.waitTimeButton = QtWidgets.QPushButton(Form)
        self.waitTimeButton.setGeometry(QtCore.QRect(280, 700, 300, 40))
        self.waitTimeButton.setStyleSheet("font: 63 16pt \"Bahnschrift SemiBold\";")
        self.waitTimeButton.setObjectName("waitTimeButton")
        self.waitTimeButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.waitTimeButton.setStyleSheet("""
             QPushButton {
                font: 63 10pt \"Bahnschrift SemiBold\";
                border-radius: 10px;
                background-color: white;
             }
             QPushButton:focus:pressed {
                 background-color: rgb(100,100,100);   
             }
             QPushButton:hover {
                 background-color: rgb(200,200,200);  
             }
        """)
        self.waitTimeButton.clicked.connect(self.waitTimeBtn)

        #allday
        self.allHours = []
        self.openLabel = QtWidgets.QLabel(Form)
        self.openLabel.setGeometry(QtCore.QRect(700, 40, 500, 200))
        self.openLabel.setObjectName(str(self.openLabel))
        self.openLabel.setText("THE STALL IS OPENED FOR \n BREAKFAST, LUNCH & DINNER ON: ")
        self.openLabel.setStyleSheet("font: 63 12pt \"Bahnschrift SemiBold\";")

        #craeting label to display the day(s) which chosen stall is opened from breakfast to dinner
        for i in range(len(self.allDayList)):
            self.allHours.append(str(i))
            self.allHours[i] = QtWidgets.QLabel(Form)
            self.allHours[i].setGeometry(QtCore.QRect(700, 90+(i*30), 500, 200))
            self.allHours[i].setObjectName(str(self.allHours[i]))
            self.allHours[i].setText(self.allDayList[i])
            self.allHours[i].setStyleSheet("font: 63 12pt \"Bahnschrift\";")      
        
        #creating labels to display day(s) which stall is closed
        self.closedHours = []
        self.closeLabel = QtWidgets.QLabel(Form)
        self.closeLabel.setGeometry(QtCore.QRect(700, 197, 500, 200))
        self.closeLabel.setObjectName(str(self.closeLabel))
        self.closeLabel.setText("THE STALL IS CLOSED ON: ")
        self.closeLabel.setStyleSheet("font: 63 12pt \"Bahnschrift SemiBold\";")

        for i in range(len(self.closeList)):
            self.closedHours.append(str(i))
            self.closedHours[i] = QtWidgets.QLabel(Form)
            self.closedHours[i].setGeometry(QtCore.QRect(700, 227+(i*30), 500, 200))
            self.closedHours[i].setObjectName(str(self.closedHours[i]))
            self.closedHours[i].setText(self.closeList[i])
            self.closedHours[i].setStyleSheet("font: 63 12pt \"Bahnschrift\";")
            self.waitTimeButton.setEnabled(False)

        self.bfastHours = []
        self.brunchHours = []
        self.lunchHours = []
        self.lunnerHours = []
        self.dinnerHours = []

        self.partialLabel = QtWidgets.QLabel(Form)
        self.partialLabel.setGeometry(QtCore.QRect(700, 290, 500, 200))
        self.partialLabel.setObjectName(str(self.partialLabel))
        self.partialLabel.setText("THE STALL IS PARTIALLY OPENED")
        self.partialLabel.setStyleSheet("font: 63 12pt \"Bahnschrift SemiBold\";")

        #creating labels to display day(s) which stall is opened for breakfast only
        if len(self.bfastList) > 0:
            self.bfastLabel = QtWidgets.QLabel(Form)
            self.bfastLabel.setGeometry(QtCore.QRect(700, 320, 500, 200))
            self.bfastLabel.setObjectName(str(self.bfastLabel))
            self.bfastLabel.setText("FOR BREAKFAST ON:")
            self.bfastLabel.setStyleSheet("font: 63 12pt \"Bahnschrift SemiBold\";")

            for i in range(len(self.bfastList)):
                self.bfastHours.append(str(i))
                self.bfastHours[i] = QtWidgets.QLabel(Form)
                self.bfastHours[i].setGeometry(QtCore.QRect(700, 350+(i*30), 500, 200))
                self.bfastHours[i].setObjectName(str(self.bfastHours[i]))
                self.bfastHours[i].setText(self.bfastList[i])
                self.bfastHours[i].setStyleSheet("font: 63 12pt \"Bahnschrift\";")
       
       #creating labels to display day(s) which stall is opened for breakfast and lunch only
        if len(self.brunchList) > 0:
            self.brunchLabel = QtWidgets.QLabel(Form)
            self.brunchLabel.setGeometry(QtCore.QRect(700, 400, 500, 200))
            self.brunchLabel.setObjectName(str(self.brunchLabel))
            self.brunchLabel.setText("FOR BREAKFAST & LUNCH ON:")
            self.brunchLabel.setStyleSheet("font: 63 12pt \"Bahnschrift SemiBold\";")

            for i in range(len(self.brunchList)):
                self.brunchHours.append(str(i))
                self.brunchHours[i] = QtWidgets.QLabel(Form)
                self.brunchHours[i].setGeometry(QtCore.QRect(700, 430+(i*30), 500, 200))
                self.brunchHours[i].setObjectName(str(self.brunchHours[i]))
                self.brunchHours[i].setText(self.brunchList[i])
                self.brunchHours[i].setStyleSheet("font: 63 12pt \"Bahnschrift\";")

        #creating labels to display day(s) which stall is opened for lunch only
        if len(self.lunchList) > 0:
            self.lunchLabel = QtWidgets.QLabel(Form)
            self.lunchLabel.setGeometry(QtCore.QRect(700, 480, 500, 200))
            self.lunchLabel.setObjectName(str(self.lunchLabel))
            self.lunchLabel.setText("FOR LUNCH ON:")
            self.lunchLabel.setStyleSheet("font: 63 12pt \"Bahnschrift SemiBold\";")

            for i in range(len(self.lunchList)):
                self.lunchHours.append(str(i))
                self.lunchHours[i] = QtWidgets.QLabel(Form)
                self.lunchHours[i].setGeometry(QtCore.QRect(700, 510+(i*30), 500, 200))
                self.lunchHours[i].setObjectName(str(self.lunchHours[i]))
                self.lunchHours[i].setText(self.lunchList[i])
                self.lunchHours[i].setStyleSheet("font: 63 12pt \"Bahnschrift\";")

        #creating labels to display day(s) which stall is opened for lunch and dinner only
        if len(self.lunnerList) > 0:
            self.lunnerLabel = QtWidgets.QLabel(Form)
            self.lunnerLabel.setGeometry(QtCore.QRect(700, 510, 500, 100))
            self.lunnerLabel.setObjectName(str(self.lunnerLabel))
            self.lunnerLabel.setText("FOR LUNCH & DINNER ON:")
            self.lunnerLabel.setStyleSheet("font: 63 12pt \"Bahnschrift SemiBold\";")

            for i in range(len(self.lunnerList)):
                self.lunnerHours.append(str(i))
                self.lunnerHours[i] = QtWidgets.QLabel(Form)
                self.lunnerHours[i].setGeometry(QtCore.QRect(700, 540+(i*30), 500, 100))
                self.lunnerHours[i].setObjectName(str(self.lunnerHours[i]))
                self.lunnerHours[i].setText(self.lunnerList[i])
                self.lunnerHours[i].setStyleSheet("font: 63 12pt \"Bahnschrift\";")

        #creating labels to display day(s) which stall is opened for dinner only
        if len(self.dinnerList) > 0:
            self.dinnerLabel = QtWidgets.QLabel(Form)
            self.dinnerLabel.setGeometry(QtCore.QRect(700, 540, 500, 100))
            self.dinnerLabel.setObjectName(str(self.dinnerLabel))
            self.dinnerLabel.setText("FOR DINNER ON:")
            self.dinnerLabel.setStyleSheet("font: 63 12pt \"Bahnschrift SemiBold\";")

            for i in range(len(self.dinnerList)):
                self.dinnerHours.append(str(i))
                self.dinnerHours[i] = QtWidgets.QLabel(Form)
                self.dinnerHours[i].setGeometry(QtCore.QRect(700, 570+(i*30), 500, 100))
                self.dinnerHours[i].setObjectName(str(self.dinnerHours[i]))
                self.dinnerHours[i].setText(self.dinnerList[i])
                self.dinnerHours[i].setStyleSheet("font: 63 12pt \"Bahnschrift\";")

        #if stalled is closed for the day
        if self.stallDict[self.dateTimeList[-1].lower()][0] == "00000000":
            self.noMenu = QtWidgets.QLabel(Form)
            self.noMenu.setGeometry(QtCore.QRect(100, 200, 500, 200))
            self.noMenu.setObjectName("noMenu")
            self.noMenu.setStyleSheet("font: 63 14pt \"Bahnschrift SemiBold\";")
            self.noMenu.setText("The stall is closed at this time.")
            self.waitTimeButton.setEnabled(False)

        #if stall is closed for breakfast
        else:
            if 830 <= int(self.dateTimeList[0]) < 1230:
                if int(self.stallDict[self.dateTimeList[-1].lower()][1]) == 0:
                    self.noMenu = QtWidgets.QLabel(Form)
                    self.noMenu.setGeometry(QtCore.QRect(100, 200, 500, 200))
                    self.noMenu.setObjectName("noMenu")
                    self.noMenu.setStyleSheet("font: 63 14pt \"Bahnschrift SemiBold\";")
                    self.noMenu.setText("The stall is closed at this time.")
                    self.waitTimeButton.setEnabled(False)

            #if stall is closed for lunch
            if 1230 <= int(self.dateTimeList[0]) < 1630:
                if int(self.stallDict[self.dateTimeList[-1].lower()][2]) == 0:
                    self.noMenu = QtWidgets.QLabel(Form)
                    self.noMenu.setGeometry(QtCore.QRect(100, 200, 500, 200))
                    self.noMenu.setObjectName("noMenu")
                    self.noMenu.setStyleSheet("font: 63 14pt \"Bahnschrift SemiBold\";")
                    self.noMenu.setText("The stall is closed at this time.")   
                    self.waitTimeButton.setEnabled(False)

            #if stall is closed for dinner
            if 1630 <= int(self.dateTimeList[0]) <= 1930:
                if int(self.stallDict[self.dateTimeList[-1].lower()][3]) == 0:
                    self.noMenu = QtWidgets.QLabel(Form)
                    self.noMenu.setGeometry(QtCore.QRect(100, 200, 500, 200))
                    self.noMenu.setObjectName("noMenu")
                    self.noMenu.setStyleSheet("font: 63 14pt \"Bahnschrift SemiBold\";")
                    self.noMenu.setText("The stall is closed at this time.")
                    self.waitTimeButton.setEnabled(False)

            #if time is after op hours
            if 1930 < int(self.dateTimeList[0]) <= 2359:
                self.noMenu = QtWidgets.QLabel(Form)
                self.noMenu.setGeometry(QtCore.QRect(100, 200, 500, 200))
                self.noMenu.setObjectName("noMenu")
                self.noMenu.setStyleSheet("font: 63 14pt \"Bahnschrift SemiBold\";")
                self.noMenu.setText("The stall is closed at this time.")
                self.waitTimeButton.setEnabled(False)

            #if time is before op hours
            if 0000 <= int(self.dateTimeList[0]) < 830:
                self.noMenu = QtWidgets.QLabel(Form)
                self.noMenu.setGeometry(QtCore.QRect(100, 200, 500, 200))
                self.noMenu.setObjectName("noMenu")
                self.noMenu.setStyleSheet("font: 63 14pt \"Bahnschrift SemiBold\";")
                self.noMenu.setText("The stall is closed at this time.")
                self.waitTimeButton.setEnabled(False)

        #displaying stall menu
        if int(self.stallDict[self.dateTimeList[-1].lower()][0][:4]) < int(self.dateTimeList[0]) < int(self.stallDict[self.dateTimeList[-1].lower()][0][4:]):
                step = 0
                for i in range(6):     
                    self.label.append("i")
                    self.label[i] = QtWidgets.QLabel(Form)
                    self.label[i].setGeometry(QtCore.QRect(70, 150+(50*i), 600, 200))
                    self.label[i].setObjectName(str(self.label[i]))
                    self.label[i].setStyleSheet("font: 63 12pt \"Bahnschrift SemiBold\";")
                    self.waitTimeButton.setEnabled(True)

                    if 830 <= int(self.dateTimeList[0]) < 1230:
                        if int(self.stallDict[self.dateTimeList[-1].lower()][1][i+step:i+step+2]) != 0:
                            self.label[i].setText(self.menuList[int(self.stallDict[self.dateTimeList[-1].lower()][1][i+step:i+step+2])])
                            step+=1
                    elif 1230 <= int(self.dateTimeList[0]) < 1630:
                        if int(self.stallDict[self.dateTimeList[-1].lower()][2][i+step:i+step+2]) != 0:
                            self.label[i].setText(self.menuList[int(self.stallDict[self.dateTimeList[-1].lower()][2][i+step:i+step+2])])
                            step+=1
                        else:
                            pass
                    elif 1630 <= int(self.dateTimeList[0]) < 1930:
                        if int(self.stallDict[self.dateTimeList[-1].lower()][3][i+step:i+step+2]) != 0:
                            self.label[i].setText(self.menuList[int(self.stallDict[self.dateTimeList[-1].lower()][3][i+step:i+step+2])])
                            step+=1

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 90, 571, 41))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.menu = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.menu.setStyleSheet("font: 63 18pt \"Bahnschrift SemiBold\";")
        self.menu.setObjectName("menu")
        self.verticalLayout_2.addWidget(self.menu)

        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(620, 90, 121, 550))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.backButton = QtWidgets.QPushButton(Form)
        self.backButton.setGeometry(QtCore.QRect(50, 700, 200, 40))
        self.backButton.setObjectName("backButton")
        self.backButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.backButton.setText("BACK")
        self.backButton.setStyleSheet("""
             QPushButton {
                font: 63 10pt \"Bahnschrift SemiBold\";
                border-radius: 10px;
                background-color: white;
             }
             QPushButton:focus:pressed {
                 background-color: rgb(100,100,100);   
             }
             QPushButton:hover {
                 background-color: rgb(200,200,200);  
             }
        """)
        self.backButton.clicked.connect(self.backBtn)

        self.homeButton = QtWidgets.QPushButton(Form)
        self.homeButton.setGeometry(QtCore.QRect(950, 700, 200, 40))
        self.homeButton.setObjectName("homeButton")
        self.homeButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.homeButton.setText("BACK TO MAIN")
        self.homeButton.setStyleSheet("""
             QPushButton {
                font: 63 10pt \"Bahnschrift SemiBold\";
                border-radius: 10px;
                background-color: white;
             }
             QPushButton:focus:pressed {
                 background-color: rgb(100,100,100);   
             }
             QPushButton:hover {
                 background-color: rgb(200,200,200);  
             }
        """)
        self.homeButton.clicked.connect(self.homeBtn)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", str(self.stalls.replace("_", " ")) + " Menu"))
        Form.setWindowIcon(QtGui.QIcon('icon.png'))
        self.menu.setText(_translate("Form", "<html><head/><body><p align=\"center\">MENU FOR THE DAY:</p></body></html>"))
        self.waitTimeButton.setText(_translate("Form", "CHECK WAITING TIME"))

#Op Hours window
class Ui_OpHours(QtWidgets.QWidget):

    def submitBtn(self):
        self.hide()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(522, 454)

        self.hoursLabel =  QtWidgets.QLabel(Form)
        self.hoursLabel.setGeometry(QtCore.QRect(0, -100, 522, 454))
        self.hoursLabel.setStyleSheet("font: 63 12pt \"Bahnschrift SemiBold\";")
        self.hoursLabel.setObjectName("hoursLabel")
        self.hoursLabel.setText("STALL OPERATING HOURS: \n\n  BREAKFAST: \t 0830 - 1230 \n LUNCH: \t 1230 - 1630 \n DINNER: \t 1630 - 1930")
        self.hoursLabel.setAlignment(QtCore.Qt.AlignCenter)
        
        self.submitButton = QtWidgets.QPushButton(Form)
        self.submitButton.setGeometry(QtCore.QRect(160, 310, 211, 41))
        self.submitButton.setStyleSheet("font: 63 16pt \"Bahnschrift SemiBold\";")
        self.submitButton.setObjectName("submitButton")
        self.submitButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.submitButton.setText("OK")
        self.submitButton.setStyleSheet("""
             QPushButton {
                font: 63 10pt \"Bahnschrift SemiBold\";
                border-radius: 10px;
                background-color: white;
             }
             QPushButton:focus:pressed {
                 background-color: rgb(100,100,100);   
             }
             QPushButton:hover {
                 background-color: rgb(200,200,200);  
             }
        """)
        self.submitButton.clicked.connect(self.submitBtn)
        
    
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Operating Hours"))
        Form.setWindowIcon(QtGui.QIcon('icon.png'))
 
#Queue Window     
class Ui_Queue(QtWidgets.QWidget):

    def enableBtn(self):
        if len(self.textEdit.text()) == 0:
            self.submitButton.setEnabled(False)
        else:
            self.submitButton.setEnabled(True)

    def submitBtn(self):
        f = open("queue.txt", "w+")
        f.write(self.textEdit.text())
        f.close()

        self.main = Ui_Wait()
        self.main.setupUi(self.main)
        self.main.show()
        self.hide()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(522, 454)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 30, 501, 41))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.question = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.question.setStyleSheet("font: 63 12pt \"Bahnschrift SemiBold\";")
        self.question.setObjectName("question")
        self.verticalLayout.addWidget(self.question)

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 90, 501, 121))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.noPpl = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.noPpl.setStyleSheet("font: 63 16pt \"Bahnschrift SemiBold\";")
        self.noPpl.setObjectName("noPpl")
        self.verticalLayout_2.addWidget(self.noPpl)

        self.textEdit = QtWidgets.QLineEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(130, 230, 271, 51))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setInputMask("999")
        self.textEdit.setFocus()

        self.submitButton = QtWidgets.QPushButton(Form)
        self.submitButton.setGeometry(QtCore.QRect(160, 310, 211, 41))
        self.submitButton.setStyleSheet("font: 63 16pt \"Bahnschrift SemiBold\";")
        self.submitButton.setObjectName("submitButton")
        self.submitButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.submitButton.setText("OK")
        self.submitButton.setStyleSheet("""
             QPushButton {
                font: 63 10pt \"Bahnschrift SemiBold\";
                border-radius: 10px;
                background-color: white;
             }
             QPushButton:focus:pressed {
                 background-color: rgb(100,100,100);   
             }
             QPushButton:hover {
                 background-color: rgb(200,200,200);  
             }
        """)
        self.submitButton.setEnabled(False)
        self.textEdit.textChanged.connect(self.enableBtn)
        self.submitButton.clicked.connect(self.submitBtn)
        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Check Queue"))
        Form.setWindowIcon(QtGui.QIcon('icon.png'))
        self.question.setText(_translate("Form", "<html><head/><body><p align=\"center\">...how long do I wait?</p></body></html>"))
        self.noPpl.setText(_translate("Form", "<html><head/><body><p align=\"center\">ENTER THE NUMBER OF</p><p align=\"center\">PEOPLE IN THE QUEUE:</p></body></html>"))

#Wait Time Window
class Ui_Wait(QtWidgets.QWidget):
    def submitBtn(self):
        self.hide()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(522, 454)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 30, 501, 41))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.waitTime = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.waitTime.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold\";")
        self.waitTime.setObjectName("waitTime")
        self.verticalLayout.addWidget(self.waitTime)

        fq = open("queue.txt", "r")
        queueNum = fq.readlines()[0]
        fq.close()

        fw = open("wait_time.txt", "r")
        waitTime = fw.readlines()[0]
        fw.close()

        self.waitLabel = QtWidgets.QLabel(Form)
        self.waitLabel.setGeometry(QtCore.QRect(10, 109, 501, 101))
        self.waitLabel.setObjectName("waitLabel")
        self.waitLabel.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold\";")
        self.waitMin = int(queueNum) * int(waitTime)
        if int(self.waitMin) >= 60 and int(self.waitMin) < 120 :
            self.waitHour = 1
            self.waitMin = self.waitMin - 60
            self.waitLabel.setText(str(self.waitHour) + " hour and " + str(self.waitMin) + " minutes")
        elif int(self.waitMin) >= 120 and int(self.waitMin) < 180 :
            self.waitHour = 2
            self.waitMin = self.waitMin - 120
            self.waitLabel.setText(str(self.waitHour) + " hours and " + str(self.waitMin) + " minutes")
        elif int(self.waitMin) >= 180:
            self.waitLabel.setText("The queue is too long.")
        else:
            self.waitLabel.setText(str(self.waitMin) + " minutes")

        self.waitLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.submitButton = QtWidgets.QPushButton(Form)
        self.submitButton.setGeometry(QtCore.QRect(160, 310, 211, 41))
        self.submitButton.setStyleSheet("font: 63 16pt \"Bahnschrift SemiBold\";")
        self.submitButton.setObjectName("submitButton")
        self.submitButton.setText("OK")
        self.submitButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.submitButton.setStyleSheet("""
             QPushButton {
                font: 63 10pt \"Bahnschrift SemiBold\";
                border-radius: 10px;
                background-color: white;
             }
             QPushButton:focus:pressed {
                 background-color: rgb(100,100,100);   
             }
             QPushButton:hover {
                 background-color: rgb(200,200,200);  
             }
        """)
        self.submitButton.clicked.connect(self.submitBtn)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Wait Time"))
        Form.setWindowIcon(QtGui.QIcon('icon.png'))
        self.waitTime.setText(_translate("Form", "<html><head/><body><p align=\"center\">THE WAITING TIME IS:</p></body></html>"))

#on application execution
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.realTimeClock(MainWindow)
    
    TodayWindow = QtWidgets.QMainWindow(MainWindow)    
    todayui = Ui_SetToday()
    todayui.setupUi(TodayWindow)

    MainWindow.show()
    sys.exit(app.exec_())