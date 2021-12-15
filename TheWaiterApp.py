import pickle
import numpy as np
from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from bs4 import BeautifulSoup
import requests
model_ = pickle.load(open('model.pkl','rb'))
#logis = pickle.load(open('logis.pkl','rb'))

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Dialog.resize(596, 458)
        Dialog.setStyleSheet("QDialog#Dialog {\n"
" background-image: url(waiter-good-service1.jpg);\n"
" }\n"
"")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(90, 10, 371, 41))
        self.label.setStyleSheet("color: rgb(234, 234, 234);\n"
"font: 75 italic 26pt \"Courier New\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 80, 81, 31))
        self.label_2.setStyleSheet("color: rgb(234, 234, 234);\n"
"border-radius: 40px;\n"
"font: 75 italic 14pt \"Times New Roman\";")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(150, 80, 151, 31))
        self.lineEdit.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"border-radius: 9px;")
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 140, 81, 31))
        self.label_3.setStyleSheet("color: rgb(234, 234, 234);\n"
"border-radius: 40px;\n"
"font: 75 italic 14pt \"Times New Roman\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(40, 260, 81, 31))
        self.label_4.setStyleSheet("color: rgb(234, 234, 234);\n"
"border-radius: 40px;\n"
"font: 75 italic 14pt \"Times New Roman\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(40, 200, 81, 31))
        self.label_5.setStyleSheet("color: rgb(234, 234, 234);\n"
"border-radius: 40px;\n"
"font: 75 italic 14pt \"Times New Roman\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(40, 380, 81, 31))
        self.label_6.setStyleSheet("color: rgb(234, 234, 234);\n"
"border-radius: 40px;\n"
"font: 80 italic 14pt \"Times New Roman\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(40, 320, 81, 31))
        self.label_7.setStyleSheet("color: rgb(234, 234, 234);\n"
"border-radius: 40px;\n"
"font: 75 italic 14pt \"Times New Roman\";")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(370, 80, 91, 31))
        self.label_8.setStyleSheet("color: rgb(234, 234, 234);\n"
"border-radius: 40px;\n"
"font: 75 italic 14pt \"Times New Roman\";")
        self.label_8.setObjectName("label_8")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(450, 80, 121, 31))
        self.comboBox.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(470, 10, 121, 41))
        self.label_13.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(57, 28, 0, 255), stop:0.988636 rgba(209, 209, 209, 255));\n"
"border-radius: 20px;\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.label_13.setObjectName("label_13")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(430, 370, 91, 31))
        self.pushButton.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(156, 101, 70, 255));\n"
"border-radius: 8px;\n"
"text-decoration: underline;\n"
"font: 75 italic 14pt \"Times New Roman\";\n"
"color: white;")
        self.pushButton.setObjectName("pushButton")
        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(150, 320, 151, 31))
        self.comboBox_2.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"border-radius: 9px;")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(Dialog)
        self.comboBox_3.setGeometry(QtCore.QRect(150, 380, 151, 31))
        self.comboBox_3.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"background-color:rgb(203, 203, 203);\n"
"border-radius: 9px;")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(40, 420, 521, 31))
        self.label_9.setStyleSheet("\n"
"border-radius: 40px;\n"
"font: 40 italic 14pt \"Times New Roman\";")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(365, 201, 221, 151))
        self.label_10.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(57, 28, 0, 255), stop:0.988636 rgba(209, 209, 209, 255));\n"
"border-radius: 40px;\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_10.setObjectName("label_10")
        self.comboBox_4 = QtWidgets.QComboBox(Dialog)
        self.comboBox_4.setGeometry(QtCore.QRect(150, 200, 151, 31))
        self.comboBox_4.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"border-radius: 9px;")
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_5 = QtWidgets.QComboBox(Dialog)
        self.comboBox_5.setGeometry(QtCore.QRect(150, 260, 151, 31))
        self.comboBox_5.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"background-color:rgb(203, 203, 203);\n"
"border-radius: 9px;")
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_6 = QtWidgets.QComboBox(Dialog)
        self.comboBox_6.setGeometry(QtCore.QRect(150, 140, 151, 31))
        self.comboBox_6.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"background-color:rgb(203, 203, 203);\n"
