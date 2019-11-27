# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\lollypop.OLOLADE\Desktop\Energy Audit APP\Code 2.0\UI\Flow\add_appliance.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import resource
import json
from pprint import pprint


class Ui_MainWindow(QtCore.QObject):
    appliance_added = QtCore.pyqtSignal(dict)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(387, 345)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setContentsMargins(5, 5, 0, 0)
        self.gridLayout.setHorizontalSpacing(18)
        self.gridLayout.setVerticalSpacing(1)
        self.gridLayout.setObjectName("gridLayout")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setMinimumSize(QtCore.QSize(120, 23))
        self.comboBox.setMaximumSize(QtCore.QSize(150, 23))
        self.comboBox.setEditable(True)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 0, 2, 1, 2)
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setMinimumSize(QtCore.QSize(30, 30))
        self.label_7.setMaximumSize(QtCore.QSize(30, 30))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(":/icons/icons/clock-circular-outline.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(self.frame)
        self.spinBox.setMinimumSize(QtCore.QSize(80, 23))
        self.spinBox.setMaximumSize(QtCore.QSize(80, 23))
        self.spinBox.setObjectName("spinBox")
        self.gridLayout.addWidget(self.spinBox, 2, 2, 1, 1)
        self.spinBox_2 = QtWidgets.QSpinBox(self.frame)
        self.spinBox_2.setMinimumSize(QtCore.QSize(80, 23))
        self.spinBox_2.setMaximumSize(QtCore.QSize(80, 23))
        self.spinBox_2.setObjectName("spinBox_2")
        self.gridLayout.addWidget(self.spinBox_2, 3, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setMinimumSize(QtCore.QSize(30, 30))
        self.label_5.setMaximumSize(QtCore.QSize(30, 30))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/icons/icons/hash.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setMinimumSize(QtCore.QSize(30, 30))
        self.label_3.setMaximumSize(QtCore.QSize(30, 30))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/icons/icons/renewable-energy.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 3, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setMinimumSize(QtCore.QSize(120, 23))
        self.lineEdit.setMaximumSize(QtCore.QSize(150, 23))
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 2, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setMinimumSize(QtCore.QSize(30, 30))
        self.label.setMaximumSize(QtCore.QSize(30, 30))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/icons/icons/washing-machine (1).png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.frame)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 0, 4, 1, 1)
        self.toolButton = QtWidgets.QToolButton(self.frame)
        self.toolButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(30, 30))
        self.toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton.setAutoRaise(True)
        self.toolButton.setObjectName("toolButton")
        self.gridLayout.addWidget(self.toolButton, 4, 1, 1, 4, QtCore.Qt.AlignHCenter)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ADD AN APPLIANCE"))
        self.label_6.setText(_translate("MainWindow", "Units"))
        self.label_8.setText(_translate("MainWindow", "Operating Hours"))
        self.label_4.setText(_translate("MainWindow", "Power Rating"))
        self.label_2.setText(_translate("MainWindow", "Appliance Name"))
        self.checkBox.setText(_translate("MainWindow", "Fluorescent"))
        self.toolButton.setText(_translate("MainWindow", "ADD"))
        self.spinBox.setMinimum(1)
        self.spinBox_2.setMinimum(1)
        self.checkBox.setVisible(False)
        self.comboBox.currentTextChanged.connect(self.appliance_name_changed)
        with open('JSON files/retrofit_appliances.json') as f:
            appliances = json.load(f)
        self.comboBox.addItems(list(appliances.keys()))
        self.toolButton.clicked.connect(self.add_appliance)

    def add_appliance(self):
        temp_dict = {
            self.comboBox.currentText(): {
                'power_rating': float(self.lineEdit.text()),
                'units': self.spinBox.value(),
                'operating_hours': self.spinBox_2.value(),
            }
        }

        if self.checkBox.isChecked():
            temp_dict['fluorescent'] = True

        self.appliance_added.emit(temp_dict)

    def appliance_name_changed(self):
        self.checkBox.setVisible(self.comboBox.currentText().lower() == 'lightning')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

