import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

from buttons import ButtonsGrid
from display import Display
from info import Info
from main_window import MainWindow
from variables import ICON_DIR

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()

    # Define icone
    icon = QIcon(str(ICON_DIR))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Info
    info = Info('Sua Conta')
    window.addWidgetToVLayout(info)

    # Display
    display = Display()
    window.addWidgetToVLayout(display)

    # Buttons Grid
    buttonGrid = ButtonsGrid(display, info, window)
    window.vLayout.addLayout(buttonGrid)

    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()
