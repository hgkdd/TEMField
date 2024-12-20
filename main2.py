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
from mainwindow2 import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.meas = TestSusceptibiliy()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
