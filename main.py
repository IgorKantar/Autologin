#!/usr/bin/env python
from os.path import (
    dirname,
)

from PySide6.QtCore import QDir

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
)

from window import MainWidget

basedir = dirname(__file__)

class Autologin(QMainWindow):

    def __init__(self) -> None:
        super().__init__()

        self.mainView = MainWidget(self)

        # WINDOW ATTRIBUTES
        self.setWindowTitle("Autologin")
        self.setFixedSize(300, 400)

        self.setCentralWidget(self.mainView)

# required folders
def check_folders(folder_names: list[str]):
    for name in folder_names:
        if not QDir(name).exists():
            QDir().mkdir(name)

if __name__ == "__main__":
    app = QApplication()

    check_folders([
        "icons",
    ])

    window = Autologin()
    window.show()

    app.exec()
