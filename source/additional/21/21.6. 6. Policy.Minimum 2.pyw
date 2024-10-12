from PyQt6 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("QSizePolicy")
window.resize(300, 150)
label = QtWidgets.QLabel("Текст надписи")
label2 = QtWidgets.QLabel("Текст надписи")

policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, 
                               QtWidgets.QSizePolicy.Policy.Minimum)
label.setFrameStyle(QtWidgets.QFrame.Shape.Box |
                    QtWidgets.QFrame.Shadow.Plain)
label.setSizePolicy(policy)

vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(label)
vbox.addWidget(label2)
window.setLayout(vbox)
window.show()
sys.exit(app.exec())
