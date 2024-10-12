from PyQt6 import QtCore, QtWidgets
import sys

def on_clicked():
    view.setFocus()
    view.scrollTo(model.index(50), 
               hint=QtWidgets.QAbstractItemView.ScrollHint.PositionAtCenter)

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QListView")
window.resize(300, 200)

view = QtWidgets.QListView()

L = []
for i in range(1, 110):
    L.append("Пункт {0}".format(i))
model = QtCore.QStringListModel(L)
view.setModel(model)

button = QtWidgets.QPushButton("Сделать элемент с индексом 50 видимым")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(view)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec())
