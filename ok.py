import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

class HelloWorld(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.label = QLabel("Hello, PyQt!", self)
        self.label.move(50, 50)
        self.setWindowTitle('PyQt Example')
        self.setGeometry(300, 300, 250, 150)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = HelloWorld()
    sys.exit(app.exec_())
