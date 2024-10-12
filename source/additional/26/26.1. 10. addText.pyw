from PyQt6 import QtCore, QtWidgets, QtGui
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QGraphicsScene")
window.resize(600, 400)

scene = QtWidgets.QGraphicsScene(0.0, 0.0, 500.0, 335.0)
scene.setBackgroundBrush(QtCore.Qt.GlobalColor.white)

scene.addSimpleText("Простой текст", QtGui.QFont("Verdana", 25))
txt = scene.addText("Простой текст", QtGui.QFont("Verdana", 25))
txt.setPos(QtCore.QPointF(0.0, 150.0))

view = QtWidgets.QGraphicsView(scene)

box = QtWidgets.QVBoxLayout()
box.addWidget(view)
window.setLayout(box)

window.show()
sys.exit(app.exec())
