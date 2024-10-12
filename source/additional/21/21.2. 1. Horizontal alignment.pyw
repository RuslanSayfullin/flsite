from PyQt6 import QtCore, QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Выравнивание по горизонтали")
window.resize(400, 50)
button1 = QtWidgets.QPushButton("Right")
button2 = QtWidgets.QPushButton("No")
button3 = QtWidgets.QPushButton("Left")
hbox = QtWidgets.QHBoxLayout()
hbox.addWidget(button1, alignment=QtCore.Qt.AlignmentFlag.AlignRight)
hbox.addWidget(button2)
hbox.addWidget(button3, alignment=QtCore.Qt.AlignmentFlag.AlignLeft)
window.setLayout(hbox)
window.show()
sys.exit(app.exec())
