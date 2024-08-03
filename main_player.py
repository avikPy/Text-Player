from player import *
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QIcon

class App(QMainWindow):
    def __init__(self) -> None:
        super(App, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
if __name__ == '__main__':
    app = QApplication([])
    
    win = App()
    win.setFixedSize(699, 341)
    win.setWindowIcon(QIcon('player_icon.ico'))
    win.show()
    app.exec()