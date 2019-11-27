# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\lollypop.OLOLADE\Desktop\Energy Audit APP\Code 2.0\UI\Flow\Start.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import resource
import Dashboard
import os
import json
from pprint import pprint


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.main_window = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(490, 397)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 30, 461, 331))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(40, 30))
        self.label.setMaximumSize(QtCore.QSize(100, 150))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/icons/icons/mechanics.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setScaledContents(False)
        self.label_2.setWordWrap(True)
        self.label_2.setOpenExternalLinks(False)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.line = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setMinimumSize(QtCore.QSize(400, 100))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.toolButton = QtWidgets.QToolButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setWeight(75)
        self.toolButton.setFont(font)
        self.toolButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/new-file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(30, 30))
        self.toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton.setAutoRaise(True)
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout.addWidget(self.toolButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.toolButton_2 = QtWidgets.QToolButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setWeight(75)
        self.toolButton_2.setFont(font)
        self.toolButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/open-folder-outline.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_2.setIcon(icon1)
        self.toolButton_2.setIconSize(QtCore.QSize(30, 30))
        self.toolButton_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_2.setAutoRaise(True)
        self.toolButton_2.setObjectName("toolButton_2")
        self.horizontalLayout.addWidget(self.toolButton_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def closeDb(self, event):
        print('closing app')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">WELCOME TO ENERGHX PLUS 2.0</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">The software is to help audit appliance, determine the power required for a installing a renewable energy (wind energy or solar energy) source on site, determine the energy required from a battery to power an electric vehicle and optimize energy consuming systems.</p></body></html>"))
        self.toolButton.setText(_translate("MainWindow", "Create New Project"))
        self.toolButton_2.setText(_translate("MainWindow", "Open Previous Project"))

        self.toolButton.clicked.connect(lambda: self.create_new_project({'rooms': {}, 'retrofit': {}}))
        self.toolButton_2.clicked.connect(lambda: self.open_new_project())
        MainWindow.setWindowTitle('Energhx Plus 2.0')

    def create_new_project(self, data, file_name=''):
        try:
            try:
                self.dboard_window.close()
            except AttributeError:
                pass
            self.dboard_window = QtWidgets.QMainWindow(self.centralwidget)
            # self.dboard_window.setWindowModality(QtCore.Qt.ApplicationModal)
            self.dboard_widget = Dashboard.Ui_MainWindow()
            self.dboard_widget.setupUi(self.dboard_window, data, file_name)
            self.dboard_window.show()
            self.dboard_widget.close.connect(self.close)
            self.main_window.setVisible(False)
        except Exception as e:
            print('Error Creating New Project -->>', type(e), str(e))

    def open_new_project(self, data=None):
        try:
            if data is None:
                fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self.centralwidget, "Select Project", "Lets See",
                                                                    "JSON(*.json)")
                if fileName:
                    with open(fileName) as f:
                        data = json.load(f)

                    self.create_new_project(data, fileName)
        except Exception as e:
            print('Error Opening New Project -->>', type(e), str(e))

    def close(self, open, data):
        print(open)
        pprint(data)
        try:
            if open:
                if data == {}:
                    self.open_new_project()
                else:
                    self.create_new_project(data)
            else:
                self.main_window.close()
                
        except Exception as e:
            print('Error Closing/Opening New Project -->>', type(e), str(e))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

