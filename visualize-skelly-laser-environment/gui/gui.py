import logging

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QMainWindow, QLabel

from visualize-skelly-laser-environment.gui.widgets.run_button_widget import RunButtonWidget

logger = logging.getLogger(__name__)
class MainWindow(QMainWindow):
    def __init__(self):
        logger.info("Initializing the main window")
        super().__init__()

        self.setGeometry(100, 100, 600, 600)

        widget = QWidget()
        self._layout = QVBoxLayout()
        self._layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        widget.setLayout(self._layout)
        self.setCentralWidget(widget)

        self.folder_open_button = QPushButton('Load a folder')
        self._layout.addWidget(self.folder_open_button)
        self.folder_open_button.clicked.connect(self._open_session_folder_dialog)

        self._path_to_folder_label = QLabel("No folder selected")
        self._layout.addWidget(self._path_to_folder_label)

        self.run_button = RunButtonWidget(self)
        self._layout.addWidget(self.run_button)

    def _open_session_folder_dialog(self):
        self._folder_path = QFileDialog.getExistingDirectory(None, "Choose a folder")
        self._path_to_folder_label.setText(self._folder_path)




def run_gui_window():
    app = QApplication([])
    win = MainWindow()
    win.show()
    app.exec()


if __name__ == "__main__":
    run_gui_window()
