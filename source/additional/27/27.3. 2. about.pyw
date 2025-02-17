from PyQt6 import QtWidgets
import sys

def on_clicked():
    QtWidgets.QMessageBox.about(window, "Текст заголовка", 
                                        "Описание программы")

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QMessageBox")
window.resize(300, 70)

ico = window.style().standardIcon(
             QtWidgets.QStyle.StandardPixmap.SP_MessageBoxCritical)
app.setWindowIcon(ico)    # Иконка приложения

button = QtWidgets.QPushButton("Отобразить диалоговое окно...")
button.clicked.connect(on_clicked)

box = QtWidgets.QVBoxLayout()
box.addWidget(button)
window.setLayout(box)
window.show()

sys.exit(app.exec())
