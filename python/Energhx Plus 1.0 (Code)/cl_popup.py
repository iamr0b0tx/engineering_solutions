# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\lollypop.OLOLADE\Desktop\Energy Audit APP\Code 2.0\UI\Flow\popup_office.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from math import ceil

from PyQt5 import QtCore, QtGui, QtWidgets
import resource
import json
from Libraries.CoolingLoadAnalysis import CoolingLoad

from energy_consumption_plot import EnergyConsumptionPlot, getMinimum

class Ui_MainWindow(QtCore.QObject):
    close = QtCore.pyqtSignal(str, dict)

    # focus on window?
    focus_on_main_window = True

    def closeit(self, event):
        if not self.focus_on_main_window:
            event.ignore()

    def setupUi(self, MainWindow, room_name, room_type, appliances, saved_data={}, optimizing_state=False):
        self.optimizing_state = optimizing_state
        self.saved_data = saved_data
        self.appliances = appliances
        self.room_name = room_name
        self.room_type = room_type
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(959, 654)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_previous = QtWidgets.QPushButton(self.centralwidget)
        self.btn_previous.setMinimumSize(QtCore.QSize(200, 45))
        self.btn_previous.setMaximumSize(QtCore.QSize(200, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/left-chevron.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_previous.setIcon(icon)
        self.btn_previous.setIconSize(QtCore.QSize(30, 30))
        self.btn_previous.setAutoDefault(False)
        self.btn_previous.setDefault(True)
        self.btn_previous.setFlat(False)
        self.btn_previous.setObjectName("btn_previous")
        self.gridLayout.addWidget(self.btn_previous, 2, 0, 1, 1)
        
        self.btn_next_analyze = QtWidgets.QPushButton(self.centralwidget)
        self.btn_next_analyze.setMinimumSize(QtCore.QSize(200, 45))
        self.btn_next_analyze.setMaximumSize(QtCore.QSize(200, 16777215))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/analyze.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_next_analyze.setIcon(icon1)
        self.btn_next_analyze.setIconSize(QtCore.QSize(30, 30))
        self.btn_next_analyze.setAutoDefault(False)
        self.btn_next_analyze.setDefault(True)
        self.btn_next_analyze.setFlat(False)
        self.btn_next_analyze.setObjectName("btn_next_analyze")
        self.gridLayout.addWidget(self.btn_next_analyze, 2, 1, 1, 1, QtCore.Qt.AlignRight)
        
        self.btn_optimize = QtWidgets.QPushButton(self.centralwidget)
        self.btn_optimize.setMinimumSize(QtCore.QSize(200, 45))
        self.btn_optimize.setMaximumSize(QtCore.QSize(200, 16777215))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/analyze.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_optimize.setIcon(icon1)
        self.btn_optimize.setIconSize(QtCore.QSize(30, 30))
        self.btn_optimize.setAutoDefault(False)
        self.btn_optimize.setDefault(True)
        self.btn_optimize.setFlat(False)
        self.btn_optimize.setObjectName("btn_optimize")
        self.gridLayout.addWidget(self.btn_optimize, 2, 1, 1, 1, QtCore.Qt.AlignLeft)
        
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.cooling_load_analysis_page = QtWidgets.QWidget()
        self.cooling_load_analysis_page.setObjectName("cooling_load_analysis_page")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.cooling_load_analysis_page)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.cl_input = QtWidgets.QScrollArea(self.cooling_load_analysis_page)
        self.cl_input.setWidgetResizable(True)
        self.cl_input.setObjectName("cl_input")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 865, 873))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.gridLayout_19 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.groupBox_12 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_3)
        self.groupBox_12.setMinimumSize(QtCore.QSize(280, 0))
        self.groupBox_12.setMaximumSize(QtCore.QSize(280, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_12.setFont(font)
        self.groupBox_12.setTitle("")
        self.groupBox_12.setFlat(True)
        self.groupBox_12.setObjectName("groupBox_12")
        self.gridLayout_20 = QtWidgets.QGridLayout(self.groupBox_12)
        self.gridLayout_20.setContentsMargins(-1, -1, -1, 15)
        self.gridLayout_20.setHorizontalSpacing(9)
        self.gridLayout_20.setVerticalSpacing(20)
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.label_4 = QtWidgets.QLabel(self.groupBox_12)
        self.label_4.setObjectName("label_4")
        self.gridLayout_20.addWidget(self.label_4, 2, 0, 1, 2)
        
        self.label_3 = QtWidgets.QLabel(self.groupBox_12)
        self.label_3.setObjectName("label_3")
        self.gridLayout_20.addWidget(self.label_3, 0, 0, 1, 1)
        
        self.label_3b = QtWidgets.QLabel(self.groupBox_12)
        self.label_3b.setObjectName("label_3b")
        self.gridLayout_20.addWidget(self.label_3b, 1, 0, 1, 1)
        
        self.spbox_cl_ac_unit = QtWidgets.QSpinBox(self.groupBox_12)
        self.spbox_cl_ac_unit.setMinimumSize(QtCore.QSize(0, 25))
        self.spbox_cl_ac_unit.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.spbox_cl_ac_unit.setFont(font)
        self.spbox_cl_ac_unit.setObjectName("spbox_cl_ac_unit")
        self.gridLayout_20.addWidget(self.spbox_cl_ac_unit, 0, 2, 1, 1)

        self.spbox_foot_candles = QtWidgets.QSpinBox(self.groupBox_12)
        self.spbox_foot_candles.setMinimumSize(QtCore.QSize(0, 25))
        self.spbox_foot_candles.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.spbox_foot_candles.setFont(font)
        self.spbox_foot_candles.setObjectName("spbox_foot_candles")
        self.gridLayout_20.addWidget(self.spbox_foot_candles, 1, 2, 1, 1)

        self.cmbx_cl_lightning = QtWidgets.QComboBox(self.groupBox_12)
        self.cmbx_cl_lightning.setMinimumSize(QtCore.QSize(160, 25))
        self.cmbx_cl_lightning.setMaximumSize(QtCore.QSize(180, 25))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.cmbx_cl_lightning.setFont(font)
        self.cmbx_cl_lightning.setObjectName("cmbx_cl_lightning")
        self.cmbx_cl_lightning.addItem("")
        self.cmbx_cl_lightning.addItem("")
        self.cmbx_cl_lightning.addItem("")
        self.cmbx_cl_lightning.addItem("")
        self.cmbx_cl_lightning.addItem("")
        self.gridLayout_20.addWidget(self.cmbx_cl_lightning, 2, 2, 1, 1, QtCore.Qt.AlignLeft)
        self.label_5 = QtWidgets.QLabel(self.groupBox_12)
        self.label_5.setObjectName("label_5")
        self.gridLayout_20.addWidget(self.label_5, 3, 0, 1, 1)
        self.cmbx_cl_space_type = QtWidgets.QComboBox(self.groupBox_12)
        self.cmbx_cl_space_type.setMinimumSize(QtCore.QSize(160, 25))
        self.cmbx_cl_space_type.setMaximumSize(QtCore.QSize(180, 25))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.cmbx_cl_space_type.setFont(font)
        self.cmbx_cl_space_type.setObjectName("cmbx_cl_space_type")
        self.cmbx_cl_space_type.addItem("")
        self.cmbx_cl_space_type.addItem("")
        self.cmbx_cl_space_type.addItem("")
        self.cmbx_cl_space_type.addItem("")
        self.cmbx_cl_space_type.addItem("")
        self.cmbx_cl_space_type.addItem("")
        self.gridLayout_20.addWidget(self.cmbx_cl_space_type, 3, 2, 1, 1)
        self.gridLayout_19.addWidget(self.groupBox_12, 0, 0, 2, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.groupBox_13 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_3)
        self.groupBox_13.setFlat(True)
        self.groupBox_13.setObjectName("groupBox_13")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.groupBox_13)
        self.gridLayout_9.setContentsMargins(0, -1, -1, -1)
        self.gridLayout_9.setVerticalSpacing(32)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.groupBox_16 = QtWidgets.QGroupBox(self.groupBox_13)
        self.groupBox_16.setMinimumSize(QtCore.QSize(180, 0))
        self.groupBox_16.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_16.setFont(font)
        self.groupBox_16.setFlat(True)
        self.groupBox_16.setObjectName("groupBox_16")
        self.gridLayout_25 = QtWidgets.QGridLayout(self.groupBox_16)
        self.gridLayout_25.setContentsMargins(-1, -1, 0, -1)
        self.gridLayout_25.setHorizontalSpacing(10)
        self.gridLayout_25.setVerticalSpacing(9)
        self.gridLayout_25.setObjectName("gridLayout_25")
        self.label_16 = QtWidgets.QLabel(self.groupBox_16)
        self.label_16.setObjectName("label_16")
        self.gridLayout_25.addWidget(self.label_16, 1, 0, 1, 1)
        self.txt_cl_room_area = QtWidgets.QTableWidget(self.groupBox_16)
        self.txt_cl_room_area.setMinimumSize(QtCore.QSize(150, 150))
        self.txt_cl_room_area.setMaximumSize(QtCore.QSize(180, 150))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.txt_cl_room_area.setFont(font)
        self.txt_cl_room_area.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.txt_cl_room_area.setFrameShadow(QtWidgets.QFrame.Plain)
        self.txt_cl_room_area.setObjectName("txt_cl_room_area")
        self.txt_cl_room_area.setColumnCount(2)
        self.txt_cl_room_area.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.txt_cl_room_area.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.txt_cl_room_area.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.txt_cl_room_area.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.txt_cl_room_area.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.txt_cl_room_area.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.txt_cl_room_area.setHorizontalHeaderItem(1, item)
        self.txt_cl_room_area.horizontalHeader().setDefaultSectionSize(58)
        self.txt_cl_room_area.horizontalHeader().setStretchLastSection(True)
        self.txt_cl_room_area.verticalHeader().setStretchLastSection(True)
        self.gridLayout_25.addWidget(self.txt_cl_room_area, 0, 0, 1, 3)
        self.txt_cl_roof_area = QtWidgets.QLineEdit(self.groupBox_16)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.txt_cl_roof_area.setFont(font)
        self.txt_cl_roof_area.setFrame(True)
        self.txt_cl_roof_area.setCursorPosition(0)
        self.txt_cl_roof_area.setClearButtonEnabled(True)
        self.txt_cl_roof_area.setObjectName("txt_cl_roof_area")
        self.gridLayout_25.addWidget(self.txt_cl_roof_area, 1, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.groupBox_16)
        self.label_17.setObjectName("label_17")
        self.gridLayout_25.addWidget(self.label_17, 2, 0, 1, 1)
        self.txt_cl_room_height = QtWidgets.QLineEdit(self.groupBox_16)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.txt_cl_room_height.setFont(font)
        self.txt_cl_room_height.setFrame(True)
        self.txt_cl_room_height.setCursorPosition(0)
        self.txt_cl_room_height.setClearButtonEnabled(True)
        self.txt_cl_room_height.setObjectName("txt_cl_room_height")
        self.gridLayout_25.addWidget(self.txt_cl_room_height, 2, 1, 1, 1)
        self.gridLayout_25.setColumnStretch(0, 1)
        self.gridLayout_9.addWidget(self.groupBox_16, 2, 0, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.groupBox_15 = QtWidgets.QGroupBox(self.groupBox_13)
        self.groupBox_15.setMinimumSize(QtCore.QSize(160, 0))
        self.groupBox_15.setMaximumSize(QtCore.QSize(160, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_15.setFont(font)
        self.groupBox_15.setFlat(True)
        self.groupBox_15.setObjectName("groupBox_15")
        self.gridLayout_24 = QtWidgets.QGridLayout(self.groupBox_15)
        self.gridLayout_24.setObjectName("gridLayout_24")
        self.label_10 = QtWidgets.QLabel(self.groupBox_15)
        self.label_10.setObjectName("label_10")
        self.gridLayout_24.addWidget(self.label_10, 0, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox_15)
        self.label_11.setObjectName("label_11")
        self.gridLayout_24.addWidget(self.label_11, 1, 0, 1, 1)
        self.sbox_cl_man = QtWidgets.QSpinBox(self.groupBox_15)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.sbox_cl_man.setFont(font)
        self.sbox_cl_man.setObjectName("sbox_cl_man")
        self.gridLayout_24.addWidget(self.sbox_cl_man, 0, 1, 1, 1)
        self.sbox_cl_woman = QtWidgets.QSpinBox(self.groupBox_15)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.sbox_cl_woman.setFont(font)
        self.sbox_cl_woman.setObjectName("sbox_cl_woman")
        self.gridLayout_24.addWidget(self.sbox_cl_woman, 1, 1, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox_15, 0, 0, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem, 0, 1, 1, 1)
        self.groupBox_23 = QtWidgets.QGroupBox(self.groupBox_13)
        self.groupBox_23.setMaximumSize(QtCore.QSize(220, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_23.setFont(font)
        self.groupBox_23.setFlat(True)
        self.groupBox_23.setObjectName("groupBox_23")
        self.gridLayout_34 = QtWidgets.QGridLayout(self.groupBox_23)
        self.gridLayout_34.setContentsMargins(-1, 6, 20, -1)
        self.gridLayout_34.setHorizontalSpacing(18)
        self.gridLayout_34.setObjectName("gridLayout_34")
        self.tbl_cltd = QtWidgets.QTableWidget(self.groupBox_23)
        self.tbl_cltd.setMinimumSize(QtCore.QSize(177, 150))
        self.tbl_cltd.setMaximumSize(QtCore.QSize(177, 150))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.tbl_cltd.setFont(font)
        self.tbl_cltd.setObjectName("tbl_cltd")
        self.tbl_cltd.setColumnCount(2)
        self.tbl_cltd.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_cltd.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_cltd.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_cltd.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_cltd.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_cltd.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_cltd.setHorizontalHeaderItem(1, item)
        self.tbl_cltd.horizontalHeader().setDefaultSectionSize(65)
        self.tbl_cltd.horizontalHeader().setStretchLastSection(True)
        self.tbl_cltd.verticalHeader().setStretchLastSection(True)
        self.gridLayout_34.addWidget(self.tbl_cltd, 2, 0, 1, 2)
        self.label_24 = QtWidgets.QLabel(self.groupBox_23)
        self.label_24.setObjectName("label_24")
        self.gridLayout_34.addWidget(self.label_24, 0, 0, 1, 1)
        self.txt_cltd_roof = QtWidgets.QLineEdit(self.groupBox_23)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.txt_cltd_roof.setFont(font)
        self.txt_cltd_roof.setFrame(True)
        self.txt_cltd_roof.setCursorPosition(0)
        self.txt_cltd_roof.setClearButtonEnabled(True)
        self.txt_cltd_roof.setObjectName("txt_cltd_roof")
        self.gridLayout_34.addWidget(self.txt_cltd_roof, 0, 1, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox_23, 3, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_9.addItem(spacerItem1, 2, 1, 2, 1)
        self.groupBox_14 = QtWidgets.QGroupBox(self.groupBox_13)
        self.groupBox_14.setMaximumSize(QtCore.QSize(500, 16777215))
        self.groupBox_14.setFlat(True)
        self.groupBox_14.setObjectName("groupBox_14")
        self.gridLayout_23 = QtWidgets.QGridLayout(self.groupBox_14)
        self.gridLayout_23.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_23.setSpacing(0)
        self.gridLayout_23.setObjectName("gridLayout_23")
        self.tbl_cl_appliances = QtWidgets.QTableWidget(self.groupBox_14)
        self.tbl_cl_appliances.setMinimumSize(QtCore.QSize(350, 0))
        self.tbl_cl_appliances.setMaximumSize(QtCore.QSize(600, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tbl_cl_appliances.setFont(font)
        self.tbl_cl_appliances.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbl_cl_appliances.setAlternatingRowColors(True)
        self.tbl_cl_appliances.setObjectName("tbl_cl_appliances")
        self.tbl_cl_appliances.setColumnCount(4)
        self.tbl_cl_appliances.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_cl_appliances.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_cl_appliances.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_cl_appliances.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_cl_appliances.setHorizontalHeaderItem(3, item)
        self.tbl_cl_appliances.horizontalHeader().setDefaultSectionSize(75)
        self.tbl_cl_appliances.horizontalHeader().setStretchLastSection(True)
        self.tbl_cl_appliances.verticalHeader().setVisible(False)
        self.gridLayout_23.addWidget(self.tbl_cl_appliances, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.line_5 = QtWidgets.QFrame(self.groupBox_14)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout_23.addWidget(self.line_5, 1, 0, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox_14, 0, 2, 4, 1)
        self.groupBox_21 = QtWidgets.QGroupBox(self.groupBox_13)
        self.groupBox_21.setMinimumSize(QtCore.QSize(160, 0))
        self.groupBox_21.setMaximumSize(QtCore.QSize(160, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_21.setFont(font)
        self.groupBox_21.setFlat(True)
        self.groupBox_21.setObjectName("groupBox_21")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_21)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_13 = QtWidgets.QLabel(self.groupBox_21)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_21)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox_21, 1, 0, 1, 1)
        self.gridLayout_19.addWidget(self.groupBox_13, 2, 0, 1, 4, QtCore.Qt.AlignLeft)
        self.groupBox_17 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_3)
        self.groupBox_17.setMaximumSize(QtCore.QSize(220, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_17.setFont(font)
        self.groupBox_17.setFlat(False)
        self.groupBox_17.setObjectName("groupBox_17")
        self.gridLayout_26 = QtWidgets.QGridLayout(self.groupBox_17)
        self.gridLayout_26.setContentsMargins(-1, -1, 19, -1)
        self.gridLayout_26.setHorizontalSpacing(40)
        self.gridLayout_26.setVerticalSpacing(30)
        self.gridLayout_26.setObjectName("gridLayout_26")
        self.groupBox_18 = QtWidgets.QGroupBox(self.groupBox_17)
        self.groupBox_18.setMaximumSize(QtCore.QSize(220, 16777215))
        self.groupBox_18.setFlat(True)
        self.groupBox_18.setObjectName("groupBox_18")
        self.gridLayout_27 = QtWidgets.QGridLayout(self.groupBox_18)
        self.gridLayout_27.setContentsMargins(-1, 5, -1, -1)
        self.gridLayout_27.setObjectName("gridLayout_27")
        self.tbl_cl_th_wall = QtWidgets.QTableWidget(self.groupBox_18)
        self.tbl_cl_th_wall.setMinimumSize(QtCore.QSize(177, 180))
        self.tbl_cl_th_wall.setMaximumSize(QtCore.QSize(177, 180))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.tbl_cl_th_wall.setFont(font)
        self.tbl_cl_th_wall.setObjectName("tbl_cl_th_wall")
        self.tbl_cl_th_wall.setColumnCount(2)
        self.tbl_cl_th_wall.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_cl_th_wall.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_cl_th_wall.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_cl_th_wall.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_cl_th_wall.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_cl_th_wall.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_cl_th_wall.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_cl_th_wall.setHorizontalHeaderItem(1, item)
        self.tbl_cl_th_wall.horizontalHeader().setDefaultSectionSize(45)
        self.tbl_cl_th_wall.horizontalHeader().setStretchLastSection(True)
        self.tbl_cl_th_wall.verticalHeader().setDefaultSectionSize(30)
        self.tbl_cl_th_wall.verticalHeader().setStretchLastSection(True)
        self.gridLayout_27.addWidget(self.tbl_cl_th_wall, 0, 0, 1, 2, QtCore.Qt.AlignTop)
        self.gridLayout_26.addWidget(self.groupBox_18, 1, 0, 1, 2)
        self.groupBox_19 = QtWidgets.QGroupBox(self.groupBox_17)
        self.groupBox_19.setMaximumSize(QtCore.QSize(220, 16777215))
        self.groupBox_19.setFlat(True)
        self.groupBox_19.setObjectName("groupBox_19")
        self.gridLayout_28 = QtWidgets.QGridLayout(self.groupBox_19)
        self.gridLayout_28.setContentsMargins(-1, 5, -1, -1)
        self.gridLayout_28.setObjectName("gridLayout_28")
        self.tbl_cl_th_roof = QtWidgets.QTableWidget(self.groupBox_19)
        self.tbl_cl_th_roof.setMinimumSize(QtCore.QSize(177, 150))
        self.tbl_cl_th_roof.setMaximumSize(QtCore.QSize(177, 150))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.tbl_cl_th_roof.setFont(font)
        self.tbl_cl_th_roof.setObjectName("tbl_cl_th_roof")
        self.tbl_cl_th_roof.setColumnCount(2)
        self.tbl_cl_th_roof.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_cl_th_roof.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_cl_th_roof.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_cl_th_roof.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_cl_th_roof.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_cl_th_roof.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_cl_th_roof.setHorizontalHeaderItem(1, item)
        self.tbl_cl_th_roof.horizontalHeader().setDefaultSectionSize(45)
        self.tbl_cl_th_roof.horizontalHeader().setStretchLastSection(True)
        self.tbl_cl_th_roof.verticalHeader().setDefaultSectionSize(30)
        self.tbl_cl_th_roof.verticalHeader().setStretchLastSection(True)
        self.gridLayout_28.addWidget(self.tbl_cl_th_roof, 0, 0, 1, 2, QtCore.Qt.AlignTop)
        self.gridLayout_26.addWidget(self.groupBox_19, 2, 0, 1, 2)
        self.groupBox_20 = QtWidgets.QGroupBox(self.groupBox_17)
        self.groupBox_20.setMaximumSize(QtCore.QSize(220, 16777215))
        self.groupBox_20.setTitle("")
        self.groupBox_20.setFlat(True)
        self.groupBox_20.setObjectName("groupBox_20")
        self.gridLayout_29 = QtWidgets.QGridLayout(self.groupBox_20)
        self.gridLayout_29.setObjectName("gridLayout_29")
        self.tbl_cl_scl_sc = QtWidgets.QTableWidget(self.groupBox_20)
        self.tbl_cl_scl_sc.setMinimumSize(QtCore.QSize(177, 150))
        self.tbl_cl_scl_sc.setMaximumSize(QtCore.QSize(177, 150))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.tbl_cl_scl_sc.setFont(font)
        self.tbl_cl_scl_sc.setObjectName("tbl_cl_scl_sc")
        self.tbl_cl_scl_sc.setColumnCount(2)
        self.tbl_cl_scl_sc.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_cl_scl_sc.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_cl_scl_sc.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_cl_scl_sc.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_cl_scl_sc.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_cl_scl_sc.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_cl_scl_sc.setHorizontalHeaderItem(1, item)
        self.tbl_cl_scl_sc.horizontalHeader().setDefaultSectionSize(65)
        self.tbl_cl_scl_sc.horizontalHeader().setStretchLastSection(True)
        self.tbl_cl_scl_sc.verticalHeader().setStretchLastSection(True)
        self.gridLayout_29.addWidget(self.tbl_cl_scl_sc, 0, 0, 1, 2)
        self.gridLayout_26.addWidget(self.groupBox_20, 3, 0, 1, 2, QtCore.Qt.AlignBottom)
        self.txt_cl_th_glass = QtWidgets.QLineEdit(self.groupBox_17)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.txt_cl_th_glass.setFont(font)
        self.txt_cl_th_glass.setObjectName("txt_cl_th_glass")
        self.gridLayout_26.addWidget(self.txt_cl_th_glass, 0, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox_17)
        self.label_12.setObjectName("label_12")
        self.gridLayout_26.addWidget(self.label_12, 0, 0, 1, 1)
        self.gridLayout_19.addWidget(self.groupBox_17, 0, 6, 3, 1, QtCore.Qt.AlignLeft)
        self.groupBox_22 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_3)
        self.groupBox_22.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_22.setFont(font)
        self.groupBox_22.setFlat(True)
        self.groupBox_22.setObjectName("groupBox_22")
        self.gridLayout_31 = QtWidgets.QGridLayout(self.groupBox_22)
        self.gridLayout_31.setContentsMargins(-1, 2, -1, -1)
        self.gridLayout_31.setObjectName("gridLayout_31")
        self.tbl_cl_weather = QtWidgets.QTableWidget(self.groupBox_22)
        self.tbl_cl_weather.setMinimumSize(QtCore.QSize(175, 85))
        self.tbl_cl_weather.setMaximumSize(QtCore.QSize(175, 85))
        self.tbl_cl_weather.setObjectName("tbl_cl_weather")
        self.tbl_cl_weather.setColumnCount(2)
        self.tbl_cl_weather.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_cl_weather.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_cl_weather.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_cl_weather.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_cl_weather.setHorizontalHeaderItem(1, item)
        self.tbl_cl_weather.horizontalHeader().setDefaultSectionSize(58)
        self.tbl_cl_weather.horizontalHeader().setStretchLastSection(True)
        self.tbl_cl_weather.verticalHeader().setStretchLastSection(True)
        self.gridLayout_31.addWidget(self.tbl_cl_weather, 3, 1, 1, 1)
        self.gridLayout_19.addWidget(self.groupBox_22, 0, 2, 1, 1, QtCore.Qt.AlignTop)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_19.addItem(spacerItem2, 0, 1, 1, 1)
        self.cl_input.setWidget(self.scrollAreaWidgetContents_3)
        self.gridLayout_3.addWidget(self.cl_input, 0, 0, 1, 2)
        self.cmd_load_data_default = QtWidgets.QCommandLinkButton(self.cooling_load_analysis_page)
        self.cmd_load_data_default.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setUnderline(True)
        self.cmd_load_data_default.setFont(font)
        self.cmd_load_data_default.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/cloud-computing.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cmd_load_data_default.setIcon(icon2)
        self.cmd_load_data_default.setObjectName("cmd_load_data_default")
        self.gridLayout_3.addWidget(self.cmd_load_data_default, 1, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.cmd_save_data_default = QtWidgets.QCommandLinkButton(self.cooling_load_analysis_page)
        self.cmd_save_data_default.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setUnderline(True)
        self.cmd_save_data_default.setFont(font)
        self.cmd_save_data_default.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/save-outlined-diskette.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cmd_save_data_default.setIcon(icon3)
        self.cmd_save_data_default.setObjectName("cmd_save_data_default")
        self.gridLayout_3.addWidget(self.cmd_save_data_default, 1, 1, 1, 1, QtCore.Qt.AlignRight)
        self.stackedWidget.addWidget(self.cooling_load_analysis_page)
        self.cooling_load_analysis_result_page = QtWidgets.QWidget()
        self.cooling_load_analysis_result_page.setObjectName("cooling_load_analysis_result_page")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.cooling_load_analysis_result_page)
        self.gridLayout_6.setObjectName("gridLayout_6")
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout_6.addItem(spacerItem3, 2, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.cooling_load_analysis_result_page)
        self.frame_2.setMinimumSize(QtCore.QSize(370, 0))
        self.frame_2.setMaximumSize(QtCore.QSize(370, 16777215))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_39 = QtWidgets.QLabel(self.frame_2)
        self.label_39.setMaximumSize(QtCore.QSize(30, 30))
        self.label_39.setText("")
        self.label_39.setPixmap(QtGui.QPixmap(":/icons/icons/air-conditioner.png"))
        self.label_39.setScaledContents(True)
        self.label_39.setObjectName("label_39")
        self.gridLayout_5.addWidget(self.label_39, 0, 0, 2, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignBottom)
        self.label_40 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_40.setFont(font)
        self.label_40.setObjectName("label_40")
        self.gridLayout_5.addWidget(self.label_40, 1, 1, 1, 2, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_cl_ac_power_required = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(24)
        self.lbl_cl_ac_power_required.setFont(font)
        self.lbl_cl_ac_power_required.setObjectName("lbl_cl_ac_power_required")
        self.gridLayout_5.addWidget(self.lbl_cl_ac_power_required, 2, 1, 1, 2, QtCore.Qt.AlignHCenter)
        self.gridLayout_6.addWidget(self.frame_2, 1, 0, 1, 2)
        self.frame = QtWidgets.QFrame(self.cooling_load_analysis_result_page)
        self.frame.setMinimumSize(QtCore.QSize(370, 0))
        self.frame.setMaximumSize(QtCore.QSize(370, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.lbl_cl_total_cardinal_heat = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(24)
        self.lbl_cl_total_cardinal_heat.setFont(font)
        self.lbl_cl_total_cardinal_heat.setObjectName("lbl_cl_total_cardinal_heat")
        self.gridLayout_4.addWidget(self.lbl_cl_total_cardinal_heat, 1, 1, 1, 1, QtCore.Qt.AlignLeft)
        self.label_29 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.gridLayout_4.addWidget(self.label_29, 0, 1, 1, 1, QtCore.Qt.AlignLeft)
        self.label_26 = QtWidgets.QLabel(self.frame)
        self.label_26.setMinimumSize(QtCore.QSize(30, 30))
        self.label_26.setMaximumSize(QtCore.QSize(30, 30))
        self.label_26.setText("")
        self.label_26.setPixmap(QtGui.QPixmap(":/icons/icons/sun (1).png"))
        self.label_26.setScaledContents(True)
        self.label_26.setObjectName("label_26")
        self.gridLayout_4.addWidget(self.label_26, 0, 2, 1, 1)
        self.gridLayout_6.addWidget(self.frame, 1, 3, 1, 1)
        self.frame_5 = QtWidgets.QFrame(self.cooling_load_analysis_result_page)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_44 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_44.setFont(font)
        self.label_44.setObjectName("label_44")
        self.gridLayout_8.addWidget(self.label_44, 0, 0, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignBottom)
        self.lbl_cl_cop = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_cl_cop.setFont(font)
        self.lbl_cl_cop.setObjectName("lbl_cl_cop")
        self.gridLayout_8.addWidget(self.lbl_cl_cop, 1, 0, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.gridLayout_6.addWidget(self.frame_5, 3, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.cooling_load_analysis_result_page)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_6.addWidget(self.label_2, 5, 0, 1, 4, QtCore.Qt.AlignHCenter)
        self.lbl_cl_rating = QtWidgets.QLabel(self.cooling_load_analysis_result_page)
        self.lbl_cl_rating.setMaximumSize(QtCore.QSize(180, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lbl_cl_rating.setFont(font)
        self.lbl_cl_rating.setText("")
        self.lbl_cl_rating.setPixmap(QtGui.QPixmap(":/icons/icons/five star.png"))
        self.lbl_cl_rating.setScaledContents(True)
        self.lbl_cl_rating.setObjectName("lbl_cl_rating")
        self.gridLayout_6.addWidget(self.lbl_cl_rating, 6, 0, 1, 4, QtCore.Qt.AlignHCenter)
        self.tbl_cl_output = QtWidgets.QTableWidget(self.cooling_load_analysis_result_page)
        self.tbl_cl_output.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tbl_cl_output.setFont(font)
        self.tbl_cl_output.setObjectName("tbl_cl_output")
        self.tbl_cl_output.setColumnCount(5)
        self.tbl_cl_output.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_cl_output.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_cl_output.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_cl_output.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_cl_output.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_cl_output.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_cl_output.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_cl_output.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_cl_output.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_cl_output.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_cl_output.setHorizontalHeaderItem(4, item)
        self.tbl_cl_output.horizontalHeader().setDefaultSectionSize(50)
        self.tbl_cl_output.horizontalHeader().setStretchLastSection(True)
        self.tbl_cl_output.verticalHeader().setDefaultSectionSize(30)
        self.tbl_cl_output.verticalHeader().setStretchLastSection(True)
        self.gridLayout_6.addWidget(self.tbl_cl_output, 0, 0, 1, 2)
        self.tbl_cl_output_2 = QtWidgets.QTableWidget(self.cooling_load_analysis_result_page)
        self.tbl_cl_output_2.setMinimumSize(QtCore.QSize(0, 0))
        self.tbl_cl_output_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tbl_cl_output_2.setFont(font)
        self.tbl_cl_output_2.setObjectName("tbl_cl_output_2")
        self.tbl_cl_output_2.setColumnCount(3)
        self.tbl_cl_output_2.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_cl_output_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_cl_output_2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_cl_output_2.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_cl_output_2.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_cl_output_2.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_cl_output_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_cl_output_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_cl_output_2.setHorizontalHeaderItem(2, item)
        self.tbl_cl_output_2.horizontalHeader().setDefaultSectionSize(100)
        self.tbl_cl_output_2.horizontalHeader().setStretchLastSection(True)
        self.tbl_cl_output_2.verticalHeader().setDefaultSectionSize(30)
        self.tbl_cl_output_2.verticalHeader().setStretchLastSection(True)
        self.gridLayout_6.addWidget(self.tbl_cl_output_2, 0, 3, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem4, 0, 2, 4, 1)
        self.frame_4 = QtWidgets.QFrame(self.cooling_load_analysis_result_page)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_42 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_42.setFont(font)
        self.label_42.setObjectName("label_42")
        self.gridLayout_7.addWidget(self.label_42, 0, 0, 1, 1, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        self.lbl_cl_eer = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_cl_eer.setFont(font)
        self.lbl_cl_eer.setObjectName("lbl_cl_eer")
        self.gridLayout_7.addWidget(self.lbl_cl_eer, 1, 0, 1, 1, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.gridLayout_6.addWidget(self.frame_4, 3, 0, 1, 2)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout_6.addItem(spacerItem5, 4, 0, 1, 1)
        self.stackedWidget.addWidget(self.cooling_load_analysis_result_page)
        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Office Details"))
        self.btn_previous.setText(_translate("MainWindow", "PREVIOUS"))
        self.btn_next_analyze.setText(_translate("MainWindow", "ANALYZE"))
        self.btn_optimize.setText(_translate("MainWindow", "Optimize"))
        self.label_4.setText(_translate("MainWindow", "Level Activity"))
        self.label_3.setText(_translate("MainWindow", "Room Area"))
        self.label_3b.setText(_translate("MainWindow", "Foot Candles"))
        self.cmbx_cl_lightning.setItemText(0, _translate("MainWindow", "Moderately active work (office)"))
        self.cmbx_cl_lightning.setItemText(1, _translate("MainWindow", "Standing, light work, or walking (store)"))
        self.cmbx_cl_lightning.setItemText(2, _translate("MainWindow", "Light bench work (factory)"))
        self.cmbx_cl_lightning.setItemText(3, _translate("MainWindow", "Heavy work (factory)"))
        self.cmbx_cl_lightning.setItemText(4, _translate("MainWindow", "Athletics (gymnasium)"))
        self.label_5.setText(_translate("MainWindow", "Type of Space"))
        self.cmbx_cl_space_type.setItemText(0, _translate("MainWindow", "Auditorium"))
        self.cmbx_cl_space_type.setItemText(1, _translate("MainWindow", "Class Room"))
        self.cmbx_cl_space_type.setItemText(2, _translate("MainWindow", "Locker Room"))
        self.cmbx_cl_space_type.setItemText(3, _translate("MainWindow", "Office Space"))
        self.cmbx_cl_space_type.setItemText(4, _translate("MainWindow", "Public Restroom"))
        self.cmbx_cl_space_type.setItemText(5, _translate("MainWindow", "Smoking Lounge"))
        self.groupBox_13.setTitle(_translate("MainWindow", "HEAT GAINED"))
        self.groupBox_16.setTitle(_translate("MainWindow", "Wall Area"))
        self.label_16.setText(_translate("MainWindow", "Roof Area"))
        item = self.txt_cl_room_area.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "North"))
        item = self.txt_cl_room_area.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "East"))
        item = self.txt_cl_room_area.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "South"))
        item = self.txt_cl_room_area.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "West"))
        item = self.txt_cl_room_area.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Walls"))
        item = self.txt_cl_room_area.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Windows"))
        self.label_17.setText(_translate("MainWindow", "Room Height"))
        self.groupBox_15.setTitle(_translate("MainWindow", "People"))
        self.label_10.setText(_translate("MainWindow", "Man"))
        self.label_11.setText(_translate("MainWindow", "Woman"))
        self.groupBox_23.setTitle(_translate("MainWindow", "CLTD"))
        item = self.tbl_cltd.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "North"))
        item = self.tbl_cltd.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "East"))
        item = self.tbl_cltd.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "South"))
        item = self.tbl_cltd.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "West"))
        item = self.tbl_cltd.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Walls"))
        item = self.tbl_cltd.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Windows"))
        self.label_24.setText(_translate("MainWindow", "Roof"))
        self.groupBox_14.setTitle(_translate("MainWindow", "APPLIANCES (To Add new appliance, repeat Appliance Audit)"))
        item = self.tbl_cl_appliances.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Appliance"))
        item = self.tbl_cl_appliances.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Power"))
        item = self.tbl_cl_appliances.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Area"))
        item = self.tbl_cl_appliances.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Op. Hours"))
        self.groupBox_21.setTitle(_translate("MainWindow", "Infiltration"))
        self.label_13.setText(_translate("MainWindow", "Airflow Rate"))
        self.groupBox_17.setTitle(_translate("MainWindow", "Constants"))
        self.groupBox_18.setTitle(_translate("MainWindow", "Th_Wall"))
        item = self.tbl_cl_th_wall.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Concrete"))
        item = self.tbl_cl_th_wall.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Plaster In"))
        item = self.tbl_cl_th_wall.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Plaster Out"))
        item = self.tbl_cl_th_wall.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "Outside Film"))
        item = self.tbl_cl_th_wall.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "Inside Film"))
        item = self.tbl_cl_th_wall.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Len"))
        item = self.tbl_cl_th_wall.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Cond."))
        self.groupBox_19.setTitle(_translate("MainWindow", "Th_Roof"))
        item = self.tbl_cl_th_roof.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Concrete"))
        item = self.tbl_cl_th_roof.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Plaster"))
        item = self.tbl_cl_th_roof.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Outside Film"))
        item = self.tbl_cl_th_roof.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "Inside Film"))
        item = self.tbl_cl_th_roof.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Len"))
        item = self.tbl_cl_th_roof.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Cond."))
        item = self.tbl_cl_scl_sc.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "North"))
        item = self.tbl_cl_scl_sc.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "East"))
        item = self.tbl_cl_scl_sc.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "South"))
        item = self.tbl_cl_scl_sc.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "West"))
        item = self.tbl_cl_scl_sc.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "SCL"))
        item = self.tbl_cl_scl_sc.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "SC"))
        self.label_12.setText(_translate("MainWindow", "Th_Glass"))
        self.groupBox_22.setTitle(_translate("MainWindow", "Weather"))
        item = self.tbl_cl_weather.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Indoor"))
        item = self.tbl_cl_weather.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Outdoor"))
        item = self.tbl_cl_weather.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Humidity"))
        item = self.tbl_cl_weather.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Dry Bulb"))
        self.cmd_load_data_default.setText(_translate("MainWindow", "Load default data"))
        self.cmd_save_data_default.setText(_translate("MainWindow", "Save data as default"))
        self.label_40.setText(_translate("MainWindow", " COOLING CAPACITY"))
        self.lbl_cl_ac_power_required.setText(_translate("MainWindow", "200 btu/hr"))
        self.lbl_cl_total_cardinal_heat.setText(_translate("MainWindow", "78 Joules"))
        self.label_29.setText(_translate("MainWindow", "CAL. COOLING LOAD"))
        self.label_44.setText(_translate("MainWindow", "Coefficient of Performance"))
        self.lbl_cl_cop.setText(_translate("MainWindow", "0.4"))
        self.label_2.setText(_translate("MainWindow", "AC Rating"))
        item = self.tbl_cl_output.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Glass Radiation"))
        item = self.tbl_cl_output.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Glass Conduction"))
        item = self.tbl_cl_output.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Wall Conduction"))
        item = self.tbl_cl_output.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "Roof Conduction"))
        item = self.tbl_cl_output.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "TOTAL"))
        item = self.tbl_cl_output.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "North"))
        item = self.tbl_cl_output.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "East"))
        item = self.tbl_cl_output.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "South"))
        item = self.tbl_cl_output.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "West"))
        item = self.tbl_cl_output.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "TOTAL"))
        item = self.tbl_cl_output_2.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "People"))
        item = self.tbl_cl_output_2.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Equipment"))
        item = self.tbl_cl_output_2.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Infiltration"))
        item = self.tbl_cl_output_2.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "Ventilation"))
        item = self.tbl_cl_output_2.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "TOTAL"))
        item = self.tbl_cl_output_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Sensible Heat"))
        item = self.tbl_cl_output_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Latent Heat"))
        item = self.tbl_cl_output_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "TOTAL"))
        self.label_42.setText(_translate("MainWindow", "Energy Efficiency Ratio"))
        self.lbl_cl_eer.setText(_translate("MainWindow", "0.4"))

        if self.saved_data != {}:
            self.load_default_data(self.saved_data)
        self.btn_previous.setVisible(False)

        self.load_appliances_table(self.appliances)

        self.btn_next_analyze.clicked.connect(self.next_analyze)
        self.btn_optimize.clicked.connect(self.optimize)
        self.btn_optimize.setVisible(self.optimizing_state)

        self.btn_previous.clicked.connect(self.prev_page)
        self.cmd_load_data_default.clicked.connect(lambda: self.load_default_data())
        self.cmd_save_data_default.clicked.connect(self.save_data)

    def optimize(self):
        self.next_analyze()
        
        total_cooling_load = self.saved_data['result']['cl_tons']
        foot_candles = self.saved_data['result']['cl_tons']
        area_of_room = self.data['room_det']['room_area']
        
        print(area_of_room, foot_candles, total_cooling_load, type(total_cooling_load))

        # the focus on this or another window?
        self.focus_on_main_window = False

        # the child window
        self.mec = EnergyConsumptionPlot(self)
        
        energy, cost, light, x_light, cooling, x_cooling = getMinimum(
            area_of_room, foot_candles, total_cooling_load
        )

        # create axis
        ax = self.mec.figure.add_subplot(221)

        # clear old graph
        ax.clear()

        ax.set_title('Energy against Number of Iterations')
        ax.plot(energy)
        ax.legend(['Min Energy {:,.4f} Watt'.format(energy[-1])])

        # create axis
        ax = self.mec.figure.add_subplot(222)

        # clear old graph
        ax.clear()

        ax.plot(cost)
        ax.set_title('Cost against Number of Iterations')
        ax.legend(['Min Cost {:,.4f} Naira'.format(cost[-1])])

        # create axis
        ax = self.mec.figure.add_subplot(223)

        # clear old graph
        ax.clear()
        
        ax.plot(light)
        ax.set_title('Number of Light Types against Number of Iterations')
        ax.legend([
            'x{} {:.4f}~{}'.format(
                i+1, x_light[i], ceil(x_light[i])
            ) for i in range(light.shape[1])
        ])

        # create axis
        ax = self.mec.figure.add_subplot(224)
        ax.clear()
        
        ax.plot(cooling)
        ax.set_title('Number of Cooling Types against Number of Iterations')
        ax.legend(['x{} {:.4f}~{}'.format(
                i+1, x_cooling[i], ceil(x_cooling[i])
            ) for i in range(cooling.shape[1])
        ])

        # space the graphs
        self.mec.figure.subplots_adjust(hspace=.5)

        # refresh canvas
        self.mec.plotWidget.draw()

        # optimization report
        # self.mec.label_opt_result.setText(message)
        
        # display results
        self.mec.showMaximized()

    def analyze(self):
        try:
            self.btn_previous.setVisible(True)
            self.analyze_cooling_load()
            self.stackedWidget.setCurrentIndex(1)
            self.btn_optimize.setVisible(self.optimizing_state)

            self.btn_next_analyze.setText('Save and Close')
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(":/icons/icons/cancel-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.btn_next_analyze.setIcon(icon)

            self.btn_next_analyze.setVisible(True)

        except Exception as e:
            print('Error Analyzing -->> ', type(e), str(e))

    def next_analyze(self):
        if self.stackedWidget.currentIndex() == 0:
            self.analyze()
        else:
            self.close.emit(self.room_name, self.saved_data)

    def prev_page(self):
        try:
            self.stackedWidget.setCurrentIndex(0)
            self.btn_previous.setVisible(False)
            self.btn_next_analyze.setVisible(True)
            self.btn_next_analyze.setText('Analyze')
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(":/icons/icons/analyze.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.btn_next_analyze.setIcon(icon)
        except Exception as e:
            print('Error moving to Previous Page -->> ', type(e), str(e))

    def load_appliances_table(self, values):
        try:
            for value in values:
                item1 = QtWidgets.QTableWidgetItem(value)
                item1.setFlags(QtCore.Qt.ItemIsEnabled)
                item1.setTextAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)

                item2 = QtWidgets.QTableWidgetItem(str(values[value]['power_rating']))
                item2.setTextAlignment(QtCore.Qt.AlignCenter)

                item3 = QtWidgets.QTableWidgetItem(str(values[value]['units']))
                item3.setTextAlignment(QtCore.Qt.AlignCenter)

                item4 = QtWidgets.QTableWidgetItem(str(values[value]['operating_hours']))
                item4.setTextAlignment(QtCore.Qt.AlignCenter)

                n = self.tbl_cl_appliances.rowCount()
                self.tbl_cl_appliances.insertRow(n)

                self.tbl_cl_appliances.setItem(n, 0, item1)
                self.tbl_cl_appliances.setItem(n, 1, item2)
                self.tbl_cl_appliances.setItem(n, 2, item3)
                self.tbl_cl_appliances.setItem(n, 3, item4)
        except Exception as e:
            print('Error Loading Appliance to Table', type(e), str(e))

    def read_data(self):
        try:
            room_det = {
                "room_area": self.spbox_cl_ac_unit.value(),
                "foot_candles": self.spbox_foot_candles.value(),
                "weather": {
                    "indoor": {
                        "dry_bulb": float(self.tbl_cl_weather.item(0, 1).text()),
                        "humidity": float(self.tbl_cl_weather.item(0, 0).text())
                    },
                    "outdoor": {
                        "dry_bulb": float(self.tbl_cl_weather.item(1, 1).text()),
                        "humidity": float(self.tbl_cl_weather.item(1, 0).text())
                    }
                },
                "level_activity": self.cmbx_cl_lightning.currentText(),
                "type_space": self.cmbx_cl_space_type.currentText(),
                "heat_gained": {
                    "infiltration_rate": float(self.lineEdit.text()),
                    "height": float(self.txt_cl_room_height.text()),
                    "people": {
                        "men": self.sbox_cl_man.value(),
                        "women": self.sbox_cl_woman.value()
                    },
                    "glass": {
                        "north": float(self.txt_cl_room_area.item(0, 1).text()),
                        "east": float(self.txt_cl_room_area.item(1, 1).text()),
                        "south": float(self.txt_cl_room_area.item(2, 1).text()),
                        "west": float(self.txt_cl_room_area.item(3, 1).text())
                    },
                    "walls": {
                        "north": float(self.txt_cl_room_area.item(0, 0).text()),
                        "east": float(self.txt_cl_room_area.item(1, 0).text()),
                        "south": float(self.txt_cl_room_area.item(2, 0).text()),
                        "west": float(self.txt_cl_room_area.item(3, 0).text())
                    },
                    "roof": {
                        "floor_area": float(self.txt_cl_roof_area.text())
                    }
                }
            }

            constants = {
                "th_walls": {
                    "concrete": {
                        "length": float(self.tbl_cl_th_wall.item(0, 0).text()),
                        "conductivity": float(self.tbl_cl_th_wall.item(0, 1).text())
                    },
                    "plaster_in": {
                        "length": float(self.tbl_cl_th_wall.item(1, 0).text()),
                        "conductivity": float(self.tbl_cl_th_wall.item(1, 1).text())
                    },
                    "plaster_out": {
                        "length": float(self.tbl_cl_th_wall.item(2, 0).text()),
                        "conductivity": float(self.tbl_cl_th_wall.item(2, 1).text())
                    },
                    "outside_film": {
                        "length": float(self.tbl_cl_th_wall.item(3, 0).text()),
                        "conductivity": float(self.tbl_cl_th_wall.item(3, 1).text())
                    },
                    "inside_film": {
                        "length": float(self.tbl_cl_th_wall.item(4, 0).text()),
                        "conductivity": float(self.tbl_cl_th_wall.item(4, 1).text())
                    }
                },
                "th_roof": {
                    "concrete": {
                        "length": float(self.tbl_cl_th_roof.item(0, 0).text()),
                        "conductivity": float(self.tbl_cl_th_roof.item(0, 1).text())
                    },
                    "plaster": {
                        "length": float(self.tbl_cl_th_roof.item(1, 0).text()),
                        "conductivity": float(self.tbl_cl_th_roof.item(1, 1).text())
                    },
                    "outside_film": {
                        "length": float(self.tbl_cl_th_roof.item(2, 0).text()),
                        "conductivity": float(self.tbl_cl_th_roof.item(2, 1).text())
                    },
                    "inside_film": {
                        "length": float(self.tbl_cl_th_roof.item(3, 0).text()),
                        "conductivity": float(self.tbl_cl_th_roof.item(3, 1).text())
                    }
                },
                "th_glass": float(self.txt_cl_th_glass.text()),
                "scl": {
                    "north": float(self.tbl_cl_scl_sc.item(0, 0).text()),
                    "east": float(self.tbl_cl_scl_sc.item(1, 0).text()),
                    "south": float(self.tbl_cl_scl_sc.item(2, 0).text()),
                    "west": float(self.tbl_cl_scl_sc.item(3, 0).text())
                },
                "sc": {
                    "north": float(self.tbl_cl_scl_sc.item(0, 1).text()),
                    "east": float(self.tbl_cl_scl_sc.item(1, 1).text()),
                    "south": float(self.tbl_cl_scl_sc.item(2, 1).text()),
                    "west": float(self.tbl_cl_scl_sc.item(3, 1).text())
                },
                "cltd": {
                    "walls": {
                        "north": float(self.tbl_cltd.item(0, 0).text()),
                        "east": float(self.tbl_cltd.item(1, 0).text()),
                        "south": float(self.tbl_cltd.item(2, 0).text()),
                        "west": float(self.tbl_cltd.item(3, 0).text())
                    },
                    "glass": {
                        "north": float(self.tbl_cltd.item(0, 1).text()),
                        "east": float(self.tbl_cltd.item(1, 1).text()),
                        "south": float(self.tbl_cltd.item(2, 1).text()),
                        "west": float(self.tbl_cltd.item(3, 1).text())
                    },
                    "roof": float(self.txt_cltd_roof.text())
                }
            }

            return {'room_det': room_det, 'constants': constants, 'appliances': self.appliances}
        except Exception:
            QtWidgets.QMessageBox.critical(self.centralwidget,
                                           'Invalid Parameters',
                                           'Please ensure all data are entered in their correct format',
                                           QtWidgets.QMessageBox.Close)

    def load_default_data(self, data=None):
        try:
            if data is None:
                with open('JSON files/default_cl_data.json') as f:
                    self.data = data = json.load(f)
            self.spbox_cl_ac_unit.setValue(data['room_det']['room_area'])
            self.spbox_foot_candles.setValue(data['room_det']['foot_candles'])

            item = QtWidgets.QTableWidgetItem(str('0'))
            item.setTextAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)

            item.setText(str(data['room_det']['weather']['indoor']['dry_bulb']))
            self.tbl_cl_weather.setItem(0, 1, item.clone())

            item.setText(str(data['room_det']['weather']['indoor']['humidity']))
            self.tbl_cl_weather.setItem(0, 0, item.clone())

            item.setText(str(data['room_det']['weather']['outdoor']['dry_bulb']))
            self.tbl_cl_weather.setItem(1, 1, item.clone())

            item.setText(str(data['room_det']['weather']['outdoor']['humidity']))
            self.tbl_cl_weather.setItem(1, 0, item.clone())

            self.cmbx_cl_lightning.setCurrentText(str(data['room_det']['level_activity']))
            self.cmbx_cl_space_type.setCurrentText(str(data['room_det']['type_space']))

            self.lineEdit.setText(str(data['room_det']['heat_gained']['infiltration_rate']))
            self.txt_cl_room_height.setText(str(data['room_det']['heat_gained']['height']))

            self.sbox_cl_man.setValue(data['room_det']['heat_gained']['people']['men'])
            self.sbox_cl_woman.setValue(data['room_det']['heat_gained']['people']['women'])

            item.setText(str(data['room_det']['heat_gained']['glass']['north']))
            self.txt_cl_room_area.setItem(0, 1, item.clone())
            item.setText(str(data['room_det']['heat_gained']['glass']['east']))
            self.txt_cl_room_area.setItem(1, 1, item.clone())
            item.setText(str(data['room_det']['heat_gained']['glass']['south']))
            self.txt_cl_room_area.setItem(2, 1, item.clone())
            item.setText(str(data['room_det']['heat_gained']['glass']['west']))
            self.txt_cl_room_area.setItem(3, 1, item.clone())

            item.setText(str(data['room_det']['heat_gained']['walls']['north']))
            self.txt_cl_room_area.setItem(0, 0, item.clone())
            item.setText(str(data['room_det']['heat_gained']['walls']['east']))
            self.txt_cl_room_area.setItem(1, 0, item.clone())
            item.setText(str(data['room_det']['heat_gained']['walls']['south']))
            self.txt_cl_room_area.setItem(2, 0, item.clone())
            item.setText(str(data['room_det']['heat_gained']['walls']['west']))
            self.txt_cl_room_area.setItem(3, 0, item.clone())

            self.txt_cl_roof_area.setText(str(str(data['room_det']['heat_gained']['roof']['floor_area'])))

            item.setText(str(data['constants']['th_walls']['concrete']['length']))
            self.tbl_cl_th_wall.setItem(0, 0, item.clone())
            item.setText(str(data['constants']['th_walls']['concrete']['conductivity']))
            self.tbl_cl_th_wall.setItem(0, 1, item.clone())
            item.setText(str(data['constants']['th_walls']['outside_film']['length']))
            self.tbl_cl_th_wall.setItem(3, 0, item.clone())
            item.setText(str(data['constants']['th_walls']['outside_film']['conductivity']))
            self.tbl_cl_th_wall.setItem(3, 1, item.clone())
            item.setText(str(data['constants']['th_walls']['inside_film']['length']))
            self.tbl_cl_th_wall.setItem(4, 0, item.clone())
            item.setText(str(data['constants']['th_walls']['inside_film']['conductivity']))
            self.tbl_cl_th_wall.setItem(4, 1, item.clone())
            item.setText(str(data['constants']['th_walls']['plaster_in']['length']))
            self.tbl_cl_th_wall.setItem(1, 0, item.clone())
            item.setText(str(data['constants']['th_walls']['plaster_in']['conductivity']))
            self.tbl_cl_th_wall.setItem(1, 1, item.clone())
            item.setText(str(data['constants']['th_walls']['plaster_out']['length']))
            self.tbl_cl_th_wall.setItem(2, 0, item.clone())
            item.setText(str(data['constants']['th_walls']['plaster_out']['conductivity']))
            self.tbl_cl_th_wall.setItem(2, 1, item.clone())

            item.setText(str(data['constants']['th_roof']['concrete']['length']))
            self.tbl_cl_th_roof.setItem(0, 0, item.clone())
            item.setText(str(data['constants']['th_roof']['concrete']['conductivity']))
            self.tbl_cl_th_roof.setItem(0, 1, item.clone())
            item.setText(str(data['constants']['th_roof']['outside_film']['length']))
            self.tbl_cl_th_roof.setItem(2, 0, item.clone())
            item.setText(str(data['constants']['th_roof']['outside_film']['conductivity']))
            self.tbl_cl_th_roof.setItem(2, 1, item.clone())
            item.setText(str(data['constants']['th_roof']['inside_film']['length']))
            self.tbl_cl_th_roof.setItem(3, 0, item.clone())
            item.setText(str(data['constants']['th_roof']['inside_film']['conductivity']))
            self.tbl_cl_th_roof.setItem(3, 1, item.clone())
            item.setText(str(data['constants']['th_roof']['plaster']['length']))
            self.tbl_cl_th_roof.setItem(1, 0, item.clone())
            item.setText(str(data['constants']['th_roof']['plaster']['conductivity']))
            self.tbl_cl_th_roof.setItem(1, 1, item.clone())

            self.txt_cl_th_glass.setText(str(data['constants']['th_glass']))

            item.setText(str(data['constants']['scl']['north']))
            self.tbl_cl_scl_sc.setItem(0, 0, item.clone())
            item.setText(str(data['constants']['scl']['east']))
            self.tbl_cl_scl_sc.setItem(1, 0, item.clone())
            item.setText(str(data['constants']['scl']['south']))
            self.tbl_cl_scl_sc.setItem(2, 0, item.clone())
            item.setText(str(data['constants']['scl']['west']))
            self.tbl_cl_scl_sc.setItem(3, 0, item.clone())

            item.setText(str(data['constants']['sc']['north']))
            self.tbl_cl_scl_sc.setItem(0, 1, item.clone())
            item.setText(str(data['constants']['sc']['east']))
            self.tbl_cl_scl_sc.setItem(1, 1, item.clone())
            item.setText(str(data['constants']['sc']['south']))
            self.tbl_cl_scl_sc.setItem(2, 1, item.clone())
            item.setText(str(data['constants']['sc']['west']))
            self.tbl_cl_scl_sc.setItem(3, 1, item.clone())

            item.setText(str(data['constants']['cltd']['walls']['north']))
            self.tbl_cltd.setItem(0, 0, item.clone())
            item.setText(str(data['constants']['cltd']['walls']['east']))
            self.tbl_cltd.setItem(1, 0, item.clone())
            item.setText(str(data['constants']['cltd']['walls']['south']))
            self.tbl_cltd.setItem(2, 0, item.clone())
            item.setText(str(data['constants']['cltd']['walls']['west']))
            self.tbl_cltd.setItem(3, 0, item.clone())

            item.setText(str(data['constants']['cltd']['glass']['north']))
            self.tbl_cltd.setItem(0, 1, item.clone())
            item.setText(str(data['constants']['cltd']['glass']['east']))
            self.tbl_cltd.setItem(1, 1, item.clone())
            item.setText(str(data['constants']['cltd']['glass']['south']))
            self.tbl_cltd.setItem(2, 1, item.clone())
            item.setText(str(data['constants']['cltd']['glass']['west']))
            self.tbl_cltd.setItem(3, 1, item.clone())

            self.txt_cltd_roof.setText(str(data['constants']['cltd']['roof']))
        except Exception as e:
            print('Load Default Error -->> ', type(e), str(e))

    def save_data(self):
        try:
            data = self.read_data()
            if data is not None:
                with open('JSON files/default_cl_data.json', 'w') as f:
                    json.dump(data, f, indent=4)
            QtWidgets.QMessageBox.about(self.centralwidget, "Saved", "Data has been saved as default data. ")
        except Exception as e:
            print('Save Default Data Error -->> ', type(e), str(e))

    def analyze_cooling_load(self):
        try:
            data = self.read_data()
            self.saved_data['saved_data'] = data
            c_load = CoolingLoad(space_dict=data['room_det'], constant=data['constants'], appliance=data['appliances'])
            result = c_load.analysis()

            self.populate_cl_result_table(result)
        except Exception as e:
            print('Error working with Cooling Load Library --> ', type(e), str(e))

    def populate_cl_result_table(self, result):
        try:
            cardinal = 0
            item = QtWidgets.QTableWidgetItem(str(result['glass_radiation']['north']['cardinal_total_heat']))
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tbl_cl_output.setItem(0, 0, item.clone())
            item.setText(str(round(result['glass_radiation']['east']['cardinal_total_heat'], 3)))
            self.tbl_cl_output.setItem(0, 1, item.clone())
            item.setText(str(round(result['glass_radiation']['south']['cardinal_total_heat'], 3)))
            self.tbl_cl_output.setItem(0, 2, item.clone())
            item.setText(str(round(result['glass_radiation']['west']['cardinal_total_heat'], 3)))
            self.tbl_cl_output.setItem(0, 3, item.clone())
            item.setText(str(round(result['glass_radiation']['total'], 2)))
            self.tbl_cl_output.setItem(0, 4, item.clone())
            cardinal += result['glass_radiation']['total']

            item.setText(str(round(result['glass_conduction']['north']['cardinal_total_heat'], 2)))
            self.tbl_cl_output.setItem(1, 0, item.clone())
            item.setText(str(round(result['glass_conduction']['east']['cardinal_total_heat'], 2)))
            self.tbl_cl_output.setItem(1, 1, item.clone())
            item.setText(str(round(result['glass_conduction']['south']['cardinal_total_heat'], 2)))
            self.tbl_cl_output.setItem(1, 2, item.clone())
            item.setText(str(round(result['glass_conduction']['west']['cardinal_total_heat'], 2)))
            self.tbl_cl_output.setItem(1, 3, item.clone())
            item.setText(str(round(result['glass_conduction']['total'], 2)))
            self.tbl_cl_output.setItem(1, 4, item.clone())
            cardinal += result['glass_conduction']['total']

            item.setText(str(round(result['walls_conduction']['north']['cardinal_total_heat'], 2)))
            self.tbl_cl_output.setItem(2, 0, item.clone())
            item.setText(str(round(result['walls_conduction']['east']['cardinal_total_heat'], 2)))
            self.tbl_cl_output.setItem(2, 1, item.clone())
            item.setText(str(round(result['walls_conduction']['south']['cardinal_total_heat'], 2)))
            self.tbl_cl_output.setItem(2, 2, item.clone())
            item.setText(str(round(result['walls_conduction']['west']['cardinal_total_heat'], 2)))
            self.tbl_cl_output.setItem(2, 3, item.clone())
            item.setText(str(round(result['walls_conduction']['total'], 2)))
            self.tbl_cl_output.setItem(2, 4, item.clone())
            cardinal += result['walls_conduction']['total']

            item.setText(str(round(result['roof_conduction']['total'], 2)))
            self.tbl_cl_output.setItem(3, 4, item.clone())
            cardinal += result['roof_conduction']['total']

            heat = 0
            item.setText(str(round(result['heat_people']['Q_sensible'], 2)))
            self.tbl_cl_output_2.setItem(0, 0, item.clone())
            item.setText(str(round(result['heat_people']['Q_latent'], 2)))
            self.tbl_cl_output_2.setItem(0, 1, item.clone())
            item.setText(str(round(result['heat_people']['total'], 2)))
            self.tbl_cl_output_2.setItem(0, 2, item.clone())
            heat += result['heat_people']['total']

            item.setText(str(round(result['heat_appliances']['total'], 2)))
            self.tbl_cl_output_2.setItem(1, 2, item.clone())
            heat += result['heat_appliances']['total']

            item.setText(str(round(result['heat_infiltration']['Q_sensible'], 2)))
            self.tbl_cl_output_2.setItem(2, 0, item.clone())
            item.setText(str(round(result['heat_infiltration']['Q_latent'], 2)))
            self.tbl_cl_output_2.setItem(2, 1, item.clone())
            item.setText(str(round(result['heat_infiltration']['total'], 2)))
            self.tbl_cl_output_2.setItem(2, 2, item.clone())
            heat += result['heat_infiltration']['total']

            item.setText(str(round(result['heat_ventilation']['Q_sensible'], 2)))
            self.tbl_cl_output_2.setItem(3, 0, item.clone())
            item.setText(str(round(result['heat_ventilation']['Q_latent'], 2)))
            self.tbl_cl_output_2.setItem(3, 1, item.clone())
            item.setText(str(round(result['heat_ventilation']['total'], 2)))
            self.tbl_cl_output_2.setItem(3, 2, item.clone())
            heat += result['heat_ventilation']['total']

            for column in range(5):
                sum_cardinal = 0
                for row in range(self.tbl_cl_output.rowCount() - 1):
                    value = self.tbl_cl_output.item(row, column)

                    if value is not None:
                        sum_cardinal += float(value.text())
                item.setText(str(round(sum_cardinal, 2)))
                self.tbl_cl_output.setItem(4, column, item.clone())

            for column in range(3):
                sum_heat = 0
                for row in range(self.tbl_cl_output_2.rowCount() - 1):
                    value = self.tbl_cl_output_2.item(row, column)

                    if value is not None:
                        sum_heat += float(value.text())
                item.setText(str(round(sum_heat, 2)))
                self.tbl_cl_output_2.setItem(4, column, item.clone())

            cl_btu = ((cardinal + heat) / 1000) * 3412.142
            eer = cl_btu / (3510)
            cop = eer / 3.014
            cl_tons = cl_btu / 12000
            rating = 0
            self.lbl_cl_total_cardinal_heat.setText(str(round(cl_btu, 2)) + ' btu/hr')
            self.lbl_cl_ac_power_required.setText(str(round(cl_tons)) + ' tons')
            self.lbl_cl_eer.setText(str(round(eer, 3)))
            self.lbl_cl_cop.setText(str(round(cop, 3)))

            print('Round')
            print(cardinal + heat)
            print(eer)

            eer_temp = str(round(eer, 1))
            if int(eer_temp[-1]) != 5:
                eer = round(eer, 1)

            if 2.8 <= eer <= 3.10:
                rating = 1
            elif 3.15 <= eer <= 3.40:
                rating = 2
            elif 3.45 <= eer <= 3.70:
                rating = 3
            elif 3.75 <= eer <= 4.0:
                rating = 4
            elif eer >= 4.0:
                rating = 5
            else:
                rating = 'None'

            star = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
            self.lbl_cl_rating.setPixmap(QtGui.QPixmap(":/icons/icons/" + star[rating] + " star.png"))

            self.saved_data['result'] = {'cl_btu': cl_btu, 'cl_tons': cl_tons, 'eer': eer, 'cop': cop, 'rating': rating}
        except Exception as e:
            print('Error Printing out Result -->> ', type(e), str(e))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    with open('JSON files/appliances.json') as f:
        appliances = json.load(f)
    ui.setupUi(MainWindow, 'Test Name', 'Test Type', appliances)
    MainWindow.show()
    sys.exit(app.exec_())

