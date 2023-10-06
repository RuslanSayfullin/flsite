# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("QGroupBox")
window.resize(200, 80)
mainbox = QtWidgets.QVBoxLayout()
radio1 = QtWidgets.QRadioButton("&Да")
radio2 = QtWidgets.QRadioButton("&Нет")
box = QtWidgets.QGroupBox("&Вы знаете язык Python?") # Объект группы
hbox = QtWidgets.QHBoxLayout()      # Контейнер для группы
# Добавляем компоненты
hbox.addWidget(radio1)
hbox.addWidget(radio2)
# Передаем ссылку на контейнер
box.setLayout(hbox)
# Добавляем группу в главный контейнер
mainbox.addWidget(box)
# Передаем ссылку на главный контейнер в окно
window.setLayout(mainbox)
# Выбираем первый переключатель
radio1.setChecked(True)
window.show()
sys.exit(app.exec_())