# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGraphicsView, QGroupBox,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)
import consumer_rc
import productor_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"background-color: rgb(40,43,48);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBoxMid = QGroupBox(self.centralwidget)
        self.groupBoxMid.setObjectName(u"groupBoxMid")
        self.groupBoxMid.setGeometry(QRect(270, 10, 301, 531))
        self.groupBoxMid.setCursor(QCursor(Qt.ArrowCursor))
        self.pushButton_Start = QPushButton(self.groupBoxMid)
        self.pushButton_Start.setObjectName(u"pushButton_Start")
        self.pushButton_Start.setGeometry(QRect(40, 430, 201, 61))
        self.pushButton_Start.setStyleSheet(u"background-color: rgb(0, 153, 117);\n"
"font: 19pt \"Impact\";\n"
"color: #FFFFFF;\n"
"border-radius: 10px;")
        self.label_titulo_Process = QLabel(self.groupBoxMid)
        self.label_titulo_Process.setObjectName(u"label_titulo_Process")
        self.label_titulo_Process.setGeometry(QRect(110, 30, 91, 31))
        self.label_titulo_Process.setStyleSheet(u"color:rgb(0, 153, 117);\n"
"font: 87 14pt \"Segoe UI Black\";\n"
"")
        self.groupBox_ProcessContainer = QGroupBox(self.groupBoxMid)
        self.groupBox_ProcessContainer.setObjectName(u"groupBox_ProcessContainer")
        self.groupBox_ProcessContainer.setGeometry(QRect(30, 80, 221, 321))
        self.graphicsView_1 = QGraphicsView(self.groupBox_ProcessContainer)
        self.graphicsView_1.setObjectName(u"graphicsView_1")
        self.graphicsView_1.setGeometry(QRect(10, 30, 31, 31))
        self.graphicsView_3 = QGraphicsView(self.groupBox_ProcessContainer)
        self.graphicsView_3.setObjectName(u"graphicsView_3")
        self.graphicsView_3.setGeometry(QRect(90, 30, 31, 31))
        self.graphicsView_4 = QGraphicsView(self.groupBox_ProcessContainer)
        self.graphicsView_4.setObjectName(u"graphicsView_4")
        self.graphicsView_4.setGeometry(QRect(130, 30, 31, 31))
        self.graphicsView_5 = QGraphicsView(self.groupBox_ProcessContainer)
        self.graphicsView_5.setObjectName(u"graphicsView_5")
        self.graphicsView_5.setGeometry(QRect(170, 30, 31, 31))
        self.graphicsView_6 = QGraphicsView(self.groupBox_ProcessContainer)
        self.graphicsView_6.setObjectName(u"graphicsView_6")
        self.graphicsView_6.setGeometry(QRect(10, 90, 31, 31))
        self.graphicsView_7 = QGraphicsView(self.groupBox_ProcessContainer)
        self.graphicsView_7.setObjectName(u"graphicsView_7")
        self.graphicsView_7.setGeometry(QRect(10, 150, 31, 31))
        self.graphicsView_8 = QGraphicsView(self.groupBox_ProcessContainer)
        self.graphicsView_8.setObjectName(u"graphicsView_8")
        self.graphicsView_8.setGeometry(QRect(10, 210, 31, 31))
        self.graphicsView_9 = QGraphicsView(self.groupBox_ProcessContainer)
        self.graphicsView_9.setObjectName(u"graphicsView_9")
        self.graphicsView_9.setGeometry(QRect(10, 270, 31, 31))
        self.graphicsView_10 = QGraphicsView(self.groupBox_ProcessContainer)
        self.graphicsView_10.setObjectName(u"graphicsView_10")
        self.graphicsView_10.setGeometry(QRect(50, 90, 31, 31))
        self.graphicsView_11 = QGraphicsView(self.groupBox_ProcessContainer)
        self.graphicsView_11.setObjectName(u"graphicsView_11")
        self.graphicsView_11.setGeometry(QRect(50, 150, 31, 31))
        self.graphicsView_12 = QGraphicsView(self.groupBox_ProcessContainer)
        self.graphicsView_12.setObjectName(u"graphicsView_12")
        self.graphicsView_12.setGeometry(QRect(50, 210, 31, 31))
        self.graphicsView_13 = QGraphicsView(self.groupBox_ProcessContainer)
        self.graphicsView_13.setObjectName(u"graphicsView_13")
        self.graphicsView_13.setGeometry(QRect(90, 90, 31, 31))
        self.graphicsView_14 = QGraphicsView(self.groupBox_ProcessContainer)
        self.graphicsView_14.setObjectName(u"graphicsView_14")
        self.graphicsView_14.setGeometry(QRect(130, 90, 31, 31))
        self.graphicsView_15 = QGraphicsView(self.groupBox_ProcessContainer)
        self.graphicsView_15.setObjectName(u"graphicsView_15")
        self.graphicsView_15.setGeometry(QRect(170, 90, 31, 31))
        self.graphicsView_16 = QGraphicsView(self.groupBox_ProcessContainer)
        self.graphicsView_16.setObjectName(u"graphicsView_16")
        self.graphicsView_16.setGeometry(QRect(90, 150, 31, 31))
        self.graphicsView_17 = QGraphicsView(self.groupBox_ProcessContainer)
        self.graphicsView_17.setObjectName(u"graphicsView_17")
        self.graphicsView_17.setGeometry(QRect(130, 150, 31, 31))
        self.graphicsView_18 = QGraphicsView(self.groupBox_ProcessContainer)
        self.graphicsView_18.setObjectName(u"graphicsView_18")
        self.graphicsView_18.setGeometry(QRect(170, 150, 31, 31))
        self.graphicsView_19 = QGraphicsView(self.groupBox_ProcessContainer)
        self.graphicsView_19.setObjectName(u"graphicsView_19")
        self.graphicsView_19.setGeometry(QRect(90, 210, 31, 31))
        self.graphicsView_20 = QGraphicsView(self.groupBox_ProcessContainer)
        self.graphicsView_20.setObjectName(u"graphicsView_20")
        self.graphicsView_20.setGeometry(QRect(130, 210, 31, 31))
        self.graphicsView_21 = QGraphicsView(self.groupBox_ProcessContainer)
        self.graphicsView_21.setObjectName(u"graphicsView_21")
        self.graphicsView_21.setGeometry(QRect(170, 210, 31, 31))
        self.graphicsView_22 = QGraphicsView(self.groupBox_ProcessContainer)
        self.graphicsView_22.setObjectName(u"graphicsView_22")
        self.graphicsView_22.setGeometry(QRect(50, 270, 31, 31))
        self.graphicsView_23 = QGraphicsView(self.groupBox_ProcessContainer)
        self.graphicsView_23.setObjectName(u"graphicsView_23")
        self.graphicsView_23.setGeometry(QRect(90, 270, 31, 31))
        self.graphicsView_24 = QGraphicsView(self.groupBox_ProcessContainer)
        self.graphicsView_24.setObjectName(u"graphicsView_24")
        self.graphicsView_24.setGeometry(QRect(130, 270, 31, 31))
        self.graphicsView_25 = QGraphicsView(self.groupBox_ProcessContainer)
        self.graphicsView_25.setObjectName(u"graphicsView_25")
        self.graphicsView_25.setGeometry(QRect(170, 270, 31, 31))
        self.label_1 = QLabel(self.groupBox_ProcessContainer)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setGeometry(QRect(20, 10, 21, 20))
        self.label_1.setAutoFillBackground(False)
        self.label_1.setStyleSheet(u"color: rgb(255, 255, 255)")
        self.label_1.setScaledContents(True)
        self.label_2 = QLabel(self.groupBox_ProcessContainer)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 10, 16, 21))
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255)")
        self.label_2.setScaledContents(True)
        self.label_3 = QLabel(self.groupBox_ProcessContainer)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setEnabled(True)
        self.label_3.setGeometry(QRect(100, 10, 16, 21))
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255)")
        self.label_3.setFrameShadow(QFrame.Raised)
        self.label_3.setLineWidth(0)
        self.label_3.setText(u"3")
        self.label_3.setTextFormat(Qt.PlainText)
        self.label_3.setScaledContents(True)
        self.label_3.setWordWrap(False)
        self.label_3.setIndent(4)
        self.label_4 = QLabel(self.groupBox_ProcessContainer)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(140, 10, 20, 21))
        self.label_4.setAutoFillBackground(False)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255)")
        self.label_4.setTextFormat(Qt.MarkdownText)
        self.label_4.setScaledContents(True)
        self.label_5 = QLabel(self.groupBox_ProcessContainer)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(180, 10, 20, 21))
        self.label_5.setAutoFillBackground(False)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255)")
        self.label_5.setScaledContents(True)
        self.label_6 = QLabel(self.groupBox_ProcessContainer)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 70, 20, 21))
        self.label_6.setAutoFillBackground(False)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255)")
        self.label_6.setScaledContents(True)
        self.label_7 = QLabel(self.groupBox_ProcessContainer)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(60, 70, 20, 21))
        self.label_7.setAutoFillBackground(False)
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255)")
        self.label_7.setScaledContents(True)
        self.label_8 = QLabel(self.groupBox_ProcessContainer)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(100, 70, 20, 21))
        self.label_8.setAutoFillBackground(False)
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255)")
        self.label_8.setScaledContents(True)
        self.label_9 = QLabel(self.groupBox_ProcessContainer)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(140, 70, 20, 21))
        self.label_9.setAutoFillBackground(False)
        self.label_9.setStyleSheet(u"color: rgb(255, 255, 255)")
        self.label_9.setScaledContents(True)
        self.label_10 = QLabel(self.groupBox_ProcessContainer)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(180, 70, 20, 21))
        self.label_10.setAutoFillBackground(False)
        self.label_10.setStyleSheet(u"color: rgb(255, 255, 255)")
        self.label_10.setScaledContents(True)
        self.label_11 = QLabel(self.groupBox_ProcessContainer)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(20, 130, 20, 21))
        self.label_11.setAutoFillBackground(False)
        self.label_11.setStyleSheet(u"color: rgb(255, 255, 255)")
        self.label_11.setScaledContents(True)
        self.label_12 = QLabel(self.groupBox_ProcessContainer)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(60, 130, 20, 21))
        self.label_12.setAutoFillBackground(False)
        self.label_12.setStyleSheet(u"color: rgb(255, 255, 255)")
        self.label_12.setScaledContents(True)
        self.label_13 = QLabel(self.groupBox_ProcessContainer)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(100, 130, 20, 21))
        self.label_13.setAutoFillBackground(False)
        self.label_13.setStyleSheet(u"color: rgb(255, 255, 255)")
        self.label_13.setScaledContents(True)
        self.label_14 = QLabel(self.groupBox_ProcessContainer)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(140, 130, 20, 21))
        self.label_14.setAutoFillBackground(False)
        self.label_14.setStyleSheet(u"color: rgb(255, 255, 255)")
        self.label_14.setScaledContents(True)
        self.label_15 = QLabel(self.groupBox_ProcessContainer)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(180, 130, 16, 21))
        self.label_15.setAutoFillBackground(False)
        self.label_15.setStyleSheet(u"color: rgb(255, 255, 255)")
        self.label_15.setScaledContents(True)
        self.label_16 = QLabel(self.groupBox_ProcessContainer)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(20, 190, 20, 21))
        self.label_16.setAutoFillBackground(False)
        self.label_16.setStyleSheet(u"color: rgb(255, 255, 255)")
        self.label_16.setScaledContents(True)
        self.label_17 = QLabel(self.groupBox_ProcessContainer)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(60, 190, 20, 21))
        self.label_17.setAutoFillBackground(False)
        self.label_17.setStyleSheet(u"color: rgb(255, 255, 255)")
        self.label_17.setScaledContents(True)
        self.label_18 = QLabel(self.groupBox_ProcessContainer)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(100, 190, 20, 21))
        self.label_18.setAutoFillBackground(False)
        self.label_18.setStyleSheet(u"color: rgb(255, 255, 255)")
        self.label_18.setScaledContents(True)
        self.label_19 = QLabel(self.groupBox_ProcessContainer)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(140, 190, 20, 21))
        self.label_19.setAutoFillBackground(False)
        self.label_19.setStyleSheet(u"color: rgb(255, 255, 255)")
        self.label_19.setScaledContents(True)
        self.label_20 = QLabel(self.groupBox_ProcessContainer)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(180, 190, 20, 21))
        self.label_20.setAutoFillBackground(False)
        self.label_20.setStyleSheet(u"color: rgb(255, 255, 255)")
        self.label_20.setScaledContents(True)
        self.label_21 = QLabel(self.groupBox_ProcessContainer)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(20, 250, 20, 21))
        self.label_21.setAutoFillBackground(False)
        self.label_21.setStyleSheet(u"color: rgb(255, 255, 255)")
        self.label_21.setScaledContents(True)
        self.label_22 = QLabel(self.groupBox_ProcessContainer)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(60, 250, 20, 21))
        self.label_22.setAutoFillBackground(False)
        self.label_22.setStyleSheet(u"color: rgb(255, 255, 255)")
        self.label_22.setScaledContents(True)
        self.label_23 = QLabel(self.groupBox_ProcessContainer)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(100, 250, 20, 21))
        self.label_23.setAutoFillBackground(False)
        self.label_23.setStyleSheet(u"color: rgb(255, 255, 255)")
        self.label_23.setScaledContents(True)
        self.label_24 = QLabel(self.groupBox_ProcessContainer)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(140, 250, 21, 21))
        self.label_24.setAutoFillBackground(False)
        self.label_24.setStyleSheet(u"color: rgb(255, 255, 255)")
        self.label_24.setScaledContents(True)
        self.label_25 = QLabel(self.groupBox_ProcessContainer)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(180, 250, 20, 21))
        self.label_25.setAutoFillBackground(False)
        self.label_25.setStyleSheet(u"color: rgb(255, 255, 255)")
        self.label_25.setScaledContents(True)
        self.graphicsView_2 = QGraphicsView(self.groupBox_ProcessContainer)
        self.graphicsView_2.setObjectName(u"graphicsView_2")
        self.graphicsView_2.setGeometry(QRect(50, 30, 31, 31))
        self.label_25.raise_()
        self.label_24.raise_()
        self.label_23.raise_()
        self.label_22.raise_()
        self.label_21.raise_()
        self.label_20.raise_()
        self.label_19.raise_()
        self.label_18.raise_()
        self.label_17.raise_()
        self.label_16.raise_()
        self.label_15.raise_()
        self.label_14.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.label_11.raise_()
        self.label_10.raise_()
        self.label_9.raise_()
        self.label_8.raise_()
        self.label_7.raise_()
        self.label_6.raise_()
        self.label_5.raise_()
        self.label_4.raise_()
        self.label_3.raise_()
        self.graphicsView_1.raise_()
        self.graphicsView_3.raise_()
        self.graphicsView_4.raise_()
        self.graphicsView_5.raise_()
        self.graphicsView_6.raise_()
        self.graphicsView_7.raise_()
        self.graphicsView_8.raise_()
        self.graphicsView_9.raise_()
        self.graphicsView_10.raise_()
        self.graphicsView_11.raise_()
        self.graphicsView_12.raise_()
        self.graphicsView_13.raise_()
        self.graphicsView_14.raise_()
        self.graphicsView_15.raise_()
        self.graphicsView_16.raise_()
        self.graphicsView_17.raise_()
        self.graphicsView_18.raise_()
        self.graphicsView_19.raise_()
        self.graphicsView_20.raise_()
        self.graphicsView_21.raise_()
        self.graphicsView_22.raise_()
        self.graphicsView_23.raise_()
        self.graphicsView_24.raise_()
        self.graphicsView_25.raise_()
        self.label_1.raise_()
        self.label_2.raise_()
        self.graphicsView_2.raise_()
        self.groupBoxFirst = QGroupBox(self.centralwidget)
        self.groupBoxFirst.setObjectName(u"groupBoxFirst")
        self.groupBoxFirst.setGeometry(QRect(10, 10, 261, 531))
        self.textBox_StatusProductor = QLineEdit(self.groupBoxFirst)
        self.textBox_StatusProductor.setObjectName(u"textBox_StatusProductor")
        self.textBox_StatusProductor.setGeometry(QRect(30, 310, 171, 81))
        self.textBox_StatusProductor.setMinimumSize(QSize(60, 35))
        self.textBox_StatusProductor.setTabletTracking(True)
        self.textBox_StatusProductor.setAutoFillBackground(False)
        self.textBox_StatusProductor.setStyleSheet(u"background-color: rgb(52, 62, 64);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(0, 153, 117);\n"
"border-radius: 4px;")
        self.label_Productor = QLabel(self.groupBoxFirst)
        self.label_Productor.setObjectName(u"label_Productor")
        self.label_Productor.setGeometry(QRect(80, 70, 101, 31))
        self.label_Productor.setStyleSheet(u"color:rgb(0, 153, 117);\n"
"font: 87 14pt \"Segoe UI Black\";\n"
"")
        self.imageProductorAwake = QLabel(self.groupBoxFirst)
        self.imageProductorAwake.setObjectName(u"imageProductorAwake")
        self.imageProductorAwake.setGeometry(QRect(50, 110, 151, 151))
        self.imageProductorAwake.setAutoFillBackground(False)
        self.imageProductorAwake.setStyleSheet(u"image: url(:/productorAwake/Productor.png);")
        self.imageProductorAwake.setPixmap(QPixmap(u":/productorAwake/Productor.png"))
        self.imageProductorAwake.setScaledContents(True)
        self.label_StatusProductor = QLabel(self.groupBoxFirst)
        self.label_StatusProductor.setObjectName(u"label_StatusProductor")
        self.label_StatusProductor.setGeometry(QRect(40, 290, 51, 16))
        self.label_StatusProductor.setStyleSheet(u"color:rgb(255, 255, 255);")
        self.groupBoxLast = QGroupBox(self.centralwidget)
        self.groupBoxLast.setObjectName(u"groupBoxLast")
        self.groupBoxLast.setGeometry(QRect(570, 10, 221, 531))
        self.label_tittleConsumer = QLabel(self.groupBoxLast)
        self.label_tittleConsumer.setObjectName(u"label_tittleConsumer")
        self.label_tittleConsumer.setGeometry(QRect(60, 60, 121, 31))
        self.label_tittleConsumer.setStyleSheet(u"color:rgb(0, 153, 117);\n"
"font: 87 14pt \"Segoe UI Black\";\n"
"")
        self.imageConsumerAwake = QLabel(self.groupBoxLast)
        self.imageConsumerAwake.setObjectName(u"imageConsumerAwake")
        self.imageConsumerAwake.setGeometry(QRect(40, 110, 151, 151))
        self.imageConsumerAwake.setAutoFillBackground(False)
        self.imageConsumerAwake.setStyleSheet(u"image:url(:/ConsumerAwake/Consumer.png);")
        self.imageConsumerAwake.setPixmap(QPixmap(u":/ConsumerAwake/Consumer.png"))
        self.imageConsumerAwake.setScaledContents(True)
        self.textBox_StatusConsumer = QLineEdit(self.groupBoxLast)
        self.textBox_StatusConsumer.setObjectName(u"textBox_StatusConsumer")
        self.textBox_StatusConsumer.setGeometry(QRect(30, 310, 171, 81))
        self.textBox_StatusConsumer.setMinimumSize(QSize(60, 35))
        self.textBox_StatusConsumer.setTabletTracking(True)
        self.textBox_StatusConsumer.setAutoFillBackground(False)
        self.textBox_StatusConsumer.setStyleSheet(u"background-color: rgb(52, 62, 64);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(0, 153, 117);\n"
"border-radius: 4px;")
        self.label_StatusConsumer = QLabel(self.groupBoxLast)
        self.label_StatusConsumer.setObjectName(u"label_StatusConsumer")
        self.label_StatusConsumer.setGeometry(QRect(50, 290, 51, 16))
        self.label_StatusConsumer.setStyleSheet(u"color:rgb(255, 255, 255);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBoxMid.setTitle("")
        self.pushButton_Start.setText(QCoreApplication.translate("MainWindow", u"Iniciar", None))
        self.label_titulo_Process.setText(QCoreApplication.translate("MainWindow", u"Procesos", None))
        self.groupBox_ProcessContainer.setTitle("")
        self.label_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"11", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"12", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"13", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"14", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"15", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"16", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"17", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"18", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"19", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"21", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"22", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"23", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"24", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"25", None))
        self.groupBoxFirst.setTitle("")
        self.textBox_StatusProductor.setText("")
        self.label_Productor.setText(QCoreApplication.translate("MainWindow", u"Productor", None))
        self.imageProductorAwake.setText("")
        self.label_StatusProductor.setText(QCoreApplication.translate("MainWindow", u"Estado:", None))
        self.groupBoxLast.setTitle("")
        self.label_tittleConsumer.setText(QCoreApplication.translate("MainWindow", u"Consumidor", None))
        self.imageConsumerAwake.setText("")
        self.textBox_StatusConsumer.setText("")
        self.label_StatusConsumer.setText(QCoreApplication.translate("MainWindow", u"Estado", None))
    # retranslateUi

