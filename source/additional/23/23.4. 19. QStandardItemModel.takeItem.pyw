from PyQt6 import QtWidgets, QtGui
import sys

def on_clicked():
    ind = view.currentIndex()
    if ind.isValid():
        print("Данные:", ind.data())
        print("Строка:", ind.row(), "Столбец:", ind.column())
    else:
        print("Нет текущего элемента")
    
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QTableView")
window.resize(500, 200)
view = QtWidgets.QTableView()

model = QtGui.QStandardItemModel()
model.setRowCount(3)
model.setColumnCount(4)
for row in range(0, 3):
    for column in range(0, 4):
        item = QtGui.QStandardItem("({0}, {1})".format(row, column))
        model.setItem(row, column, item)

item1 = model.takeItem(0, 0)
item2 = model.takeItem(0, 1)
model.setItem(0, 0, item2)
model.setItem(0, 1, item1)

view.setModel(model)
button = QtWidgets.QPushButton("Получить значение")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(view)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec())
