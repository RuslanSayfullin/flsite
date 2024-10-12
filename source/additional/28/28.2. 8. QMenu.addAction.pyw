from PyQt6 import QtCore, QtWidgets, QtGui
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.label = QtWidgets.QLabel("Содержимое страницы")
        self.button = QtWidgets.QPushButton("Очистить меню File")
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
        self.menuFile = QtWidgets.QMenu("&File")
        self.actOpen = QtGui.QAction("Open", None)
        self.actOpen.setShortcut(QtGui.QKeySequence.StandardKey.Open)
        self.actOpen.triggered.connect(self.on_open)
        self.menuFile.addAction(self.actOpen)
        self.menuFile.addAction("Пункт &1")
        ico = self.style().standardIcon(
                   QtWidgets.QStyle.StandardPixmap.SP_MessageBoxCritical)
        self.menuFile.addAction(ico, "Пункт &2")
        self.menuFile.addAction("Пункт &3",
                         QtWidgets.QApplication.instance().quit,
                         shortcut="Ctrl+Q")
        self.menuFile.addAction("Пункт &4", self.on_act1,
                         QtGui.QKeySequence.fromString("Ctrl+S"))
        self.act5 = self.menuFile.addAction(ico, "Пункт &5",
                         QtWidgets.QApplication.instance().quit, 
                         shortcut=QtGui.QKeySequence.fromString("Ctrl+D"))
        self.menuFile.addAction(ico, "Пункт &6", self.on_act2, 
                                QtGui.QKeySequence("Ctrl+R"))
        self.menuFile.insertSeparator(self.act5)
        self.menuFile.addSeparator()
        self.actExit = QtGui.QAction("Exit", None)
        self.actExit.setShortcut("Ctrl+W")
        self.actExit.triggered.connect(
                     QtWidgets.QApplication.instance().quit)
        self.menuFile.addAction(self.actExit)
        self.actMenuFile = self.menuBar().addMenu(self.menuFile)

        self.menuHelp = QtWidgets.QMenu("&Help")
        self.actHelp = QtGui.QAction("Help", None)
        self.actHelp.setShortcut("F1")
        self.actHelp.triggered.connect(self.on_help)
        self.menuHelp.addAction(self.actHelp)
        self.menuBar().addMenu(self.menuHelp)

    def on_open(self):
        print("Выбран пункт меню Open")

    def on_help(self):
        print("Выбран пункт меню Help")

    def on_act1(self):
        print("on_act1")

    def on_act2(self):
        print("on_act2")

    def on_clicked(self):
        self.menuFile.clear()
        self.w.button.setEnabled(False)

app = QtWidgets.QApplication(sys.argv)
window = MyWindow()
window.setWindowTitle("Класс QMenu")
window.resize(500, 350)

window.show()
sys.exit(app.exec())
