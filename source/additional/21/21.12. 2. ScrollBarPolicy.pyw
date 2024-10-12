from PyQt6 import QtCore, QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QScrollArea")
window.resize(350, 200)
scrollArea = QtWidgets.QScrollArea()
widget = QtWidgets.QWidget()
label1 = QtWidgets.QLabel("Содержимое компонента 1")
label2 = QtWidgets.QLabel("Содержимое компонента 2")
label1.setFrameStyle(QtWidgets.QFrame.Shape.Box |
                     QtWidgets.QFrame.Shadow.Plain)
label2.setFrameStyle(QtWidgets.QFrame.Shape.Box |
                     QtWidgets.QFrame.Shadow.Plain)
label1.setMinimumSize(350, 150)
label2.setMinimumHeight(80)
vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(label1)
vbox.addWidget(label2)
widget.setLayout(vbox)
scrollArea.setWidget(widget)
scrollArea.setHorizontalScrollBarPolicy(
              QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
scrollArea.setVerticalScrollBarPolicy(
              QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
mainbox = QtWidgets.QVBoxLayout()
mainbox.addWidget(scrollArea)
window.setLayout(mainbox)
window.show()
sys.exit(app.exec())
