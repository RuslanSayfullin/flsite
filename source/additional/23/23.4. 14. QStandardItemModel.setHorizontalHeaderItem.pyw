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

model.setHorizontalHeaderItem(0, QtGui.QStandardItem("A"))
model.setHorizontalHeaderItem(1, QtGui.QStandardItem("B"))
model.setHorizontalHeaderItem(2, QtGui.QStandardItem("C"))
model.setHorizontalHeaderItem(3, QtGui.QStandardItem("D"))

model.setVerticalHeaderItem(0, QtGui.QStandardItem("01"))
model.setVerticalHeaderItem(1, QtGui.QStandardItem("02"))
model.setVerticalHeaderItem(2, QtGui.QStandardItem("03"))

view.setModel(model)
button = QtWidgets.QPushButton("Получить значение")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(view)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec())
