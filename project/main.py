import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeView, QFileSystemModel, QVBoxLayout, QWidget

class FileExplorer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Проводник")
        self.setGeometry(100, 100, 800, 600)

        self.tree_view = QTreeView(self)
        self.file_model = QFileSystemModel()
        self.file_model.setRootPath("")
        self.tree_view.setModel(self.file_model)
        self.tree_view.setRootIndex(self.file_model.index(os.path.expanduser("~")))  # Начальная директория

        layout = QVBoxLayout()
        layout.addWidget(self.tree_view)

        main_widget = QWidget()
        main_widget.setLayout(layout)
        self.setCentralWidget(main_widget)

        self.show()

app = QApplication(sys.argv)
explorer = FileExplorer()
sys.exit(app.exec_())
