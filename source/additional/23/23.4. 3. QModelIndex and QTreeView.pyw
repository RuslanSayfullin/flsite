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
parent = model.invisibleRootItem()
for i in range(0, 4):
    item = QtGui.QStandardItem("Пункт {0}-1".format(i))
    parent.appendRow(item)
    item = QtGui.QStandardItem("Пункт {0}-2".format(i))
    parent.appendRow(item)
    item = QtGui.QStandardItem("Пункт {0}-3".format(i))
    parent.appendRow(item)
    parent = item
view.setModel(model)

button = QtWidgets.QPushButton("Получить значения")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(view)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec())
