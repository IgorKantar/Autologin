from PySide6.QtCore import Qt

from PySide6.QtWidgets import (
    QDialog,
    QDialogButtonBox,
    QLabel,
    QFormLayout,
    QVBoxLayout,
    QLineEdit,
    QMessageBox,
    QApplication,
)

class AddSiteDialog(QDialog):
    """
    Form for adding a website to the autologin list.
    """

    def __init__(self, parent) -> None:
        super().__init__()
        self.parent = parent
        self.form   = QFormLayout()
        self.layout = QVBoxLayout()

        self.setWindowTitle("Add Website Form")
        self.setFixedSize(300,200)
        self.layout.setAlignment(Qt.AlignTop)

        # WIDGETS
        buttons = QDialogButtonBox.Save | QDialogButtonBox.Cancel
        self.buttonBox  = QDialogButtonBox(buttons)
        self.nameEdit   = ("Name: ", QLineEdit())
        self.linkEdit   = ("Link: ", QLineEdit())
        self.unameEdit  = ("User: ", QLineEdit())
        self.passwEdit  = ("Pass: ", QLineEdit())
        self.passwEdit[1].setEchoMode(QLineEdit.Password)
        self.formList = [
            self.nameEdit,
            self.linkEdit,
            self.unameEdit,
            self.passwEdit,
        ]

        # FILL LAYOUT
        self.layout.addWidget(QLabel("Enter website info:"))
        for l, le in self.formList:
            self.form.addRow(l, le)
        self.layout.addLayout(self.form)
        self.layout.addWidget(self.buttonBox)

        self.setLayout(self.layout)

        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

    def accept(self):
        button = QMessageBox.question(
            self,
            "Save",
            "Are you sure you want to save these credentials?"
        )
        if button == QMessageBox.Yes:
            self.handle_save()

    def handle_save(self):
        cipher = self.parent.cipher
        d = {
            "name": self.formList[0][1].text(),
            "link": self.formList[1][1].text(),
            "user": cipher.encrypt(self.formList[2][1].text()),
            "pw":   cipher.encrypt(self.formList[3][1].text()),
        }
        self.parent.data.append(d)
        cipher.save(self.parent.data)