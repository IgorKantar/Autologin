from PySide6.QtCore import QSize

from PySide6.QtGui import (
	QStandardItemModel,
	QStandardItem,
)

from PySide6.QtWidgets import (
    QWidget,
    QListView,
)

class ButtonList(QWidget):

    def __init__(self, parent) -> None:
        super().__init__()

        self.init_list()
        self.populate_list()

    def init_list(self):
        # set up list
        self.list = QListView()
        self.list_model = QStandardItemModel(self.list)
        self.list.setModel(self.list_model)

    def populate_list(self):
        pass