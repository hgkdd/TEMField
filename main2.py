# This Python file uses the following encoding: utf-8
import os.path
import sys
import csv
import datetime
import time
import numpy as np

from matplotlib.backends.backend_qtagg import FigureCanvas, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

from PySide6.QtCore import Qt, QLocale, QSettings, QTimer, QEventLoop, QThread
from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox,
                               QFileDialog, QTableWidgetItem, QVBoxLayout, QWidget)

import mpy.device.prb_lumiloop_lsporobe as lumiprb
from mpy.tools.spacing import logspace, linspace
from TestSusceptibility import TestSusceptibiliy

# Important:
# You need to run the following command to generate the mainwindow.py file
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
        self.ui.EUT_plainTextEdit.textChanged.connect(self.EUT_plainTextEdit_changed)
        self.ui.save_table_pushButton.clicked.connect(self.save_Table)
        # waveform
        self.efield_canvas = FigureCanvas(Figure(figsize=(5, 4)))
        self.efield_toolbar = NavigationToolbar(self.efield_canvas, self)

        layout = QVBoxLayout()
        layout.addWidget(self.efield_toolbar)
        layout.addWidget(self.efield_canvas)
        widget = QWidget()
        widget.setLayout(layout)
        self.ui.waveform_scrollArea.setWidget(widget)
        self._efield_ax = self.efield_canvas.figure.subplots()
        t = np.linspace(0, 10, 101)
        # Set up a Line2D.
        self._line, = self._efield_ax.plot(t, np.sin(t + time.time()))
        self._timer = self.efield_canvas.new_timer(50)
        self._timer.add_callback(self._update_efield)
        self._timer.start()

        self.meas = TestSusceptibiliy()
        self.ui.start_pause_pushButton.setDisabled(False)
        self.ui.rf_pushButton.toggled.connect(self.toggle_rf)

    def _update_efield(self):
        t = np.linspace(0, 10, 101)
        # Shift the sinusoid as a function of time.
        self._line.set_data(t, np.sin(t + time.time()))
        self._line.figure.canvas.draw()

    def EUT_plainTextEdit_changed(self):
        self.eut_description = self.ui.EUT_plainTextEdit.toPlainText()

    def do_long_log(self, text):
        logtxt = f"{self.get_time_as_string()}: {text}"
        self.ui.logtab_log_plainTextEdit.appendPlainText(logtxt)

    def do_fill_table(self, freq=None, cw=None, status=None):
        table = self.ui.table_tableWidget
        rowposition = table.rowCount()
        table.insertRow(rowposition)
        val = QTableWidgetItem(self.get_time_as_string())
        val.setFlags(val.flags() & ~Qt.ItemIsEditable)
        table.setItem(rowposition, 0, val)
        val = QTableWidgetItem(str(freq))
        val.setFlags(val.flags() & ~Qt.ItemIsEditable)
        table.setItem(rowposition, 1, val)
        val = QTableWidgetItem(str(cw))
        val.setFlags(val.flags() & ~Qt.ItemIsEditable)
        table.setItem(rowposition, 2, val)
        table.setItem(rowposition, 3, QTableWidgetItem(str(status)))

        table.verticalScrollBar().setSliderPosition(table.verticalScrollBar().maximum())

    def process_frequencies(self):
        if self.pause_processing:
            QTimer.singleShot(100, self.process_frequencies)
        else:
            try:
                f = self.remaining_freqs.pop(0)
                self.ui.permanent_log_plainTextEdit.appendPlainText(f"Freq: {f} MHz")
                self.do_long_log(f"set freq to {f} MHz")
                self.do_fill_table(freq=f, cw=self.cw, status="passed")
                # wait and process next freq
                QTimer.singleShot(self.dwell_time * 1000, self.process_frequencies)
            except IndexError:
                # all freqs processed
                self.do_long_log("all frequencies processed")
                self.ui.rf_pushButton.setChecked(False)
                self.ui.start_pause_pushButton.setText("Start Test")

    def toggle_rf(self):
        if self.ui.rf_pushButton.isChecked():
            self.ui.permanent_log_plainTextEdit.appendPlainText('RF On')
            self.do_long_log("RF On")
        else:
            self.ui.permanent_log_plainTextEdit.appendPlainText('RF Off')
            self.do_long_log("RF Off")

    def start_pause_pushButton_clicked(self):
        if self.ui.start_pause_pushButton.text() == "Start Test":
            self.do_long_log("Start Test")
            self.do_long_log(f"EUT description: {self.eut_description}")
            self.pause_processing = False
            self.ui.start_pause_pushButton.setText("Pause Test")
            err = self.meas.Init(dwell_time=self.dwell_time,
                    e_target=self.cw,
                    names=self.names,
                    dotfile=self.dotfile,
                    SearchPath=self.searchpath)
            self.meas.init_measurement()
            self.remaining_freqs = self.freqs.copy()
            self.ui.rf_pushButton.setChecked(True)
            self.process_frequencies()
        elif self.ui.start_pause_pushButton.text() == "Pause Test":
            self.do_long_log("Pause Test")
            self.ui.start_pause_pushButton.setText("Cont. Test")
            self.ui.rf_pushButton.setChecked(False)
            self.pause_processing = True
        else:
            self.do_long_log("Continue Test")
            self.ui.start_pause_pushButton.setText("Pause Test")
            self.ui.rf_pushButton.setChecked(True)
            self.pause_processing = False


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
        self.do_long_log("close event")
        ret = QMessageBox.question(self, "TEMField",
                                       "Do you want to exit the application?",
                                           QMessageBox.Yes, QMessageBox.No)
        if ret == QMessageBox.Yes:
            self._save_setup()
            self.do_long_log("Exit Application")
            event.accept()
        else:
            self.do_long_log("Continue Application")
            event.ignore()

    def _read_setup(self):
        self.do_long_log("read setup")
        self.start_freq = self.settings.value("frequencies/start_freq", 30.)  # .toFloat()
        self.stop_freq = self.settings.value("frequencies/stop_freq", 1000.)  # .toFloat()
        self.step_freq = self.settings.value("frequencies/step_freq", 1.)  # .toFloat()
        self.log_sweep = self.settings.value("frequencies/log_sweep", True)  # .toInt()
        self.cw = self.settings.value("fieldstrength/cw", 1.)
        self.am = self.settings.value("fieldstrength/am", 80.)
        self.dwell_time = self.settings.value("settings/dwell_time", 1.)
        self.dotfile = self.settings.value("settings/dotfile", os.path.abspath('./conf/gtem.dot'))
        self.searchpath = self.settings.value("settings/searchpath", ['.', os.path.abspath('./conf')])
        self.names = self.settings.value("settings/names", {'sg': 'sg', 'a1': 'amp1', 'a2': 'amp2',
                                                            'tem': 'gtem', 'fp': 'prb'})
        self.eut_description = self.settings.value("settings/eut-description", '')
        self.table_save_dir = self.settings.value("settings/table-save-dir", '.')
        self.table_save_dir = os.path.abspath(self.table_save_dir)
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
        for row,key in enumerate(['sg', 'a1', 'a2', 'tem', 'fp']):
            self.ui.node_names_tableWidget.setItem(row, 1, QTableWidgetItem(self.names[key]))
        self.ui.EUT_plainTextEdit.setPlainText(self.eut_description)

    def _save_setup(self):
        self.do_long_log("save setup")
        self.settings.setValue("frequencies/start_freq", self.start_freq)
        self.settings.setValue("frequencies/stop_freq", self.stop_freq)
        self.settings.setValue("frequencies/step_freq", self.step_freq)
        self.settings.setValue("frequencies/log_sweep", self.log_sweep)
        self.settings.setValue("fieldstrength/cw", self.cw)
        self.settings.setValue("fieldstrength/am", self.am)
        self.settings.setValue("settings/dwell_time", self.dwell_time)
        self.settings.setValue("settings/searchpath", self.searchpath)
        self.settings.setValue("settings/dotfile", self.dotfile)
        self.settings.setValue("settings/names", self.names)
        self.settings.setValue("settings/eut-description", self.eut_description)
        self.settings.setValue("settings/table-save-dir", self.table_save_dir)
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

    def get_time_as_string(self, format=None):
        if format is None:
            format = "%Y-%m-%dT%H:%M:%S.%f%z"
        tz = datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo
        tstr = datetime.datetime.now(tz=tz).strftime(format)
        return tstr

    def save_Table(self):
        path, _ = QFileDialog.getSaveFileName(self, 'Save as CSV', self.table_save_dir, '(*.csv)')
        self.table_save_dir = os.path.dirname(path)
        if path:
            columns = range(self.ui.table_tableWidget.columnCount())
            header = [self.ui.table_tableWidget.horizontalHeaderItem(column).text()
                      for column in columns]
            with open(path, 'w') as csvfile:
                t = self.get_time_as_string()
                csvfile.write(f"# File saved: {t}\n#\n")
                csvfile.write('# EUT Description\n')
                plaintext_EUT = self.eut_description
                for eut_line in plaintext_EUT.splitlines():
                    csvfile.write(f"# {eut_line}\n")

                writer = csv.writer(
                    csvfile, dialect='excel', lineterminator='\n')
                writer.writerow(header)
                for row in range(self.ui.table_tableWidget.rowCount()):
                    writer.writerow(
                        self.ui.table_tableWidget.item(row, column).text()
                        for column in columns)


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
