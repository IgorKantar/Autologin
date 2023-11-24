from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
)

class MainWidget(QWidget):

    def __init__(self, parent) -> None:
        super().__init__()
        self.parent = parent
        self.layout = QVBoxLayout()

        self.setLayout(self.layout)