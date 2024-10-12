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
window.resize(500, 400)
view = QtWidgets.QTableView()

model = QtGui.QStandardItemModel(4, 4)
for row in range(0, 4):
    for column in range(0, 4):
        item = QtGui.QStandardItem("({0}, {1})".format(row, column))
        model.setItem(row, column, item)
view.setModel(model)
model.setHorizontalHeaderLabels(["A", "B", "C", "D"])
model.setVerticalHeaderLabels(["01", "02", "03", "04"])

view.setRowHeight(0, 100)
view.setColumnWidth(0, 250)

button = QtWidgets.QPushButton("Получить значение")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(view)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec())
