from PyQt6 import QtWidgets
import sys

def on_clicked():
    print(textEdit.textCursor().position())
    print(textEdit.textCursor().positionInBlock())

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QTextCursor")
window.resize(500, 250)
textEdit = QtWidgets.QTextEdit()
textEdit.setPlainText("Блок 1\nБлок 2\nБлок 3\nБлок 4\nБлок 5 jjkh "
                      "hkjhkjh khk hkh khk jhkh hkh khk hk hkh hkj hk "
                      "hkhk k kjh kh jh kh khk hkh khk hkjh kh kh kjh "
                      "kjhkj h kh kh kjh khk hk kh kh k")
button = QtWidgets.QPushButton("Вывести позицию курсора")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(textEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec())
