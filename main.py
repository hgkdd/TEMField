# This Python file uses the following encoding: utf-8
import sys
import time

import numpy as np

from PySide6.QtCore import QDate
from matplotlib.backends.backend_qtagg import FigureCanvas
#from matplotlib.backends.qt_compat import QtWidgets
from matplotlib.figure import Figure

from PySide6.QtWidgets import QApplication, QMainWindow

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic mainwindow.ui -o mainwindow.py
from mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        efield_canvas = FigureCanvas(Figure(figsize=(5, 4)))
        self.ui.EFieldWAV_scrollArea.setWidget(efield_canvas)
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
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
