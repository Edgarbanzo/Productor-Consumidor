# Arrglar scroll
from PySide6.QtWidgets import QApplication

from controllers.main_window import MainForm 
from controllers.table_bcp import BCP_table
import sys

if __name__ == '__main__':
    # Aplicación de Qt
    app = QApplication()
    window =  MainForm()
    # Se hace visible el botón
    window.show()
    # Qt loopb
    sys.exit(app.exec()) 



