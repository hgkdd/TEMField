# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow2.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFormLayout, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTabWidget,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1008, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.Main_tabWidget = QTabWidget(self.centralwidget)
        self.Main_tabWidget.setObjectName(u"Main_tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_4 = QGridLayout(self.tab)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.groupBox_2 = QGroupBox(self.tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_3 = QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_5)

        self.lineEdit_5 = QLineEdit(self.groupBox_2)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.lineEdit_5)

        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_6)

        self.lineEdit_6 = QLineEdit(self.groupBox_2)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.lineEdit_6)


        self.gridLayout_3.addLayout(self.formLayout_2, 0, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.groupBox_2)

        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_6 = QGridLayout(self.groupBox)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.lineEdit_2 = QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_2)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.lineEdit_3 = QLineEdit(self.groupBox)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_3)

        self.checkBox = QCheckBox(self.groupBox)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setChecked(True)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.checkBox)

        self.plainTextEdit = QPlainTextEdit(self.groupBox)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setAcceptDrops(False)
        self.plainTextEdit.setReadOnly(True)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.plainTextEdit)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_4)

        self.lineEdit_4 = QLineEdit(self.groupBox)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setReadOnly(True)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.lineEdit_4)


        self.gridLayout_6.addLayout(self.formLayout, 0, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.groupBox)

        self.groupBox_3 = QGroupBox(self.tab)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_5 = QGridLayout(self.groupBox_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.lineEdit_7 = QLineEdit(self.groupBox_3)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.lineEdit_7)

        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_7)

        self.lineEdit_8 = QLineEdit(self.groupBox_3)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setReadOnly(True)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.lineEdit_8)

        self.label_8 = QLabel(self.groupBox_3)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_8)


        self.gridLayout_5.addLayout(self.formLayout_3, 0, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.groupBox_3)


        self.gridLayout_4.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.Main_tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.Main_tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.Main_tabWidget.addTab(self.tab_4, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.Main_tabWidget.addTab(self.tab_3, "")

        self.gridLayout.addWidget(self.Main_tabWidget, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setCheckable(True)

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setCheckable(True)

        self.horizontalLayout.addWidget(self.pushButton_4)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)


        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.plainTextEdit_2 = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setAcceptDrops(False)
        self.plainTextEdit_2.setReadOnly(True)

        self.gridLayout.addWidget(self.plainTextEdit_2, 1, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1008, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.Main_tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Field Strength", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"CW / V/m", None))
        self.lineEdit_5.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"AM / %", None))
        self.lineEdit_6.setText(QCoreApplication.translate("MainWindow", u"80", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Frequency", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Start / MHz", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"30", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Stop / MHz", None))
        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"1000", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Step / %", None))
        self.lineEdit_3.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Log Sweep", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"# Freq.", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.lineEdit_7.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Dwell Time / s", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Test Time / s", None))
        self.Main_tabWidget.setTabText(self.Main_tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Settings", None))
        self.Main_tabWidget.setTabText(self.Main_tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Waveform", None))
        self.Main_tabWidget.setTabText(self.Main_tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Table", None))
        self.Main_tabWidget.setTabText(self.Main_tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Log", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Start Test", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"RF", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"MOD", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
    # retranslateUi

