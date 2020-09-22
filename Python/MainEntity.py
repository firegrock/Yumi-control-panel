import sys
from RAPID import abb
from RAPID.yumi_g201 import start_barista

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QMainWindow

from Python.guis.controlpanel_gui import Ui_ABBYumiControlPanel

LeftHand = None
RightHand = None

class MainWindow(QMainWindow, Ui_ABBYumiControlPanel):
    def __init__(self, parent=None, *args, **kwargs):
        QMainWindow.__init__(self)
        self.__robotIsConnectedFlag = False
        self.__cameraIsConnectedFlag = False
        self.__choosedCase = 'None'
        self.__caseIsRunningFlag = False
        self.setupUi(self)

        self.robotConnect_Button.clicked.connect(self.connect_robot)
        self.runCase_Button.clicked.connect(self.runCase)
        self.stopCase_Button.clicked.connect(self.stopCase)

        self.alcocase_checkBox.stateChanged.connect(self.alcocase_checkBox_cliked)
        self.assemble_checkBox.stateChanged.connect(self.assemble_checkBox_cliked)
        self.VR_checkBox.stateChanged.connect(self.VR_checkBox_cliked)
        self.coffee_checkBox.stateChanged.connect(self.coffee_checkBox_cliked)
        self.signature_checkBox.stateChanged.connect(self.signature_checkBox_cliked)

    def set_enable(self):
        self.alcocase_checkBox.setEnabled(True)
        self.assemble_checkBox.setEnabled(True)
        self.VR_checkBox.setEnabled(True)
        self.coffee_checkBox.setEnabled(True)
        self.signature_checkBox.setEnabled(True)
        self.runCase_Button.setEnabled(True)
        self.leadThrough_Button.setEnabled(True)
        self.returnToCalPosition_Button.setEnabled(True)
        self.robotConnect_Button.setText("Отключиться")
        self.fakeUpdate()

    def set_disable(self):
        self.alcocase_checkBox.setEnabled(False)
        self.assemble_checkBox.setEnabled(False)
        self.VR_checkBox.setEnabled(False)
        self.coffee_checkBox.setEnabled(False)
        self.signature_checkBox.setEnabled(False)
        self.runCase_Button.setEnabled(False)
        self.leadThrough_Button.setEnabled(False)
        self.returnToCalPosition_Button.setEnabled(False)
        self.robotConnect_Button.setText("Подключиться")
        self.fakeUpdate()

    def set_enable_stopButton(self):
        self.stopCase_Button.setEnabled(True)
        self.runCase_Button.setEnabled(False)
        self.fakeUpdate()

    def set_disable_stopButton(self):
        self.stopCase_Button.setEnabled(False)
        self.runCase_Button.setEnabled(True)
        self.fakeUpdate()

    def set_enable_caseChoosing(self):
        self.alcocase_checkBox.setEnabled(True)
        self.assemble_checkBox.setEnabled(True)
        self.VR_checkBox.setEnabled(True)
        self.coffee_checkBox.setEnabled(True)
        self.signature_checkBox.setEnabled(True)
        self.stopCase_Button.setEnabled(False)
        self.runCase_Button.setEnabled(True)
        self.fakeUpdate()

    def set_disable_caseChoosing(self):
        self.alcocase_checkBox.setEnabled(False)
        self.assemble_checkBox.setEnabled(False)
        self.VR_checkBox.setEnabled(False)
        self.coffee_checkBox.setEnabled(False)
        self.signature_checkBox.setEnabled(False)
        self.stopCase_Button.setEnabled(False)
        self.runCase_Button.setEnabled(True)
        self.fakeUpdate()

    def setRobotIsConnectedFlag(self, value): # Запись
        self.__robotIsConnectedFlag = value
        if value == True:
            self.set_enable()
        elif value == False:
            self.set_disable()

    def getRobotIsConnectedFlag(self):        # Чтение
        return self.__robotIsConnectedFlag

    def setChoosedCase(self, value): # Запись
        self.__choosedCase = value
        print(self.__choosedCase)

    def getChoosedCase(self):        # Чтение
        return self.__choosedCase

    def connect_robot(self):
        if self.__robotIsConnectedFlag == False:
            try:
                self.setRobotIsConnectedFlag(True)
                LeftHand = abb.Robot(ip='192.168.125.1', port_motion=5000)
                RightHand = abb.Robot(ip='192.168.125.1', port_motion=5001)
            except Exception as exc:
                print(exc.args)
                #TODO: messagebox about exceptions
        elif self.__robotIsConnectedFlag == True:
            try:
                self.setRobotIsConnectedFlag(False)
                LeftHand = None
                RightHand = None
                #LeftHand = abb.Robot(ip='192.168.125.1', port_motion=5000)
                #RightHand = abb.Robot(ip='192.168.125.1', port_motion=5001)
            except Exception as exc:
                print(exc.args)
                #TODO: messagebox about exceptions

    def runCase(self):
        #TODO: this method
        self.set_disable_caseChoosing()
        self.set_enable_stopButton()
        self.__caseIsRunningFlag = True

    def stopCase(self):
        #TODO: this method
        self.set_enable_caseChoosing()
        self.set_disable_stopButton()
        self.__caseIsRunningFlag = False

    def alcocase_checkBox_cliked(self, int):
        if self.alcocase_checkBox.isChecked():
            self.setChoosedCase('alco')
            self.assemble_checkBox.setChecked(False)
            self.VR_checkBox.setChecked(False)
            self.coffee_checkBox.setChecked(False)
            self.signature_checkBox.setChecked(False)
        elif not self.alcocase_checkBox.isChecked() and self.__choosedCase == 'alco':
            self.setChoosedCase('none')

    def assemble_checkBox_cliked(self, int):
        if self.assemble_checkBox.isChecked():
            self.setChoosedCase('assemble')
            self.alcocase_checkBox.setChecked(False)
            self.VR_checkBox.setChecked(False)
            self.coffee_checkBox.setChecked(False)
            self.signature_checkBox.setChecked(False)
        elif not self.assemble_checkBox.isChecked() and self.__choosedCase == 'assemble':
            self.setChoosedCase('none')

    def VR_checkBox_cliked(self, int):
        if self.VR_checkBox.isChecked():
            self.setChoosedCase('VR')
            self.alcocase_checkBox.setChecked(False)
            self.assemble_checkBox.setChecked(False)
            self.coffee_checkBox.setChecked(False)
            self.signature_checkBox.setChecked(False)
        elif not self.VR_checkBox.isChecked() and self.__choosedCase == 'VR':
            self.setChoosedCase('none')

    def coffee_checkBox_cliked(self, int):
        if self.coffee_checkBox.isChecked():
            self.setChoosedCase('coffee')
            self.alcocase_checkBox.setChecked(False)
            self.assemble_checkBox.setChecked(False)
            self.VR_checkBox.setChecked(False)
            self.signature_checkBox.setChecked(False)
        elif not self.coffee_checkBox.isChecked() and self.__choosedCase == 'coffee':
            self.setChoosedCase('none')

    def signature_checkBox_cliked(self, int):
        if self.signature_checkBox.isChecked():
            self.setChoosedCase('sign')
            self.alcocase_checkBox.setChecked(False)
            self.assemble_checkBox.setChecked(False)
            self.VR_checkBox.setChecked(False)
            self.coffee_checkBox.setChecked(False)
        elif not self.signature_checkBox.isChecked() and self.__choosedCase == 'sign':
            self.setChoosedCase('none')

    def fakeUpdate(self):
        self.resize(QSize(554, 348))
        self.resize(QSize(554, 347))

    def run_barista(self):
        if(LeftHand is not None and RightHand is not None):
            start_barista(LeftHand, RightHand)
        else:
            #TODO: show MessageBox with error
            pass
    

def main():
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())

main()