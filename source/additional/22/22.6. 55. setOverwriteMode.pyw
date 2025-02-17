from PyQt6 import QtWidgets
import sys

def on_clicked():
    textEdit.setOverwriteMode(not textEdit.overwriteMode())

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QTextEdit")
window.resize(500, 250)
textEdit = QtWidgets.QTextEdit("Значение <b>по умолчанию</b>")
textEdit.setOverwriteMode(True)
button = QtWidgets.QPushButton("Переключить режим")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(textEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec())
