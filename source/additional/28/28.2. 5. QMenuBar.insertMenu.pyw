from PyQt6 import QtWidgets, QtGui
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.label = QtWidgets.QLabel("Содержимое страницы")
        self.button = QtWidgets.QPushButton("Сделать меню File активным")
        self.box = QtWidgets.QVBoxLayout()
        self.box.addWidget(self.label)
        self.box.addWidget(self.button)
        self.setLayout(self.box)

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.w = MyWidget()
        self.setCentralWidget(self.w)
        self.w.button.clicked.connect(self.on_clicked)
        self.add_menu()

    def add_menu(self):
        self.myMenuBar = QtWidgets.QMenuBar()
        self.setMenuBar(self.myMenuBar)
        
        self.menuFile = QtWidgets.QMenu("&File")
        self.actOpen = QtGui.QAction("Open", None)
        self.actOpen.setShortcut(QtGui.QKeySequence.StandardKey.Open)
        self.actOpen.triggered.connect(self.on_open)
        self.menuFile.addAction(self.actOpen)
        self.actMenuFile = self.myMenuBar.addMenu(self.menuFile)
        self.actMenuFile.setEnabled(False)
        self.myMenuBar.addSeparator()
        
        self.menuHelp = QtWidgets.QMenu("&Help")
        self.actHelp = QtGui.QAction("Help", None)
        self.actHelp.setShortcut("F1")
        self.actHelp.triggered.connect(self.on_help)
        self.menuHelp.addAction(self.actHelp)
        self.myMenuBar.insertMenu(self.actMenuFile, self.menuHelp)

    def on_open(self):
        print("Выбран пункт меню Open")

    def on_help(self):
        print("Выбран пункт меню Help")

    def on_clicked(self):
        self.actMenuFile.setEnabled(True)

app = QtWidgets.QApplication(sys.argv)
window = MyWindow()
window.setWindowTitle("Класс QMenuBar")
window.resize(500, 350)

window.show()
sys.exit(app.exec())
