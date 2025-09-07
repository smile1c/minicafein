# -*- coding: utf-8 -*-

import csv
import datetime
from PyQt5 import QtCore, QtGui, QtWidgets

all_price = 0
items_list = []

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(973, 833)
        self.listMenu = QtWidgets.QListView(Form)
        self.listMenu.setEnabled(True)
        self.listMenu.setGeometry(QtCore.QRect(550, 320, 351, 341))
        self.listMenu.setObjectName("listMenu")
        self.list_model = QtGui.QStandardItemModel(self.listMenu)
        self.listMenu.setModel(self.list_model)

        self.btt_Confirm = QtWidgets.QPushButton(Form)
        self.btt_Confirm.setGeometry(QtCore.QRect(550, 750, 351, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btt_Confirm.setFont(font)
        self.btt_Confirm.setObjectName("btt_Confirm")

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(60, 50, 181, 151))
        self.label.setStyleSheet("background-image: url(:/newPrefix/smoothie-menu-1.jpg);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/smoothie-menu-1.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(280, 50, 181, 151))
        self.label_2.setStyleSheet("background-image: url(:/newPrefix/smoothie-menu-2.jpg);")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/newPrefix/smoothie-menu-2.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(500, 50, 181, 151))
        self.label_3.setStyleSheet("background-image: url(:/newPrefix/Latte-Frappe.jpg);\n"
"")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/newPrefix/Latte-Frappe.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(60, 310, 181, 151))
        self.label_4.setStyleSheet("background-image: url(:/newPrefix/thai-tea.jpg);\n"
"")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/newPrefix/thai-tea.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(720, 50, 181, 151))
        self.label_5.setStyleSheet("background-image: url(:/newPrefix/smoothie-menu-1.jpg);\n"
"background-image: url(:/newPrefix/smoothie-menu-2.jpg);\n"
"background-image: url(:/newPrefix/smoothie-menu-2.jpg);")
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/newPrefix/Oreo.jpg"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(280, 310, 181, 151))
        self.label_6.setStyleSheet("background-image: url(:/newPrefix/smoothie-menu-1.jpg);")
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(":/newPrefix/menus-from-mango-5.jpg"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(60, 570, 181, 151))
        self.label_7.setStyleSheet("background-image: url(:/newPrefix/smoothie-menu-1.jpg);\n"
"")
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(":/newPrefix/coconut-smoothie.jpg"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")

        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(280, 570, 181, 151))
        self.label_8.setStyleSheet("background-image: url(:/newPrefix/smoothie-menu-1.jpg);\n"
"")
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap(":/newPrefix/Cocoa-Shake-Cornflakes.jpg"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")

        self.btt_Matcha = QtWidgets.QPushButton(Form)
        self.btt_Matcha.setGeometry(QtCore.QRect(80, 230, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btt_Matcha.setFont(font)
        self.btt_Matcha.setObjectName("btt_Matcha")

        self.btt_Strawberry_Yogurt = QtWidgets.QPushButton(Form)
        self.btt_Strawberry_Yogurt.setGeometry(QtCore.QRect(300, 230, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btt_Strawberry_Yogurt.setFont(font)
        self.btt_Strawberry_Yogurt.setObjectName("btt_Strawberry_Yogurt")

        self.btt_Latte = QtWidgets.QPushButton(Form)
        self.btt_Latte.setGeometry(QtCore.QRect(520, 230, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btt_Latte.setFont(font)
        self.btt_Latte.setObjectName("btt_Latte")

        self.btt_Oreo = QtWidgets.QPushButton(Form)
        self.btt_Oreo.setGeometry(QtCore.QRect(740, 230, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btt_Oreo.setFont(font)
        self.btt_Oreo.setObjectName("btt_Oreo")

        self.btt_Cha_Thai = QtWidgets.QPushButton(Form)
        self.btt_Cha_Thai.setGeometry(QtCore.QRect(80, 490, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btt_Cha_Thai.setFont(font)
        self.btt_Cha_Thai.setObjectName("btt_Cha_Thai")

        self.btt_mango = QtWidgets.QPushButton(Form)
        self.btt_mango.setGeometry(QtCore.QRect(300, 490, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btt_mango.setFont(font)
        self.btt_mango.setObjectName("btt_mango")

        self.btt_coconut = QtWidgets.QPushButton(Form)
        self.btt_coconut.setGeometry(QtCore.QRect(80, 750, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btt_coconut.setFont(font)
        self.btt_coconut.setObjectName("btt_coconut")

        self.btt_cocoa = QtWidgets.QPushButton(Form)
        self.btt_cocoa.setGeometry(QtCore.QRect(310, 750, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btt_cocoa.setFont(font)
        self.btt_cocoa.setObjectName("btt_cocoa")

        self.btt_Clear = QtWidgets.QPushButton(Form)
        self.btt_Clear.setGeometry(QtCore.QRect(550, 690, 351, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btt_Clear.setFont(font)
        self.btt_Clear.setObjectName("btt_Clear")

        self.label_TotalPrice = QtWidgets.QLabel(Form)
        self.label_TotalPrice.setGeometry(QtCore.QRect(550, 655, 351, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_TotalPrice.setFont(font)
        self.label_TotalPrice.setObjectName("label_TotalPrice")
        self.label_TotalPrice.setAlignment(QtCore.Qt.AlignCenter)

        self.retranslateUi(Form)
        self.btt_Matcha.clicked.connect(lambda: self.add_item("Matcha", 35))
        self.btt_Strawberry_Yogurt.clicked.connect(lambda: self.add_item("Strawberry", 45))
        self.btt_Latte.clicked.connect(lambda: self.add_item("Latte", 30))
        self.btt_Oreo.clicked.connect(lambda: self.add_item("Oreo", 40))
        self.btt_Cha_Thai.clicked.connect(lambda: self.add_item("Cha Thai", 40))
        self.btt_mango.clicked.connect(lambda: self.add_item("Mango", 45))
        self.btt_coconut.clicked.connect(lambda: self.add_item("Coconut", 30))
        self.btt_cocoa.clicked.connect(lambda: self.add_item("Cocoa", 35))
        self.btt_Clear.clicked.connect(self.clear_list)
        self.btt_Confirm.clicked.connect(self.save_report)  # Connect "Confirm" button to save_report function
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.update_confirm_button_state()  # Initialize button state

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Menu"))
        self.btt_Matcha.setText(_translate("Form", "Matcha\n35 Baht"))
        self.btt_Strawberry_Yogurt.setText(_translate("Form", "Strawberry Yogurt\n45 Baht"))
        self.btt_Latte.setText(_translate("Form", "Latte\n30 Baht"))
        self.btt_Oreo.setText(_translate("Form", "Oreo\n40 Baht"))
        self.btt_Cha_Thai.setText(_translate("Form", "Cha Thai\n40 Baht"))
        self.btt_mango.setText(_translate("Form", "Mango\n45 Baht"))
        self.btt_coconut.setText(_translate("Form", "Coconut\n30 Baht"))
        self.btt_cocoa.setText(_translate("Form", "Cocoa\n35 Baht"))
        self.btt_Clear.setText(_translate("Form", "Clear"))
        self.btt_Confirm.setText(_translate("Form", "Confirm"))
        self.label_TotalPrice.setText(_translate("Form", "Total Price: 0 Baht"))

    def add_item(self, item_name, item_price):
        global all_price
        global items_list
        item = QtGui.QStandardItem(f"{item_name}\t\t{item_price} Baht")
        self.list_model.appendRow(item)
        all_price += item_price
        items_list.append((item_name, item_price))
        self.update_total_price()
        self.update_confirm_button_state()  # Update button state
        self.label_TotalPrice.setVisible(True)

    def clear_list(self):
        global all_price
        global items_list
        self.list_model.clear()
        all_price = 0
        items_list = []
        self.update_total_price()
        self.update_confirm_button_state()  # Update button state
        self.label_TotalPrice.setVisible(False)

    def update_total_price(self):
        self.label_TotalPrice.setText(f"Total Price: {all_price} Baht")

    def update_confirm_button_state(self):
        if self.list_model.rowCount() == 0:
            self.btt_Confirm.setEnabled(False)
        else:
            self.btt_Confirm.setEnabled(True)

    def save_report(self):
        timestamp = datetime.datetime.now().strftime("%m/%d/%Y,%H:%M")
        with open('REPORT.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([timestamp])
            for item_name, item_price in items_list:
                writer.writerow([item_name, item_price])
            writer.writerow(['Total', all_price])
        self.clear_list()  # Clear the list and reset total price
        QtWidgets.QMessageBox.information(None, "Thank You", "Thank you for choosing our beverage menu; we appreciate your patronage!")


import Pic_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
