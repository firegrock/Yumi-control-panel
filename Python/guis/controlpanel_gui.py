# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cp.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, QObject

class Communicate(QObject):
    closeApp = pyqtSignal()

class Ui_ABBYumiControlPanel(object):
    def setupUi(self, ABBYumiControlPanel):
        ABBYumiControlPanel.setObjectName("ABBYumiControlPanel")
        ABBYumiControlPanel.resize(554, 347)
        self.centralwidget = QtWidgets.QWidget(ABBYumiControlPanel)
        self.centralwidget.setObjectName("centralwidget")

        self.robotConnect_Button = QtWidgets.QPushButton(self.centralwidget)
        self.robotConnect_Button.setGeometry(QtCore.QRect(120, 10, 121, 41))
        self.robotConnect_Button.setMouseTracking(False)
        self.robotConnect_Button.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Russia))
        self.robotConnect_Button.setObjectName("robotConnect_Button")

        self.robotIP_textBox = QtWidgets.QLineEdit(self.centralwidget)
        self.robotIP_textBox.setGeometry(QtCore.QRect(10, 10, 111, 31))
        self.robotIP_textBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.robotIP_textBox.setObjectName("robotIP_textBox")

        self.runCase_Button = QtWidgets.QPushButton(self.centralwidget)
        self.runCase_Button.setEnabled(False)
        self.runCase_Button.setGeometry(QtCore.QRect(120, 80, 121, 41))
        self.runCase_Button.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Russia))
        self.runCase_Button.setObjectName("runCase_Button")

        self.stopCase_Button = QtWidgets.QPushButton(self.centralwidget)
        self.stopCase_Button.setEnabled(False)
        self.stopCase_Button.setGeometry(QtCore.QRect(120, 110, 121, 41))
        self.stopCase_Button.setObjectName("stopCase_Button")

        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(315, 10, 281, 192))
        self.graphicsView.setObjectName("graphicsView")

        self.camera_connectButton = QtWidgets.QPushButton(self.centralwidget)
        self.camera_connectButton.setGeometry(QtCore.QRect(430, 200, 121, 41))
        self.camera_connectButton.setMouseTracking(False)
        self.camera_connectButton.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Russia))
        self.camera_connectButton.setObjectName("camera_connectButton")

        self.cameraIP_textBox = QtWidgets.QLineEdit(self.centralwidget)
        self.cameraIP_textBox.setGeometry(QtCore.QRect(320, 200, 111, 31))
        self.cameraIP_textBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.cameraIP_textBox.setObjectName("cameraIP_textBox")

        self.alcocase_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.alcocase_checkBox.setEnabled(False)
        self.alcocase_checkBox.setGeometry(QtCore.QRect(10, 60, 87, 20))
        self.alcocase_checkBox.setObjectName("alcocase_checkBox")

        self.assemble_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.assemble_checkBox.setEnabled(False)
        self.assemble_checkBox.setGeometry(QtCore.QRect(10, 80, 87, 20))
        self.assemble_checkBox.setObjectName("assemble_checkBox")

        self.VR_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.VR_checkBox.setEnabled(False)
        self.VR_checkBox.setGeometry(QtCore.QRect(10, 100, 87, 20))
        self.VR_checkBox.setObjectName("VR_checkBox")

        self.coffee_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.coffee_checkBox.setEnabled(False)
        self.coffee_checkBox.setGeometry(QtCore.QRect(10, 120, 87, 20))
        self.coffee_checkBox.setObjectName("coffee_checkBox")

        self.returnToCalPosition_Button = QtWidgets.QPushButton(self.centralwidget)
        self.returnToCalPosition_Button.setEnabled(False)
        self.returnToCalPosition_Button.setGeometry(QtCore.QRect(0, 260, 311, 41))
        self.returnToCalPosition_Button.setObjectName("returnToCalPosition_Button")

        self.signature_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.signature_checkBox.setEnabled(False)
        self.signature_checkBox.setGeometry(QtCore.QRect(10, 140, 87, 20))
        self.signature_checkBox.setObjectName("signature_checkBox")

        self.leadThrough_Button = QtWidgets.QPushButton(self.centralwidget)
        self.leadThrough_Button.setEnabled(False)
        self.leadThrough_Button.setGeometry(QtCore.QRect(0, 220, 311, 41))
        self.leadThrough_Button.setCheckable(True)
        self.leadThrough_Button.setObjectName("leadThrough_Button")

        ABBYumiControlPanel.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ABBYumiControlPanel)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 554, 22))
        self.menubar.setObjectName("menubar")

        ABBYumiControlPanel.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ABBYumiControlPanel)
        self.statusbar.setObjectName("statusbar")
        ABBYumiControlPanel.setStatusBar(self.statusbar)

        self.retranslateUi(ABBYumiControlPanel)
        QtCore.QMetaObject.connectSlotsByName(ABBYumiControlPanel)

    def retranslateUi(self, ABBYumiControlPanel):
        _translate = QtCore.QCoreApplication.translate
        ABBYumiControlPanel.setWindowTitle(_translate("ABBYumiControlPanel", "ABB Yumi Industry 4.0 control panel"))
        self.robotConnect_Button.setText(_translate("ABBYumiControlPanel", "Подлючиться"))
        self.robotIP_textBox.setText(_translate("ABBYumiControlPanel", "192.168.125.1"))
        self.runCase_Button.setText(_translate("ABBYumiControlPanel", "Запуск кейса"))
        self.stopCase_Button.setText(_translate("ABBYumiControlPanel", "Остановить"))
        self.camera_connectButton.setText(_translate("ABBYumiControlPanel", "Видео"))
        self.cameraIP_textBox.setText(_translate("ABBYumiControlPanel", "192.168.1.1"))
        self.alcocase_checkBox.setText(_translate("ABBYumiControlPanel", "Бармен"))
        self.assemble_checkBox.setText(_translate("ABBYumiControlPanel", "Сборка"))
        self.VR_checkBox.setText(_translate("ABBYumiControlPanel", "VR"))
        self.coffee_checkBox.setText(_translate("ABBYumiControlPanel", "Бариста"))
        self.returnToCalPosition_Button.setText(_translate("ABBYumiControlPanel", "Калибровочное положение"))
        self.signature_checkBox.setText(_translate("ABBYumiControlPanel", "Подпись"))
        self.leadThrough_Button.setText(_translate("ABBYumiControlPanel", " Ручная доводка"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ABBYumiControlPanel = QtWidgets.QMainWindow()
    ui = Ui_ABBYumiControlPanel()
    ui.setupUi(ABBYumiControlPanel)
    ABBYumiControlPanel.show()
    sys.exit(app.exec_())

