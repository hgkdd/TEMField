# This Python file uses the following encoding: utf-8
import os.path
import sys
import time
import io
import datetime
import numpy as np

from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.figure import Figure

from PySide6.QtCore import Qt, QLocale, QSettings
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from PySide6.QtGui import QIntValidator

import mpy.device.prb_lumiloop_lsporobe as lumiprb
from mpy.tools.spacing import logspace, linspace
from TestSusceptibility import TestSusceptibiliy

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic mainwindow.ui -o mainwindow.py
from mainwindow2 import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, settings, parent=None):
        super().__init__(parent)
        self.settings = settings
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.disable_update = True
        self._read_setup()
        self.disable_update = False

        # register message box for quit action
        self.ui.quit_MsgBox = QMessageBox()
        self.ui.quit_MsgBox.setText("Application Exit.")
        self.ui.quit_MsgBox.setInformativeText("Do you want to exit the application?")
        self.ui.quit_MsgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        self.ui.quit_MsgBox.setDefaultButton(QMessageBox.Cancel)
        self.ui.actionQuit.triggered.connect(MainWindow.close)
        # File Dialog
        self.ui.actionLoad_Graph.triggered.connect(self.load_graph)

        # cw field strength
        self.ui.cw_doubleSpinBox.valueChanged.connect(self.cw_doubleSpinBox_changed)
        # am percentage
        self.ui.am_spinBox.valueChanged.connect(self.am_spinBox_changed)
        # about
        self.ui.actionAbout.triggered.connect(self.about_triggered)
        # node names
        self.ui.node_names_tableWidget.cellChanged.connect(self.node_names_table_cellChanged)
        # update the other fields
        self.update()
        self.ui.start_pause_pushButton.setDisabled(True)
        self.node_names_table_cellChanged()
        self.ui.start_pause_pushButton.clicked.connect(self.start_pause_pushButton_clicked)


        self.meas = TestSusceptibiliy()
        self.ui.start_pause_pushButton.setDisabled(False)

    def start_pause_pushButton_clicked(self):
        err = self.meas.Init(dwell_time=self.dwell_time,
             e_target=self.cw,
            names=self.names,
             dotfile=self.dotfile,
             SearchPath=self.searchpath)

    def node_names_table_cellChanged(self):
        names = {'sg': None, 'a1': None, 'a2': None, 'tem': None, 'fp': None}
        for row,key in enumerate(['sg', 'a1', 'a2', 'tem', 'fp']):
            names[key] = self.ui.node_names_tableWidget.item(row, 1).text()
        self.names = names

    def load_graph(self):
        fullfile = QFileDialog.getOpenFileName(self,
                                                   "Open Graph File",
                                                   ".",
                                                   "dot files (*.dot)")[0]
        dotpath, self.dotfile = os.path.split(fullfile)
        self.searchpath = [dotpath,]
        self.ui.graph_file_lineEdit.setText(self.dotfile)
        self.ui.search_path_lineEdit.setText(str(self.searchpath))
        # print(self.dotfile, self.searchpath)


    def about_triggered(self):
        QMessageBox.about(self, "TEMField", "Susceptibility measurements in (G)TEM-cell.\n\n(c) Prof. H. G. Krauthäuser")

    def cw_doubleSpinBox_changed(self):
        self.cw = self.ui.cw_doubleSpinBox.value()

    def am_spinBox_changed(self):
        self.am = self.ui.am_spinBox.value()

    def closeEvent(self, event):
        # fire confirmation box
        ret = self.ui.quit_MsgBox.exec()
        if ret == QMessageBox.Ok:
            self._save_setup()
            event.accept()
        else:
            event.ignore()

    def _read_setup(self):
        self.start_freq = self.settings.value("frequencies/start_freq", 30.)  # .toFloat()
        self.stop_freq = self.settings.value("frequencies/stop_freq", 1000.)  # .toFloat()
        self.step_freq = self.settings.value("frequencies/step_freq", 1.)  # .toFloat()
        self.log_sweep = self.settings.value("frequencies/log_sweep", True)  # .toInt()
        self.cw = self.settings.value("fieldstrength/cw", 1.)
        self.am = self.settings.value("fieldstrength/am", 80.)
        self.dwell_time = self.settings.value("settings/dwell_time", 1.)
        self.dotfile = self.settings.value("settings/dotfile", os.path.abspath('./conf/gtem.dot'))
        self.searchpath = self.settings.value("settings/searchpath", ['.', os.path.abspath('./conf')])
        # print("Init: ", self.log_sweep)
        # print(type(self.log_sweep), self.log_sweep)
        self.ui.log_sweep_checkBox.setChecked(self.log_sweep)
        self.ui.freq_start_doubleSpinBox.setValue(self.start_freq)
        self.ui.freq_stop_doubleSpinBox.setValue(self.stop_freq)
        self.ui.freq_step_doubleSpinBox.setValue(self.step_freq)
        self.ui.cw_doubleSpinBox.setValue(self.cw)
        self.ui.am_spinBox.setValue(self.am)
        self.ui.dwell_time_doubleSpinBox.setValue(self.dwell_time)
        self.ui.graph_file_lineEdit.setText(self.dotfile)
        self.ui.search_path_lineEdit.setText(str(self.searchpath))

    def _save_setup(self):
        self.settings.setValue("frequencies/start_freq", self.start_freq)
        self.settings.setValue("frequencies/stop_freq", self.stop_freq)
        self.settings.setValue("frequencies/step_freq", self.step_freq)
        self.settings.setValue("frequencies/log_sweep", self.log_sweep)
        self.settings.setValue("fieldstrength/cw", self.cw)
        self.settings.setValue("fieldstrength/am", self.am)
        self.settings.setValue("settings/dwell_time", self.dwell_time)
        self.settings.setValue("settings/searchpath", self.searchpath)
        self.settings.setValue("settings/dotfile", self.dotfile)
        # print("Exit: ", self.log_sweep)
        self.settings.sync()

    def update(self):
        if self.disable_update:
            return
        # print("update")
        self.log_sweep = True if self.ui.log_sweep_checkBox.checkState() == Qt.Checked else False
        # print("update", self.log_sweep)
        if not self.log_sweep:
            self.ui.freq_step_doubleSpinBox.setSuffix(' MHz')
            self.ui.freq_step_doubleSpinBox.setDecimals(4)
            self.ui.freq_step_doubleSpinBox.setRange(0, 99999.9999)
        else:
            self.ui.freq_step_doubleSpinBox.setSuffix('%')
            self.ui.freq_step_doubleSpinBox.setDecimals(2)
            self.ui.freq_step_doubleSpinBox.setRange(0, 99.99)

        self.start_freq = self.ui.freq_start_doubleSpinBox.value()
        self.stop_freq = self.ui.freq_stop_doubleSpinBox.value()
        self.step_freq = self.ui.freq_step_doubleSpinBox.value()
        if not self.log_sweep:
            self.freqs = linspace(self.start_freq, self.stop_freq, self.step_freq, endpoint=True)
        else:
            self.freqs = logspace(self.start_freq, self.stop_freq, 1+self.step_freq*0.01, endpoint=True)
        self.ui.nr_freqs_lineEdit.setText(str(len(self.freqs)))
        self.ui.freqs_plainTextEdit.setPlainText('\n'.join(map(str, self.freqs)))

        self.dwell_time = self.ui.dwell_time_doubleSpinBox.value()
        time_s = self.dwell_time*len(self.freqs)
        self.ui.est_time_lineEdit.setText(' '+str(datetime.timedelta(seconds=time_s))+' (hh:mm:ss)')

if __name__ == "__main__":
    #QApplication.shutdown()
    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()
    app.setOrganizationName("TUD-TETEMV")
    app.setOrganizationDomain("tu-dresden.de/et/tet")
    app.setApplicationName("TEMField")
    settings = QSettings()

    QLocale.setDefault(QLocale.English)

    widget = MainWindow(settings)
    widget.show()
    sys.exit(app.exec())
