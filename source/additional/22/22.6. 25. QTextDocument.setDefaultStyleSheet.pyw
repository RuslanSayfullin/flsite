from PyQt6 import QtWidgets, QtGui
import sys

def on_clicked():
    print(textEdit.document().toHtml())

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QTextDocument")
window.resize(500, 250)
textEdit = QtWidgets.QTextEdit()
document = QtGui.QTextDocument()
document.setDefaultStyleSheet("""
body { color:#FFFFFF; background-color:#000000; font-family: Tahoma;
    font-size: 30pt;}
""")
document.setHtml("<html><body><p>Текст внутри поля</p></body></html>")
textEdit.setDocument(document)
button = QtWidgets.QPushButton("Получить HTML-текст")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(textEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec())
