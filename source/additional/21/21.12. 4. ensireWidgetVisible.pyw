from PyQt6 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)
scrollArea = QtWidgets.QScrollArea()
scrollArea.setWindowTitle("Класс QScrollArea")
scrollArea.resize(300, 200)
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
scrollArea.show()
scrollArea.ensureWidgetVisible(label2, yMargin=50)
sys.exit(app.exec())
