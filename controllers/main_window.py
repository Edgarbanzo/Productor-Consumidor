# Deben manejarse tiempos aleatorios para dormir al productor y al consumidor
# Cuando se les acaba el tiempo de sueño, realizan su actividad en 1 s.

# QT Imports
from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QMessageBox, QTableWidgetItem, QGraphicsScene
from PySide6.QtCore import QTimer, QCoreApplication, QRectF
from PySide6.QtGui import *

#UI Imports
from view.ui_mainWindow import Ui_MainWindow as MainWindow

#Model Imports
from models.consumer import Consumer
from models.producer import Producer

#Library Imports
import keyboard
from random import randint

class MainForm(QMainWindow, MainWindow):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Productor Consumidor")
        self.labelZProductor.setVisible(False)
        self.label_ZConsumidor.setVisible(False)
        
        #Connections
        keyboard.on_press(self.onKeyPressed)
        self.pushButton_Start.clicked.connect(self.startExecution)
        
        #Variables
        self.producer = Producer()
        self.consumer = Consumer()
        self.productsLit = []
        
        self.startExecution()
        
        
        
    def startExecution(self):
        self.producer.setProduceItems(self.getRandNum())
        self.consumer.setRemainingTime(self.getRandTime())
        self.prepareGrahpicsView()
        
    
    def stopExecution(self):
        pass
    
    def fillProducts(self):
        index = self.producer.getLastItemIndex()
        if(index == 0):
            self.graphicsView_1.setVisible(True)
        
    
        
    def getRandTime(self):
        return randint(1, 10)
    
    def getRandNum(self) -> int:
        return randint(2,5)
    
    def onKeyPressed(self, event):
        try:
            option = str(event.name).lower()
            if(option == "esc"):
                self.stopExecution()
        except:
            pass
    
    def prepareGrahpicsView(self):
        scene = QGraphicsScene()
        scene.addPixmap(QPixmap("images/Fruit.png"))
        self.graphicsView_1.setScene(scene)
        self.graphicsView_1.scale(0.035,0.035)
        self.graphicsView_2.setScene(scene)
        self.graphicsView_2.scale(0.035,0.035)
        self.graphicsView_3.setScene(scene)
        self.graphicsView_3.scale(0.035,0.035)
        self.graphicsView_4.setScene(scene)
        self.graphicsView_4.scale(0.035,0.035)
        self.graphicsView_5.setScene(scene)
        self.graphicsView_5.scale(0.035,0.035)
        self.graphicsView_6.setScene(scene)
        self.graphicsView_6.scale(0.035,0.035)
        self.graphicsView_7.setScene(scene)
        self.graphicsView_7.scale(0.035,0.035)
        self.graphicsView_8.setScene(scene)
        self.graphicsView_8.scale(0.035,0.035)
        self.graphicsView_9.setScene(scene)
        self.graphicsView_9.scale(0.035,0.035)
        self.graphicsView_10.setScene(scene)
        self.graphicsView_11.setScene(scene)
        self.graphicsView_12.setScene(scene)
        self.graphicsView_13.setScene(scene)
        self.graphicsView_14.setScene(scene)
        self.graphicsView_15.setScene(scene)
        self.graphicsView_16.setScene(scene)
        self.graphicsView_17.setScene(scene)
        self.graphicsView_18.setScene(scene)
        self.graphicsView_19.setScene(scene)
        self.graphicsView_20.setScene(scene)
        self.graphicsView_21.setScene(scene)
        self.graphicsView_22.setScene(scene)
        self.graphicsView_23.setScene(scene)
        self.graphicsView_24.setScene(scene)
        self.graphicsView_25.setScene(scene)
        self.graphicsView_10.scale(0.035,0.035)
        self.graphicsView_11.scale(0.035,0.035)
        self.graphicsView_12.scale(0.035,0.035)
        self.graphicsView_13.scale(0.035,0.035)
        self.graphicsView_14.scale(0.035,0.035)
        self.graphicsView_15.scale(0.035,0.035)
        self.graphicsView_16.scale(0.035,0.035)
        self.graphicsView_17.scale(0.035,0.035)
        self.graphicsView_18.scale(0.035,0.035)
        self.graphicsView_19.scale(0.035,0.035)
        self.graphicsView_20.scale(0.035,0.035)
        self.graphicsView_21.scale(0.035,0.035)
        self.graphicsView_22.scale(0.035,0.035)
        self.graphicsView_23.scale(0.035,0.035)
        self.graphicsView_24.scale(0.035,0.035)
        self.graphicsView_25.scale(0.035,0.035)
        scene.update()
        self.graphicsView_1.setVisible(False)
        self.graphicsView_2.setVisible(False)
        self.graphicsView_3.setVisible(False)
        self.graphicsView_4.setVisible(False)
        self.graphicsView_5.setVisible(False)
        self.graphicsView_6.setVisible(False)
        self.graphicsView_7.setVisible(False)
        self.graphicsView_8.setVisible(False)
        self.graphicsView_9.setVisible(False)
        self.graphicsView_10.setVisible(False)
        self.graphicsView_11.setVisible(False)
        self.graphicsView_12.setVisible(False)
        self.graphicsView_13.setVisible(False)
        self.graphicsView_14.setVisible(False)
        self.graphicsView_15.setVisible(False)
        self.graphicsView_16.setVisible(False)
        self.graphicsView_17.setVisible(False)
        self.graphicsView_18.setVisible(False)
        self.graphicsView_19.setVisible(False)
        self.graphicsView_20.setVisible(False)
        self.graphicsView_21.setVisible(False)
        self.graphicsView_22.setVisible(False)
        self.graphicsView_23.setVisible(False)
        self.graphicsView_24.setVisible(False)
        self.graphicsView_25.setVisible(False)