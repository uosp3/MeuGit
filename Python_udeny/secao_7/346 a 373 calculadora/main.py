import sys

from buttons import ButtonsGrid
from display import Display
from info import Info
from main_window import MainWindow
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from styles import setupTheme
from variables import WINDOW_ICON_PATH

if __name__ == '__main__':
    # cria a aplicação
    app = QApplication(sys.argv)
    setupTheme(app)
    window = MainWindow()  # gera uma janela, vide classe em main_window.py

    # Define o icone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Info
    info = Info('Sua conta')  # informação que aparece como anterior
    window.addWidgetToVLayout(info)  # coloca a informação no layout

    # Display
    display = Display()
    window.addWidgetToVLayout(display)

    # Grid
    buttonsGrid = ButtonsGrid(display, info, window)
    window.vLayout.addLayout(buttonsGrid)

    # Executa tudo
    window.adjustFixedSize()  # chama função que ajusta e inibe redimensionar
    window.show()  # mostra a janela
    app.exec()
