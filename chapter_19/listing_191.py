from PyQt6 import QtWidgets
import sys

# Создание и отображение окна
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()            # Создаём окно
window.setWindowTitle("Зоголовок окна") # Указываем зоголовок
window.resize(300, 50)                  # Минимальные размеры
window.show()                           # Отображает окно
sys.exit(app.exec())