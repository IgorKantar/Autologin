from PySide6.QtCore import Qt

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QSplitter,
)

from button_list import ButtonList

class MainWidget(QWidget):

    def __init__(self, parent) -> None:
        super().__init__()
        self.parent = parent
        self.layout = QVBoxLayout()
        self.label  = QLabel("Sites:")
        self.buttonList = ButtonList(self)
        self.addButton  = QPushButton("+")

        self.layout.setAlignment(Qt.AlignTop)

        for widget in [
            self.label,
            self.buttonList,
            QSplitter(),
            self.addButton,
        ]:
            self.layout.addWidget(widget)

        self.setLayout(self.layout)