from PySide6.QtWidgets import QMainWindow, QMessageBox, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        # Configurando Layout Básico
        self.widgetCentral = QWidget()
        self.vLayout = QVBoxLayout()

        self.widgetCentral.setLayout(self.vLayout)
        self.setCentralWidget(self.widgetCentral)

        # Título da janela
        self.setWindowTitle("Calculadora")

    def adjustFixedSize(self):
        # Última coisa a ser feita
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    def addWidgetToVLayout(self, widget: QWidget):
        self.vLayout.addWidget(widget)

    def makeMsgBox(self):
        return QMessageBox(self)
