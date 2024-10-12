from PyQt6 import QtCore, QtWidgets
import sys

def on_clicked():
    print("Кнопка нажата")
    
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QPushButton")
window.resize(300, 50)
button = QtWidgets.QPushButton("Выполнить операцию")
button.setShortcut("Alt+B")
button.clicked.connect(on_clicked)
vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(button)
window.setLayout(vbox)
window.show()
sys.exit(app.exec())
