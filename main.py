
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic,QtGui

class UI(QMainWindow):
    def __init__(self):
        super().__init__()
        # loading the ui file with uic modul
        self.setWindowIcon(QtGui.QIcon('icon.ico'))
        uic.loadUi("app.ui", self)
        self.pass_btn.clicked.connect(self.change_pass)
        self.btn_clear.clicked.connect(self.clear)
    def clear(self):
        self.out.clear()
    def change_pass(self):
        import secrets
        import string
        letters = string.ascii_letters
        digits = string.digits
        special_chars = string.punctuation
        alphabet = letters + digits + special_chars
        pwd_length = int(self.leng.text())
        pwd = ''
        for i in range(pwd_length):
            pwd += ''.join(secrets.choice(alphabet))
        while True:
            pwd = ''
            for i in range(pwd_length):
                pwd += ''.join(secrets.choice(alphabet))
            if (any(char in special_chars for char in pwd) and
                    sum(char in digits for char in pwd) >= 2):
                break
        self.out.appendPlainText(pwd)
if __name__ == "__main__":
    app = QApplication([])
    window = UI()
    window.show()
    app.exec()