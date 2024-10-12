from PyQt6 import QtWidgets, QtGui
import sys

def on_clicked():
    view.collapse(view.model().index(0, 0))

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QTreeView")
window.resize(500, 400)
view = QtWidgets.QTreeView()

model = QtGui.QStandardItemModel()
model.setColumnCount(4)
parent = model.invisibleRootItem()
for i in range(0, 4):
    item = QtGui.QStandardItem("Пункт {0}-1".format(i))
    parent.appendRow(item)
    parent = item

parent = QtGui.QStandardItem(3, 4)
parent.setText("Элемент-родитель")
for row in range(0, 3):
    for column in range(0, 4):
        item = QtGui.QStandardItem("({0}, {1})".format(row, column))
        parent.setChild(row, column, item)
model.appendRow(parent)

view.setModel(model)

view.setColumnWidth(0, 200)
view.expandAll()

button = QtWidgets.QPushButton("Скрыть дочерние элементы элемента 1")
button.clicked.connect(on_clicked)
button2 = QtWidgets.QPushButton("Скрыть все дочерние элементы")
button2.clicked.connect(view.collapseAll)
box = QtWidgets.QVBoxLayout()
box.addWidget(view)
box.addWidget(button)
box.addWidget(button2)
window.setLayout(box)
window.show()
sys.exit(app.exec())
