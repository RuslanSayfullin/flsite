from PyQt6 import QtWidgets, QtGui, QtCore
import sys

def on_clicked():
    ind = view.currentIndex()
    if ind.isValid():
        print("Данные:", ind.data())
        print("Строка:", ind.row(), "Столбец:", ind.column())
        ind_parent = ind.parent()
        if ind_parent.isValid():
            print("Родитель:", ind_parent.data())
        else:
            print("Нет родителя")

        item = model.itemFromIndex(ind)
        item_child = item.child(0)
        if item_child:
            print("Потомок:", item_child.data(
                  role=QtCore.Qt.ItemDataRole.DisplayRole))
        else:
            print("Нет потомка")

        ind_sibling = ind.sibling(0, 0)
        if ind_sibling.isValid():
            print("Сосед:", ind_sibling.data())
        else:
            print("Нет соседа")

    else:
        print("Нет текущего элемента")

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QTreeView")
window.resize(500, 400)
view = QtWidgets.QTreeView()

model = QtGui.QStandardItemModel()
model.setColumnCount(4)

parent = QtGui.QStandardItem(3, 4)
parent.setText("Элемент-родитель")
for row in range(0, 3):
    for column in range(0, 4):
        item = QtGui.QStandardItem("({0}, {1})".format(row, column))
        parent.setChild(row, column, item)
model.appendRow(parent)

parent.setSelectable(False)

item2 = QtGui.QStandardItem("Пункт нельзя выделить")
item2.setSelectable(False)
model.appendRow(item2)

item3 = QtGui.QStandardItem("Пункт нельзя редактировать")
item3.setEditable(False)
model.appendRow(item3)

item4 = QtGui.QStandardItem("С пунктом нельзя взаимодействовать")
item4.setEnabled(False)
model.appendRow(item4)

view.setModel(model)

button = QtWidgets.QPushButton("Получить значения")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(view)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec())
