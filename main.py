# This Python file uses the following encoding: utf-8
import sys
import time
import io
import numpy as np

from PySide6.QtCore import QDate
from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.figure import Figure

from PySide6.QtWidgets import QApplication, QMainWindow

import mpy.device.prb_lumiloop_lsporobe as lumiprb
from mpy.tools.spacing import logspace
from TestSusceptibility import TestSusceptibiliy

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic mainwindow.ui -o mainwindow.py
from mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.meas = TestSusceptibiliy()
        self.meas.setup_measurement()
        try:
            self.meas.init_measurement()
            freqs = logspace(30e6, 4.2e9, factor=1.10, endpoint=True)
            for f in freqs:  # [30e6, 500e6, 1000e6, 2000e6]:
                self.meas.do_measurement(f)
        finally:
            self.meas.finalize_measurement()

        sys.exit()


        efield_canvas = FigureCanvas(Figure(figsize=(5, 4)))
        self.ui.EFieldWAV_scrollArea.setWidget(efield_canvas)

        # init field probe
        ini = format_block("""
                                [DESCRIPTION]
                                description: 'LSProbe 1.2'
                                type:        'FIELDPROBE'
                                vendor:      'LUMILOOP'
                                serialnr:
                                deviceid:
                                driver:

                                [Init_Value]
                                fstart: 10e3
                                fstop: 8.2e9
                                fstep: 0
                                visa: TCPIP0::192.168.88.3::10000::SOCKET
                                mode: 0
                                virtual: 0

                                [Channel_1]
                                name: EField
                                unit: Voverm
                                """)
        ini = io.StringIO(ini)

        prb = lumiprb.FIELDPROBE()
        prb.Init(ini=ini, channel=1)
        err, des = prb.GetDescription()


        self._efield_ax = efield_canvas.figure.subplots()
        t = np.linspace(0, 10, 101)
        # Set up a Line2D.
        self._line, = self._efield_ax.plot(t, np.sin(t + time.time()))
        self._timer = efield_canvas.new_timer(50)
        self._timer.add_callback(self._update_efield)
        self._timer.start()

    def _update_efield(self):
        t = np.linspace(0, 10, 101)
        # Shift the sinusoid as a function of time.
        self._line.set_data(t, np.sin(t + time.time()))
        self._line.figure.canvas.draw()


if __name__ == "__main__":
    #app = QApplication(sys.argv)
    widget = MainWindow()
    #widget.show()
    #sys.exit(app.exec())
