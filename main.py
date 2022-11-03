# Arrglar scroll
from PySide6.QtWidgets import QApplication

from view.ui_mainWindow import Ui_MainWindow as MainForm
import sys

if __name__ == '__main__':
    # Aplicación de Qt
    app = QApplication()
    window =  MainForm()
    # Se hace visible el botón
    window.show()
    # Qt loopb
    sys.exit(app.exec()) 