"border-radius: 9px;")
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.pushButton.clicked.connect(self.output)
        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.comboBox.setItemText(0, _translate("Dialog", "USD"))
        self.comboBox.setItemText(3, _translate("Dialog", "NGN"))
        self.comboBox.setItemText(1, _translate("Dialog", "INR"))
        self.comboBox.setItemText(2, _translate("Dialog", "EUR"))
        self.label.setText(_translate("Dialog", "The Waiter\'s Tip"))
        self.label_2.setText(_translate("Dialog", "total-bill"))
        self.label_3.setText(_translate("Dialog", "sex"))
        self.label_4.setText(_translate("Dialog", "Day"))
        self.label_5.setText(_translate("Dialog", "smoker"))
        self.label_6.setText(_translate("Dialog", "Size"))
        self.label_7.setText(_translate("Dialog", "Time"))
        self.label_8.setText(_translate("Dialog", "currency"))
        self.pushButton.setText(_translate("Dialog", "Predict Tip"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "Lunch"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "Dinner"))
        self.comboBox_3.setItemText(0, _translate("Dialog", "1"))
        self.comboBox_3.setItemText(1, _translate("Dialog", "2"))
        self.comboBox_3.setItemText(2, _translate("Dialog", "3"))
        self.comboBox_3.setItemText(3, _translate("Dialog", "4"))
        self.comboBox_3.setItemText(4, _translate("Dialog", "5"))
        self.comboBox_3.setItemText(5, _translate("Dialog", "6"))
        self.label_9.setText(_translate("Dialog", "\"...predict the waiter\'s tip {A machine learning App }\""))
        self.comboBox_4.setItemText(0, _translate("Dialog", "Yes"))
        self.comboBox_4.setItemText(1, _translate("Dialog", "No"))
        self.comboBox_5.setItemText(0, _translate("Dialog", "Thursday"))
        self.comboBox_5.setItemText(1, _translate("Dialog", "Friday"))
        self.comboBox_5.setItemText(2, _translate("Dialog", "Saturday"))
        self.comboBox_5.setItemText(3, _translate("Dialog", "Sunday"))
        self.comboBox_6.setItemText(0, _translate("Dialog", "Male"))
        self.comboBox_6.setItemText(1, _translate("Dialog", "Female"))

    def current_date_time(self):
        time = datetime.now()
        return time

    def clock(self):
        time_ = self.current_date_time()
        hour_ = time_.hour
        mins_ = time_.minute
        merid = ['AM', 'PM']
        if hour_ < 12:
            gm = merid[0]
        else:
            gm = merid[1]
        concat_time = f'{hour_} : {mins_} {gm} '
        return concat_time

    def clock_display(self):
        while self.current_date_time().hour < 24:
            return self.clock()

    def output(self):
        total_bill = self.lineEdit.text()
        denomination = self.comboBox.currentText()
        Sex = self.comboBox_6.currentText()
        Smoker = self.comboBox_4.currentText()
        Day = self.comboBox_5.currentText()
        Time = self.comboBox_2.currentText()
        Size = self.comboBox_3.currentText()
        if Sex == 'Male':
            Sex = 0
        elif Sex == 'Female':
            Sex = 1
        if Smoker == 'No':
            Smoker = 0
        elif Smoker == 'Yes':
            Smoker = 1
        if Day == 'Thursday':
            Day = 0
        elif Day == 'Friday':
            Day = 1
        elif Day == 'Saturday':
            Day = 2
        elif Day == 'Sunday':
            Day = 3
        if Time == 'Lunch':
            Time = 0
        elif Time == 'Dinner':
            Time = 1
        amount_in_USD = scrapper(total_bill,denomination)
        inputt = np.array([float(amount_in_USD), float(Sex), float(Smoker), float(Day), float(Time), float(Size)])
        input_ = inputt.reshape(1, 6)
        amount = model_.predict(input_)[0]
        output = converter_output(amount,denomination)
        self.label_10.setText(f'The predicted amount \n to tip the waiter is \n{output} in {denomination}')
        self.label_13.setText(f'{self.clock()}')
        print(model_.predict(input_))

def scrapper(Amount=None,From=None):
    link = requests.get(f'https://www.xe.com/currencyconverter/convert/?Amount={Amount}&From={From}&To=USD').text
    soup = BeautifulSoup(link,'lxml')
    a = soup.find(class_='result__BigRate-sc-1bsijpp-1 iGrAod').text
    amount = a.split('.')
    amounT = f'{amount[0]}.{amount[1][:2]}'
    array = [x for x in amounT]
    if ',' in array:
        AMOUNT = amounT.split(',')
        join1 = AMOUNT[0]
        join2 = AMOUNT[1]
        amounT = f'{join1}{join2}'
    return amounT

def converter_output(fig=None,currency=None):
    link = requests.get(f'https://www.xe.com/currencyconverter/convert/?Amount={fig}&From=USD&To={currency}').text
    soup = BeautifulSoup(link, 'lxml')
    a = soup.find(class_='result__BigRate-sc-1bsijpp-1 iGrAod').text
    amount = a.split('.')
    amounT = f'{amount[0]}.{amount[1][:2]}'
    return amounT

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

