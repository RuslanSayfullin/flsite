import pytest
from PyQt5.QtWidgets import QApplication
from main import FileExplorer

@pytest.fixture
def app():
    application = QApplication([])
    yield application
    application.quit()

@pytest.fixture
def file_explorer(app):
    explorer = FileExplorer()
    yield explorer

def test_initial_state(file_explorer):
    assert file_explorer.windowTitle() == "Проводник"
    assert file_explorer.geometry() == QRect(100, 100, 800, 600)
    assert file_explorer.tree_view.model().rootPath() == ""

def test_file_explorer_navigation(file_explorer):
    # TODO: Implement navigation tests
    pass

def test_file_explorer_open_file(file_explorer):
    # TODO: Implement open file tests
    pass