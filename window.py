from PySide6.QtCore import Qt

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QSplitter,
)

from cipher import AESCipher
from button_list import ButtonList
from dialogs import (
    AddSiteDialog,
)

class MainWidget(QWidget):

    def __init__(self, parent) -> None:
        super().__init__()
        self.parent = parent
        self.layout = QVBoxLayout()
        self.label  = QLabel("Sites:")
        self.cipher = AESCipher("kljuc")
        self.data = self.cipher.load()
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

        self.addButton.clicked.connect(self.handle_add)

    def handle_add(self):
        self.dlg = AddSiteDialog(self)
        self.dlg.exec_()