from PyQt6 import QtCore, QtWidgets, QtGui
import sys

def on_clicked():
    sel = view.selectionModel()
    print("hasSelection:", sel.hasSelection())
    print("isSelected:", sel.isSelected(view.model().index(0, 0)))

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QItemSelectionModel")
window.resize(400, 300)
view = QtWidgets.QTableView()

model = QtGui.QStandardItemModel(4, 2)
for row in range(0, 4):
    for column in range(0, 2):
        item = QtGui.QStandardItem("({0}, {1})".format(row, column))
        model.setItem(row, column, item)
model.setHorizontalHeaderLabels(["A", "B"])
model.setVerticalHeaderLabels(["01", "02", "03", "04"])
view.setModel(model)

selModel = QtCore.QItemSelectionModel(model)
view.setSelectionModel(selModel)

button = QtWidgets.QPushButton("Проверить выделение")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(view)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec())
