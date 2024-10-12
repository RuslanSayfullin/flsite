from PyQt6 import QtCore, QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QGroupBox")
window.resize(300, 80)
radio1 = QtWidgets.QRadioButton("&Да")
radio2 = QtWidgets.QRadioButton("&Нет")
mainbox = QtWidgets.QVBoxLayout()
box = QtWidgets.QGroupBox()
box.setTitle("&Вы знаете язык Python?")
#box.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
#box.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
box.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
hbox = QtWidgets.QHBoxLayout()
hbox.addWidget(radio1)
hbox.addWidget(radio2)
box.setLayout(hbox)
mainbox.addWidget(box)
window.setLayout(mainbox)
radio1.setChecked(True)
window.show()
sys.exit(app.exec())
