# QT Imports
from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QMessageBox, QTableWidgetItem
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QTimer, QCoreApplication

#UI Imports
from view.ui_mainWindow import Ui_MainWindow as MainWindow

class MainForm(QMainWindow, MainWindow):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Productor Consumidor")