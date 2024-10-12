from PyQt6 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("QSizePolicy")
window.resize(300, 150)
label = QtWidgets.QLabel("Текст надписи")
button = QtWidgets.QPushButton("1")

policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, 
                               QtWidgets.QSizePolicy.Policy.Minimum)
label.setFrameStyle(QtWidgets.QFrame.Shape.Box |
                    QtWidgets.QFrame.Shadow.Plain)
label.setSizePolicy(policy)

vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(label)
vbox.addWidget(button)
window.setLayout(vbox)
window.show()
sys.exit(app.exec())
