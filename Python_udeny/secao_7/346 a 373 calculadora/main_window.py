from PySide6.QtWidgets import QMainWindow, QMessageBox, QVBoxLayout, QWidget


class MainWindow(QMainWindow):  # a classe herda de QMainWindow
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        # configurando o layout básico
        self.cw = QWidget()  # cria widget central
        self.vLayout = QVBoxLayout()  # cria o layout vertical
        self.cw.setLayout(self.vLayout)  # coloca o layou no widget central
        self.setCentralWidget(self.cw)  # coloca o widget central na janela

        # coloca um título na janela
        self.setWindowTitle('Calculadora')

    def adjustFixedSize(self):
        # ultima coisa a ser feita
        self.adjustSize()  # ajusta o tamanho da janela
        self.setFixedSize(self.width(), self.height())  # não redimensionar

    def addWidgetToVLayout(self, widget: QWidget):
        self.vLayout.addWidget(widget)

    def makeMsgBox(self):
        return QMessageBox(self)
