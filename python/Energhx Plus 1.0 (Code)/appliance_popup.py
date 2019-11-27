# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\lollypop.OLOLADE\Desktop\Energy Audit APP\Code 2.0\UI\Flow\appliance_popup.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import resource
import add_appliance
import multiple_app_select
from pprint import pprint


class Ui_MainWindow(QtCore.QObject):
    appliances_added = QtCore.pyqtSignal(str, dict)

    def setupUi(self, MainWindow, room_name, room_type, appliances= {}):
        if appliances == {}:
            self.appliances = dict()
        else:
            self.appliances = appliances


        self.room_name = room_name
        self.room_type = room_type
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(457, 558)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_multiple_add = QtWidgets.QToolButton(self.centralwidget)
        self.btn_multiple_add.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_multiple_add.setIcon(icon)
        self.btn_multiple_add.setIconSize(QtCore.QSize(20, 20))
        self.btn_multiple_add.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.btn_multiple_add.setAutoRaise(True)
        self.btn_multiple_add.setObjectName("btn_multiple_add")
        self.gridLayout.addWidget(self.btn_multiple_add, 3, 1, 1, 1)
        self.btn_aa_add_appliance = QtWidgets.QToolButton(self.centralwidget)
        self.btn_aa_add_appliance.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_aa_add_appliance.setIcon(icon1)
        self.btn_aa_add_appliance.setIconSize(QtCore.QSize(20, 20))
        self.btn_aa_add_appliance.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.btn_aa_add_appliance.setAutoRaise(True)
        self.btn_aa_add_appliance.setObjectName("btn_aa_add_appliance")
        self.gridLayout.addWidget(self.btn_aa_add_appliance, 3, 0, 1, 1)
        self.btn_close_window = QtWidgets.QToolButton(self.centralwidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_close_window.setIcon(icon2)
        self.btn_close_window.setIconSize(QtCore.QSize(20, 20))
        self.btn_close_window.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.btn_close_window.setAutoRaise(True)
        self.btn_close_window.setObjectName("btn_close_window")
        self.gridLayout.addWidget(self.btn_close_window, 3, 3, 1, 1)
        self.btn_del_appliance = QtWidgets.QToolButton(self.centralwidget)
        self.btn_del_appliance.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/cancel-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_del_appliance.setIcon(icon3)
        self.btn_del_appliance.setIconSize(QtCore.QSize(20, 20))
        self.btn_del_appliance.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.btn_del_appliance.setAutoRaise(True)
        self.btn_del_appliance.setObjectName("btn_del_appliance")
        self.gridLayout.addWidget(self.btn_del_appliance, 3, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.tbl_aa_siteapp_input = QtWidgets.QTableWidget(self.centralwidget)
        self.tbl_aa_siteapp_input.setEnabled(True)
        self.tbl_aa_siteapp_input.setMinimumSize(QtCore.QSize(0, 0))
        self.tbl_aa_siteapp_input.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tbl_aa_siteapp_input.setFont(font)
        self.tbl_aa_siteapp_input.setFrameShape(QtWidgets.QFrame.Panel)
        self.tbl_aa_siteapp_input.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tbl_aa_siteapp_input.setLineWidth(1)
        self.tbl_aa_siteapp_input.setMidLineWidth(1)
        self.tbl_aa_siteapp_input.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tbl_aa_siteapp_input.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tbl_aa_siteapp_input.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tbl_aa_siteapp_input.setAlternatingRowColors(True)
        self.tbl_aa_siteapp_input.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tbl_aa_siteapp_input.setShowGrid(True)
        self.tbl_aa_siteapp_input.setColumnCount(4)
        self.tbl_aa_siteapp_input.setObjectName("tbl_aa_siteapp_input")
        self.tbl_aa_siteapp_input.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        item.setFont(font)
        self.tbl_aa_siteapp_input.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_aa_siteapp_input.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_aa_siteapp_input.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_aa_siteapp_input.setHorizontalHeaderItem(3, item)
        self.tbl_aa_siteapp_input.horizontalHeader().setVisible(True)
        self.tbl_aa_siteapp_input.horizontalHeader().setCascadingSectionResizes(False)
        self.tbl_aa_siteapp_input.horizontalHeader().setDefaultSectionSize(100)
        self.tbl_aa_siteapp_input.horizontalHeader().setMinimumSectionSize(38)
        self.tbl_aa_siteapp_input.horizontalHeader().setStretchLastSection(True)
        self.tbl_aa_siteapp_input.verticalHeader().setVisible(False)
        self.tbl_aa_siteapp_input.verticalHeader().setStretchLastSection(False)
        self.gridLayout.addWidget(self.tbl_aa_siteapp_input, 2, 0, 1, 4)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_multiple_add.setText(_translate("MainWindow", "Add From Database"))
        self.btn_aa_add_appliance.setText(_translate("MainWindow", "Add New Appliance"))
        self.btn_close_window.setText(_translate("MainWindow", "Save and Close"))
        self.btn_del_appliance.setText(_translate("MainWindow", "Delete Appliance(s)"))
        self.label.setText(_translate("MainWindow", "SITE APPLIANCES"))
        self.tbl_aa_siteapp_input.setSortingEnabled(True)
        item = self.tbl_aa_siteapp_input.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Appliance"))
        item = self.tbl_aa_siteapp_input.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Power"))
        item = self.tbl_aa_siteapp_input.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Units"))
        item = self.tbl_aa_siteapp_input.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Op. Hours"))
        self.label_2.setText(_translate("MainWindow", "Please Enter Appliances for Room Here"))
        MainWindow.setWindowTitle('Add Appliances -> (' + self.room_name + ')')

        pprint(self.appliances)
        if self.appliances != {}:
            self.add_appliances(self.appliances)
        self.btn_aa_add_appliance.clicked.connect(lambda: self.add_appliance_clicked())
        self.btn_multiple_add.clicked.connect(self.multiple_add_btn_clicked)
        self.btn_del_appliance.clicked.connect(self.appliance_deleted)
        self.btn_close_window.clicked.connect(self.close_window)

    def add_appliance_clicked(self):
        try:
            self.w = QtWidgets.QMainWindow(self.centralwidget)
            self.w.setWindowModality(QtCore.Qt.ApplicationModal)
            self.p = add_appliance.Ui_MainWindow()
            self.p.setupUi(self.w)
            self.p.appliance_added.connect(self.add_appliance)
            self.w.show()
        except Exception as e:
            print('Add Appliance Button Click Error -->>', type(e), str(e))

    def multiple_add_btn_clicked(self):
        try:
            self.ws = QtWidgets.QMainWindow(self.centralwidget)
            self.ws.setWindowModality(QtCore.Qt.ApplicationModal)
            self.ps = multiple_app_select.Ui_MainWindow()
            self.ps.setupUi(self.ws)
            self.ps.add_appliances_signal.connect(self.add_appliances)
            self.ps.close_window_signal.connect(self.close_popup_window)
            self.ws.show()
        except Exception as e:
            print('Add Multiple Appliance Button Clicked Error -->>', type(e), str(e))

    def close_popup_window(self):
        self.ws.close()

    def appliance_deleted(self):
        try:
            indexes = self.tbl_aa_siteapp_input.selectionModel().selectedRows()
            for index in indexes:
                del self.appliances[self.tbl_aa_siteapp_input.item(index.row(), 0).text()]
                self.tbl_aa_siteapp_input.removeRow(index.row())
            
        except Exception as e:
            print('Delete Appliance Error -->>', type(e), str(e))

    def add_appliance(self, value):
        self.add_appliances(value)
        self.w.close()

    def tbl_input_site_data_columns(self):
        for row in range(self.tbl_aa_siteapp_input.rowCount()):
            yield self.tbl_aa_siteapp_input.item(row, 0).text()

    def check_for_repetition(self, appliance_name, appliance_dict):
        response = (False,)
        if appliance_name in self.tbl_input_site_data_columns():
            index = list(self.tbl_input_site_data_columns()).index(appliance_name)

            pow_tab = float(self.tbl_aa_siteapp_input.item(index, 1).text())

            if pow_tab == appliance_dict[appliance_name]['power_rating']:
                response = (True, index)
        return response

    def add_appliances(self, appliances):
        try:
            for appliance in appliances:
                repeat = self.check_for_repetition(appliance, appliances)
                pow_rating = appliances[appliance]['power_rating']
                units = appliances[appliance]['units']
                op_hours = appliances[appliance]['operating_hours']
                if not repeat[0]:
                    item1 = QtWidgets.QTableWidgetItem(appliance)
                    item1.setFlags(QtCore.Qt.ItemIsEnabled)
                    item1.setTextAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)

                    item2 = QtWidgets.QTableWidgetItem(str(pow_rating))
                    item2.setTextAlignment(QtCore.Qt.AlignCenter)

                    item3 = QtWidgets.QTableWidgetItem(str(units))
                    item3.setTextAlignment(QtCore.Qt.AlignCenter)

                    item4 = QtWidgets.QTableWidgetItem(str(op_hours))
                    item4.setTextAlignment(QtCore.Qt.AlignCenter)

                    n = self.tbl_aa_siteapp_input.rowCount()
                    self.tbl_aa_siteapp_input.insertRow(n)

                    self.tbl_aa_siteapp_input.setItem(n, 0, item1)
                    self.tbl_aa_siteapp_input.setItem(n, 1, item2)
                    self.tbl_aa_siteapp_input.setItem(n, 2, item3)
                    self.tbl_aa_siteapp_input.setItem(n, 3, item4)
                else:
                    units += int(self.tbl_aa_siteapp_input.item(repeat[1], 2).text())
                    item = QtWidgets.QTableWidgetItem(str(units))
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.tbl_aa_siteapp_input.setItem(repeat[1], 2, item)

                    op_hours += int(self.tbl_aa_siteapp_input.item(repeat[1], 3).text())
                    item1 = QtWidgets.QTableWidgetItem(str(op_hours))
                    item1.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.tbl_aa_siteapp_input.setItem(repeat[1], 2, item1)
                self.appliances[appliance] = {}
                self.appliances[appliance]['power_rating'] = pow_rating
                self.appliances[appliance]['units'] = units
                self.appliances[appliance]['operating_hours'] = op_hours
        except Exception as e:
            print('Add Appliance To Table Error -->>', type(e), str(e))

    def close_window(self):
        try:
            row_pos = self.tbl_aa_siteapp_input.rowCount()
            appliances = dict()

            for index in range(row_pos):
                app_name = self.tbl_aa_siteapp_input.item(index, 0).text()
                pow_rating = self.tbl_aa_siteapp_input.item(index, 1).text()
                units = self.tbl_aa_siteapp_input.item(index, 2).text()
                op_hours = self.tbl_aa_siteapp_input.item(index, 3).text()
                appliances[app_name] = {'power_rating': float(pow_rating), 'units': int(units),
                                        'operating_hours': int(op_hours)}
            self.appliances_added.emit(self.room_name, appliances)
        except Exception as e:
            print('Error Saving and Closing Window -->> ', type(e), str(e))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow, 'Test Name', 'Test Type')
    MainWindow.show()
    sys.exit(app.exec_())

