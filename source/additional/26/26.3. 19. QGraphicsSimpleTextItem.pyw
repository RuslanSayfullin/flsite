from PyQt6 import QtCore, QtWidgets, QtGui
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QGraphicsSimpleTextItem")
window.resize(600, 600)

scene = QtWidgets.QGraphicsScene(0.0, 0.0, 500.0, 535.0)
scene.setBackgroundBrush(QtCore.Qt.GlobalColor.white)

item = QtWidgets.QGraphicsSimpleTextItem()
item.setText("Простой текст")
item.setPen(QtGui.QPen(QtCore.Qt.GlobalColor.darkBlue, 3))
item.setFont(QtGui.QFont("Verdana", 25))
item.setPos(QtCore.QPointF(50.0, 150.0))
item.setFlag(QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
item.setFlag(QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
item.setFlag(QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemIsFocusable)
scene.addItem(item)

view = QtWidgets.QGraphicsView(scene)

box = QtWidgets.QVBoxLayout()
box.addWidget(view)
window.setLayout(box)

window.show()
sys.exit(app.exec())
