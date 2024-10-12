from PyQt6 import QtCore, QtWidgets, QtGui
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.label = QtWidgets.QLabel("Содержимое страницы")
        self.button = QtWidgets.QPushButton("Проверить положение панели")
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
        self.setIconSize(QtCore.QSize(32, 32))
        #self.setAnimated(False)
        self.add_menu()
        self.add_tool_bar()

    def add_menu(self):
        self.menuFile = QtWidgets.QMenu("&File")
        self.actOpen = QtGui.QAction("Open", None)
        ico = self.style().standardIcon(
                   QtWidgets.QStyle.StandardPixmap.SP_ComputerIcon)
        self.actOpen.setIcon(ico)
        self.actOpen.setShortcut(QtGui.QKeySequence.StandardKey.Open)
        self.actOpen.triggered.connect(self.on_open)
        self.menuFile.addAction(self.actOpen)
        self.menuBar().addMenu(self.menuFile)

    def add_tool_bar(self):
        self.toolBar = QtWidgets.QToolBar("MyToolBar")
        self.toolBar.addAction(self.actOpen)
        self.toolBar.setIconSize(QtCore.QSize(24, 24))
        self.toolBar.setFloatable(True)
        
        self.toolBar.actionTriggered.connect(self.on_triggered)
        self.toolBar.topLevelChanged[bool].connect(
                                           self.on_topLevelChanged)
        self.toolBar.visibilityChanged[bool].connect(
                                             self.on_visibilityChanged)
        self.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        
        self.addToolBarBreak(QtCore.Qt.ToolBarArea.TopToolBarArea)
        
        self.toolBar2 = QtWidgets.QToolBar("MyToolBar2")
        self.toolBar2.setToolButtonStyle(
                      QtCore.Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.toolBar2.setFloatable(False)
        ico = self.style().standardIcon(
                   QtWidgets.QStyle.StandardPixmap.SP_DialogCloseButton)
        self.actQuit = self.toolBar2.addAction(ico, "Quit",
                                QtWidgets.QApplication.instance().quit)
        self.actQuit.setShortcut(QtGui.QKeySequence.StandardKey.Quit)
        self.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolBar2)

    def on_open(self):
        print("Выбран пункт меню Open")

    def on_triggered(self, act):
        print("Выбрано дейстие", act.text())

    def on_topLevelChanged(self, status):
        print("on_topLevelChanged", status)

    def on_visibilityChanged(self, status):
        print("visibilityChanged", status)

    def on_clicked(self):
        print(self.toolBar.isFloating())

app = QtWidgets.QApplication(sys.argv)
window = MyWindow()
window.setWindowTitle("Класс QToolBar")
window.resize(500, 350)

window.show()
sys.exit(app.exec())
