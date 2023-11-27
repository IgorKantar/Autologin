from PySide6.QtCore import QSize

from PySide6.QtGui import (
	QStandardItemModel,
	QStandardItem,
)

from PySide6.QtWidgets import (
    QWidget,
    QListView,
    QPushButton,
    QVBoxLayout,
)

class ButtonList(QWidget):

    def __init__(self, parent) -> None:
        super().__init__()
        self.parent = parent
        self.layout = QVBoxLayout()

        self.init_list()
        self.populate_list()

        self.layout.addWidget(self.list)
        self.setLayout(self.layout)

    def init_list(self):
        # set up list
        self.list = QListView()
        self.list_model = QStandardItemModel(self.list)
        self.list.setModel(self.list_model)

    def populate_list(self):
        for site_dict in self.parent.data:
            item = QStandardItem("")
            item.setSizeHint(QSize(10,40))
            self.list_model.appendRow(item)
            self.list.setIndexWidget(item.index(), Button(self, site_dict))

    def clear(self):
        self.list_model.removeRows(0, self.list_model.rowCount())

class Button(QPushButton):
    """Button for editing specific website info."""

    def __init__(self, parent, website: dict) -> None:
        super().__init__()
        self.parent = parent
        self.set_attr(website)

        self.setText(self.name)

        self.clicked.connect(self.handle_click)

    def set_attr(self, d):
        for key in d:
            setattr(self, key, d[key])

    def handle_click(self):
        print(self.link)