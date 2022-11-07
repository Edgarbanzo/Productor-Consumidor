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
from models.updateType import Updates as up

#Library Imports
import keyboard
from random import randint
from time import sleep

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
        self.firstProduct = 0
        self.productList = [False] * 25
        self.executeFlag = True
        
        self.prepareGrahpicsView()
        
        
    def startExecution(self):
        self.producer.setProduceItems(self.getRandNum())
        self.updateUI(up.PRODUCER)
        while(self.producer.isAvailable()):
            self.fillProducts()
            self.updateUI(up.PRODUCER)
            sleep(1)
            
        self.consumer.setRemainingTime(self.getRandTime())
        self.consumer.setConsumeItems(self.getRandNum())
        self.consumer.setLastItemIndex(self.firstProduct)
        self.updateUI(up.CONSUMER)
        self.producer.setRemainingTime(self.getRandTime())
        self.producer.setProduceItems(self.getRandNum())
        self.producer.setSleep(True)
        self.producer.setAvailability(False)
        self.updateUI(up.PRODUCER)
        self.updateUI(up.TIME)
        
        self.execution()
        
    def execution(self):
        while(self.executeFlag):
            #Tiempo del productor llega a 0
            if(not self.producer.isSleeping()):
                while(self.producer.isAvailable()):
                    self.fillProducts()
                    self.updateUI(up.PRODUCER)
                    sleep(1)
                self.producer.setRemainingTime(self.getRandTime())
                self.producer.setProduceItems(self.getRandNum())
                self.updateUI(up.PRODUCER)
            #Tiempo del consumidor llega a 0
            if(not self.consumer.isSleeping()):
                while(self.consumer.isAvailable()):
                    self.consumeProduct(self.consumer.getLastItemIndex())
                    self.updateUI(up.CONSUMER)
                    sleep(1)
                self.firstProduct = self.producer.getLastItemIndex()
                self.consumer.setRemainingTime(self.getRandTime())
                self.consumer.setConsumeItems(self.getRandNum())
                self.updateUI(up.CONSUMER)
            self.producer.update()
            self.consumer.update()
            self.updateUI(up.TIME)
            sleep(1)
        
    def stopExecution(self):
        self.executeFlag = False
        
    def consumeProduct(self,indx: int):
        index = indx
        
        if(not self.consumer.isAvailable()):
            return
        if(not self.productList[index]):
            self.consumer.setConsumeItems(0)
            self.consumer.update()
            return
        if(index == 0):
            
            self.graphicsView_1.setVisible(False)
            
        elif(index == 1):
            self.graphicsView_2.setVisible(False)
            
        elif(index == 2):
            self.graphicsView_3.setVisible(False)
            
        elif(index == 3):
            self.graphicsView_4.setVisible(False)
            
        elif(index == 4):
            self.graphicsView_5.setVisible(False)
            
        elif(index == 5):
            self.graphicsView_6.setVisible(False)
            
        elif(index == 6):
            self.graphicsView_7.setVisible(False)
            
        elif(index == 7):
            self.graphicsView_8.setVisible(False)
            
        elif(index == 8):
            self.graphicsView_9.setVisible(False)
            
        elif(index == 9):
            self.graphicsView_10.setVisible(False)
            
        elif(index == 10):
            self.graphicsView_11.setVisible(False)
            
        elif(index == 11):
            self.graphicsView_12.setVisible(False)
            
        elif(index == 12):
            self.graphicsView_13.setVisible(False)
            
        elif(index == 13):
            self.graphicsView_14.setVisible(False)
            
        elif(index == 14):
            self.graphicsView_15.setVisible(False)
            
        elif(index == 15):
            self.graphicsView_16.setVisible(False)
            
        elif(index == 16):
            self.graphicsView_17.setVisible(False)
            
        elif(index == 17):
            self.graphicsView_18.setVisible(False)
            
        elif(index == 18):
            self.graphicsView_19.setVisible(False)
            
        elif(index == 19):
            self.graphicsView_20.setVisible(False)
            
        elif(index == 20):
            self.graphicsView_21.setVisible(False)
            
        elif(index == 21):
            self.graphicsView_22.setVisible(False)
            
        elif(index == 22):
            self.graphicsView_23.setVisible(False)
            
        elif(index == 23):
            self.graphicsView_24.setVisible(False)
            
        elif(index == 24):
            self.graphicsView_25.setVisible(False)
        
        self.productList[index] = False
        self.consumer.update()
        return
    
    def updateUI(self, uiUpdate: int) -> None:
        if(uiUpdate == up.TIME):
            self.textBox_StatusProductor_2.setText(str(self.producer.getRemainingTime()))
            self.textBox_TiempoConsumidor.setText(str(self.consumer.getRemainingTime()))
        if(uiUpdate == up.PRODUCER):
            if(self.producer.isSleeping()):
                self.labelZProductor.setVisible(True)
                self.textBox_StatusProductor.setText("Durmiendo")
            else:
                self.labelZProductor.setVisible(False)
                self.textBox_StatusProductor.setText("Produciendo")
            self.textBox_ProductosProductor.setText(str(self.producer.getProduceItems()))
        if(uiUpdate == up.CONSUMER):
            if(self.consumer.isSleeping()):
                self.label_ZConsumidor.setVisible(True)
                self.textBox_StatusConsumer.setText("Durmiendo")
            else:
                self.label_ZConsumidor.setVisible(False)
                self.textBox_StatusConsumer.setText("Consumiendo")
            self.textBox_TiempoConsumidor_2.setText(str(self.consumer.getConsumeItems()))
        if(uiUpdate == up.END):
            pass
        QCoreApplication.processEvents()
    
    def fillProducts(self):
        index = self.producer.getLastItemIndex()
        if(not self.producer.isAvailable()):
            return
        if(index == 0):
            self.graphicsView_1.setVisible(True)
            
        elif(index == 1):
            self.graphicsView_2.setVisible(True)
            
        elif(index == 2):
            self.graphicsView_3.setVisible(True)
            
        elif(index == 3):
            self.graphicsView_4.setVisible(True)
            
        elif(index == 4):
            self.graphicsView_5.setVisible(True)
            
        elif(index == 5):
            self.graphicsView_6.setVisible(True)
            
        elif(index == 6):
            self.graphicsView_7.setVisible(True)
            
        elif(index == 7):
            self.graphicsView_8.setVisible(True)
            
        elif(index == 8):
            self.graphicsView_9.setVisible(True)
            
        elif(index == 9):
            self.graphicsView_10.setVisible(True)
            
        elif(index == 10):
            self.graphicsView_11.setVisible(True)
            
        elif(index == 11):
            self.graphicsView_12.setVisible(True)
            
        elif(index == 12):
            self.graphicsView_13.setVisible(True)
            
        elif(index == 13):
            self.graphicsView_14.setVisible(True)
            
        elif(index == 14):
            self.graphicsView_15.setVisible(True)
            
        elif(index == 15):
            self.graphicsView_16.setVisible(True)
            
        elif(index == 16):
            self.graphicsView_17.setVisible(True)
            
        elif(index == 17):
            self.graphicsView_18.setVisible(True)
            
        elif(index == 18):
            self.graphicsView_19.setVisible(True)
            
        elif(index == 19):
            self.graphicsView_20.setVisible(True)
            
        elif(index == 20):
            self.graphicsView_21.setVisible(True)
            
        elif(index == 21):
            self.graphicsView_22.setVisible(True)
            
        elif(index == 22):
            self.graphicsView_23.setVisible(True)
            
        elif(index == 23):
            self.graphicsView_24.setVisible(True)
            
        elif(index == 24):
            self.graphicsView_25.setVisible(True)
        
        self.productList[index] = True
        self.producer.update()
        return
    
    def getRandTime(self):
        return randint(2, 10)
    
    def getRandNum(self) -> int:
        return randint(2,5)
    
    def onKeyPressed(self, event):
        try:
            option = str(event.name).lower()
            if(option == "esc"):
                self.stopExecution()
            elif(option == "c"):
                self.executeFlag = True
                self.execution()
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