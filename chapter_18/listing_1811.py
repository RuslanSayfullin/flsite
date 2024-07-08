from PyQt6 import QtWidgets
import sys, time
def on_clicked():
    time.sleep(3) # "Засыпаем" на 10 секунд

# Выполнение длительной операции
app = QtWidgets.QApplication(sys.argv)
button = QtWidgets.QPushButton("Запустить процесс")
button.resize(200, 40)
button.clicked.connect(on_clicked)
button.show()
sys.exit(app.exec())
