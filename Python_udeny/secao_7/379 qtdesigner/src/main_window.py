import sys
from PySide6.QtCore import QEvent
from PySide6.QtGui import QKeyEvent
from PyQt5 import QtWidgets
from window import Ui_MainWindow
from typing import cast


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.buttonSend.clicked.connect(self.changeLabelResult)

        self.lineName.installEventFilter(self)

    def changeLabelResult(self):
        text = self.lineName.text()
        self.labelResult.setText(f"Olá, {text}!")

    def eventFilter(self, watched, event) -> bool:

        if event.type() == QEvent.Type.KeyPress:
            event = cast(QKeyEvent, event)
            text = self.lineName.text()
            self.labelResult.setText(text + event.text())

        return super().eventFilter(watched, event)  # type: ignore


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    app.exec()
