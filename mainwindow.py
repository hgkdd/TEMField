# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QScrollArea, QSizePolicy,
    QStatusBar, QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(979, 604)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionLoad_Dot = QAction(MainWindow)
        self.actionLoad_Dot.setObjectName(u"actionLoad_Dot")
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionTest = QAction(MainWindow)
        self.actionTest.setObjectName(u"actionTest")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.MainWindow_tabWidget = QTabWidget(self.centralwidget)
        self.MainWindow_tabWidget.setObjectName(u"MainWindow_tabWidget")
        self.MainWindow_tabWidget.setGeometry(QRect(10, 0, 951, 541))
        self.EFieldWAV_tab = QWidget()
        self.EFieldWAV_tab.setObjectName(u"EFieldWAV_tab")
        self.layoutWidget = QWidget(self.EFieldWAV_tab)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 941, 493))
        self.horizontalLayout_6 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.EFieldWAV_groupBox = QGroupBox(self.layoutWidget)
        self.EFieldWAV_groupBox.setObjectName(u"EFieldWAV_groupBox")
        self.EFieldWAV_groupBox.setMinimumSize(QSize(600, 0))
        self.verticalLayout_5 = QVBoxLayout(self.EFieldWAV_groupBox)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.EFieldWAV_scrollArea = QScrollArea(self.EFieldWAV_groupBox)
        self.EFieldWAV_scrollArea.setObjectName(u"EFieldWAV_scrollArea")
        self.EFieldWAV_scrollArea.setMinimumSize(QSize(580, 0))
        self.EFieldWAV_scrollArea.setWidgetResizable(True)
        self.EFieldWAV_scrollAreaWidgetContents = QWidget()
        self.EFieldWAV_scrollAreaWidgetContents.setObjectName(u"EFieldWAV_scrollAreaWidgetContents")
        self.EFieldWAV_scrollAreaWidgetContents.setGeometry(QRect(0, 0, 578, 442))
        self.EFieldWAV_scrollArea.setWidget(self.EFieldWAV_scrollAreaWidgetContents)

        self.verticalLayout_5.addWidget(self.EFieldWAV_scrollArea)


        self.horizontalLayout_6.addWidget(self.EFieldWAV_groupBox)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.Sweep_groupBox = QGroupBox(self.layoutWidget)
        self.Sweep_groupBox.setObjectName(u"Sweep_groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.Sweep_groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.f_start_label = QLabel(self.Sweep_groupBox)
        self.f_start_label.setObjectName(u"f_start_label")

        self.horizontalLayout.addWidget(self.f_start_label)

        self.f_start_lineEdit = QLineEdit(self.Sweep_groupBox)
        self.f_start_lineEdit.setObjectName(u"f_start_lineEdit")
        self.f_start_lineEdit.setClearButtonEnabled(False)

        self.horizontalLayout.addWidget(self.f_start_lineEdit)

        self.f_start_unit = QLabel(self.Sweep_groupBox)
        self.f_start_unit.setObjectName(u"f_start_unit")

        self.horizontalLayout.addWidget(self.f_start_unit)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.f_stop_label = QLabel(self.Sweep_groupBox)
        self.f_stop_label.setObjectName(u"f_stop_label")

        self.horizontalLayout_2.addWidget(self.f_stop_label)

        self.f_stop_lineEdit = QLineEdit(self.Sweep_groupBox)
        self.f_stop_lineEdit.setObjectName(u"f_stop_lineEdit")

        self.horizontalLayout_2.addWidget(self.f_stop_lineEdit)

        self.f_stop_unit = QLabel(self.Sweep_groupBox)
        self.f_stop_unit.setObjectName(u"f_stop_unit")

        self.horizontalLayout_2.addWidget(self.f_stop_unit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.f_step_label = QLabel(self.Sweep_groupBox)
        self.f_step_label.setObjectName(u"f_step_label")

        self.horizontalLayout_3.addWidget(self.f_step_label)

        self.f_step_lineEdit = QLineEdit(self.Sweep_groupBox)
        self.f_step_lineEdit.setObjectName(u"f_step_lineEdit")

        self.horizontalLayout_3.addWidget(self.f_step_lineEdit)

        self.f_step_unit = QLabel(self.Sweep_groupBox)
        self.f_step_unit.setObjectName(u"f_step_unit")

        self.horizontalLayout_3.addWidget(self.f_step_unit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.Log_Sweep_checkBox = QCheckBox(self.Sweep_groupBox)
        self.Log_Sweep_checkBox.setObjectName(u"Log_Sweep_checkBox")
        self.Log_Sweep_checkBox.setChecked(True)

        self.verticalLayout_2.addWidget(self.Log_Sweep_checkBox)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.f_step_time_label = QLabel(self.Sweep_groupBox)
        self.f_step_time_label.setObjectName(u"f_step_time_label")

        self.horizontalLayout_5.addWidget(self.f_step_time_label)

        self.f_step_time_lineEdit = QLineEdit(self.Sweep_groupBox)
        self.f_step_time_lineEdit.setObjectName(u"f_step_time_lineEdit")

        self.horizontalLayout_5.addWidget(self.f_step_time_lineEdit)

        self.f_step_time_unit = QLabel(self.Sweep_groupBox)
        self.f_step_time_unit.setObjectName(u"f_step_time_unit")

        self.horizontalLayout_5.addWidget(self.f_step_time_unit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.Sweep_Pause_pushButton = QPushButton(self.Sweep_groupBox)
        self.Sweep_Pause_pushButton.setObjectName(u"Sweep_Pause_pushButton")
        self.Sweep_Pause_pushButton.setCheckable(True)

        self.verticalLayout_2.addWidget(self.Sweep_Pause_pushButton)


        self.verticalLayout_3.addWidget(self.Sweep_groupBox)

        self.E_groupBox = QGroupBox(self.layoutWidget)
        self.E_groupBox.setObjectName(u"E_groupBox")
        self.verticalLayout_4 = QVBoxLayout(self.E_groupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.E_Target_label = QLabel(self.E_groupBox)
        self.E_Target_label.setObjectName(u"E_Target_label")

        self.horizontalLayout_7.addWidget(self.E_Target_label)

        self.E_Target_lineEdit = QLineEdit(self.E_groupBox)
        self.E_Target_lineEdit.setObjectName(u"E_Target_lineEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.E_Target_lineEdit.sizePolicy().hasHeightForWidth())
        self.E_Target_lineEdit.setSizePolicy(sizePolicy)
        self.E_Target_lineEdit.setMaximumSize(QSize(16777215, 16777215))
        self.E_Target_lineEdit.setClearButtonEnabled(False)

        self.horizontalLayout_7.addWidget(self.E_Target_lineEdit)

        self.E_Target_unit = QLabel(self.E_groupBox)
        self.E_Target_unit.setObjectName(u"E_Target_unit")

        self.horizontalLayout_7.addWidget(self.E_Target_unit)


        self.verticalLayout_4.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.E_AM_label = QLabel(self.E_groupBox)
        self.E_AM_label.setObjectName(u"E_AM_label")

        self.horizontalLayout_8.addWidget(self.E_AM_label)

        self.E_AM_lineEdit = QLineEdit(self.E_groupBox)
        self.E_AM_lineEdit.setObjectName(u"E_AM_lineEdit")
        sizePolicy.setHeightForWidth(self.E_AM_lineEdit.sizePolicy().hasHeightForWidth())
        self.E_AM_lineEdit.setSizePolicy(sizePolicy)
        self.E_AM_lineEdit.setMaximumSize(QSize(16777215, 16777215))
        self.E_AM_lineEdit.setClearButtonEnabled(False)

        self.horizontalLayout_8.addWidget(self.E_AM_lineEdit)

        self.E_AM_unit = QLabel(self.E_groupBox)
        self.E_AM_unit.setObjectName(u"E_AM_unit")

        self.horizontalLayout_8.addWidget(self.E_AM_unit)


        self.verticalLayout_4.addLayout(self.horizontalLayout_8)


        self.verticalLayout_3.addWidget(self.E_groupBox)

        self.SG_groupBox = QGroupBox(self.layoutWidget)
        self.SG_groupBox.setObjectName(u"SG_groupBox")
        self.verticalLayout = QVBoxLayout(self.SG_groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.RF_pushButton = QPushButton(self.SG_groupBox)
        self.RF_pushButton.setObjectName(u"RF_pushButton")
        self.RF_pushButton.setCheckable(True)

        self.verticalLayout.addWidget(self.RF_pushButton)

        self.MOD_pushButton = QPushButton(self.SG_groupBox)
        self.MOD_pushButton.setObjectName(u"MOD_pushButton")
        self.MOD_pushButton.setCheckable(True)

        self.verticalLayout.addWidget(self.MOD_pushButton)


        self.verticalLayout_3.addWidget(self.SG_groupBox)

        self.Quit_pushButton = QPushButton(self.layoutWidget)
        self.Quit_pushButton.setObjectName(u"Quit_pushButton")

        self.verticalLayout_3.addWidget(self.Quit_pushButton)


        self.horizontalLayout_6.addLayout(self.verticalLayout_3)

        self.MainWindow_tabWidget.addTab(self.EFieldWAV_tab, "")
        self.Table_tab = QWidget()
        self.Table_tab.setObjectName(u"Table_tab")
        self.MainWindow_tabWidget.addTab(self.Table_tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 979, 37))
        self.menu_File = QMenu(self.menubar)
        self.menu_File.setObjectName(u"menu_File")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
#if QT_CONFIG(shortcut)
        self.f_start_label.setBuddy(self.f_start_lineEdit)
        self.f_stop_label.setBuddy(self.f_stop_lineEdit)
        self.f_step_label.setBuddy(self.f_step_lineEdit)
        self.f_step_time_label.setBuddy(self.f_step_time_lineEdit)
        self.E_Target_label.setBuddy(self.E_Target_lineEdit)
        self.E_AM_label.setBuddy(self.E_AM_lineEdit)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.f_start_lineEdit, self.f_stop_lineEdit)
        QWidget.setTabOrder(self.f_stop_lineEdit, self.f_step_lineEdit)
        QWidget.setTabOrder(self.f_step_lineEdit, self.f_step_time_lineEdit)
        QWidget.setTabOrder(self.f_step_time_lineEdit, self.E_Target_lineEdit)
        QWidget.setTabOrder(self.E_Target_lineEdit, self.E_AM_lineEdit)
        QWidget.setTabOrder(self.E_AM_lineEdit, self.RF_pushButton)
        QWidget.setTabOrder(self.RF_pushButton, self.MOD_pushButton)
        QWidget.setTabOrder(self.MOD_pushButton, self.Sweep_Pause_pushButton)
        QWidget.setTabOrder(self.Sweep_Pause_pushButton, self.EFieldWAV_scrollArea)
        QWidget.setTabOrder(self.EFieldWAV_scrollArea, self.Quit_pushButton)

        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menu_File.addAction(self.actionAbout)
        self.menu_File.addAction(self.actionLoad_Dot)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionTest)

        self.retranslateUi(MainWindow)
        self.actionQuit.triggered.connect(MainWindow.close)
        self.Quit_pushButton.clicked.connect(self.actionQuit.trigger)

        self.MainWindow_tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"TEM Field", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionLoad_Dot.setText(QCoreApplication.translate("MainWindow", u"Load Dot ...", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionTest.setText(QCoreApplication.translate("MainWindow", u"Test", None))
        self.EFieldWAV_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"E-Field Waveform", None))
        self.Sweep_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Sweep Control", None))
        self.f_start_label.setText(QCoreApplication.translate("MainWindow", u"Start:", None))
        self.f_start_lineEdit.setPlaceholderText("")
        self.f_start_unit.setText(QCoreApplication.translate("MainWindow", u"MHz", None))
        self.f_stop_label.setText(QCoreApplication.translate("MainWindow", u"Stop:", None))
        self.f_stop_unit.setText(QCoreApplication.translate("MainWindow", u"MHz", None))
        self.f_step_label.setText(QCoreApplication.translate("MainWindow", u"Step:", None))
        self.f_step_unit.setText(QCoreApplication.translate("MainWindow", u"MHz / %", None))
        self.Log_Sweep_checkBox.setText(QCoreApplication.translate("MainWindow", u"Log Sweep", None))
        self.f_step_time_label.setText(QCoreApplication.translate("MainWindow", u"Time:", None))
        self.f_step_time_unit.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.Sweep_Pause_pushButton.setText(QCoreApplication.translate("MainWindow", u"Pause Sweep", None))
        self.E_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"E-Field", None))
        self.E_Target_label.setText(QCoreApplication.translate("MainWindow", u"E:", None))
        self.E_Target_lineEdit.setPlaceholderText("")
        self.E_Target_unit.setText(QCoreApplication.translate("MainWindow", u"V/m", None))
        self.E_AM_label.setText(QCoreApplication.translate("MainWindow", u"AM:", None))
        self.E_AM_lineEdit.setPlaceholderText("")
        self.E_AM_unit.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.SG_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Signal Generator", None))
        self.RF_pushButton.setText(QCoreApplication.translate("MainWindow", u"RF", None))
        self.MOD_pushButton.setText(QCoreApplication.translate("MainWindow", u"MOD", None))
        self.Quit_pushButton.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.MainWindow_tabWidget.setTabText(self.MainWindow_tabWidget.indexOf(self.EFieldWAV_tab), QCoreApplication.translate("MainWindow", u"Waveform", None))
        self.MainWindow_tabWidget.setTabText(self.MainWindow_tabWidget.indexOf(self.Table_tab), QCoreApplication.translate("MainWindow", u"Table", None))
        self.menu_File.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

