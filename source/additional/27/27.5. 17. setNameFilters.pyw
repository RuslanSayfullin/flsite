from PyQt6 import QtCore, QtWidgets
import sys

def on_clicked():
    dialog = QtWidgets.QFileDialog(parent=window,
                            caption="Это заголовок окна")
    dialog.setAcceptMode(QtWidgets.QFileDialog.AcceptMode.AcceptOpen)
    dialog.setDirectory(QtCore.QDir.currentPath())
    dialog.setNameFilters(["All (*)", "Images (*.png *.jpg)"])
    result = dialog.exec()
    if result == QtWidgets.QDialog.DialogCode.Accepted:
        print(dialog.selectedFiles())
    else:
        print("Нажата кнопка Cancel")

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QFileDialog")
window.resize(300, 70)

button = QtWidgets.QPushButton("Отобразить диалоговое окно...")
button.clicked.connect(on_clicked)

box = QtWidgets.QVBoxLayout()
box.addWidget(button)
window.setLayout(box)
window.show()

sys.exit(app.exec())
