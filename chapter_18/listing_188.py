from PyQt6 import QtWidgets
import sys
from ui_MyForm import Ui_MyForm

# Использование сгенерированного класса формы
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
ui = ui_MyForm.Ui_MyForm()
ui.setupUi(window)
ui.btnQuit.clicked.connect(QtWidgets.QApplication.instance().quit)
window.show()
sys.exit(app.exec())
