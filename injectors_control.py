# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'injectors_control.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(521, 492)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(521, 492))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.CloseSerial = QtWidgets.QPushButton(self.centralwidget)
        self.CloseSerial.setEnabled(False)
        self.CloseSerial.setGeometry(QtCore.QRect(290, 10, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.CloseSerial.setFont(font)
        self.CloseSerial.setObjectName("CloseSerial")
        self.SerialStatusLabel = QtWidgets.QLabel(self.centralwidget)
        self.SerialStatusLabel.setGeometry(QtCore.QRect(20, 130, 191, 18))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.SerialStatusLabel.setFont(font)
        self.SerialStatusLabel.setObjectName("SerialStatusLabel")
        self.SerialStatus = QtWidgets.QLabel(self.centralwidget)
        self.SerialStatus.setGeometry(QtCore.QRect(210, 130, 31, 21))
        self.SerialStatus.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"border: 2px solid black;")
        self.SerialStatus.setText("")
        self.SerialStatus.setObjectName("SerialStatus")
        self.ComboSerial = QtWidgets.QComboBox(self.centralwidget)
        self.ComboSerial.setGeometry(QtCore.QRect(20, 10, 121, 41))
        self.ComboSerial.setObjectName("ComboSerial")
        self.OpenSerial = QtWidgets.QPushButton(self.centralwidget)
        self.OpenSerial.setGeometry(QtCore.QRect(150, 10, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.OpenSerial.setFont(font)
        self.OpenSerial.setFlat(False)
        self.OpenSerial.setObjectName("OpenSerial")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(20, 170, 481, 301))
        self.frame_3.setAutoFillBackground(True)
        self.frame_3.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame_3)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(100, 210, 281, 81))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.StartButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.StartButton.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StartButton.sizePolicy().hasHeightForWidth())
        self.StartButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.StartButton.setFont(font)
        self.StartButton.setStyleSheet("QPushButton{\n"
"border: 2px solid black;\n"
"border-radius: 10px;\n"
"background-color: rgb(209, 209, 209);\n"
"}\n"
"QPushButton:hover{\n"
"border: 2px solid black;\n"
"border-radius: 10px;\n"
"background-color:rgb(207, 238, 236);\n"
"}\n"
"QPushButton:checked{background-color:rgb(0,128,0); border: none}\n"
"")
        self.StartButton.setCheckable(False)
        self.StartButton.setObjectName("StartButton")
        self.horizontalLayout.addWidget(self.StartButton)
        self.StopButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.StopButton.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StopButton.sizePolicy().hasHeightForWidth())
        self.StopButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.StopButton.setFont(font)
        self.StopButton.setStyleSheet("QPushButton{\n"
"border: 2px solid black;\n"
"border-radius: 10px;\n"
"background-color: rgb(209, 209, 209);\n"
"}\n"
"QPushButton:hover{\n"
"border: 2px solid black;\n"
"border-radius: 10px;\n"
"background-color:rgb(207, 238, 236);\n"
"}\n"
"")
        self.StopButton.setObjectName("StopButton")
        self.horizontalLayout.addWidget(self.StopButton)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame_3)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 141, 91))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.FrequencyLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.FrequencyLabel.setFont(font)
        self.FrequencyLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.FrequencyLabel.setObjectName("FrequencyLabel")
        self.verticalLayout.addWidget(self.FrequencyLabel)
        self.FrequencyBox = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FrequencyBox.sizePolicy().hasHeightForWidth())
        self.FrequencyBox.setSizePolicy(sizePolicy)
        self.FrequencyBox.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.FrequencyBox.setFont(font)
        self.FrequencyBox.setMinimum(1)
        self.FrequencyBox.setMaximum(500)
        self.FrequencyBox.setProperty("value", 1)
        self.FrequencyBox.setObjectName("FrequencyBox")
        self.verticalLayout.addWidget(self.FrequencyBox)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.frame_3)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(19, 100, 141, 101))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.DutyLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.DutyLabel.setFont(font)
        self.DutyLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.DutyLabel.setObjectName("DutyLabel")
        self.verticalLayout_2.addWidget(self.DutyLabel)
        self.DutyBox = QtWidgets.QSpinBox(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DutyBox.sizePolicy().hasHeightForWidth())
        self.DutyBox.setSizePolicy(sizePolicy)
        self.DutyBox.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.DutyBox.setFont(font)
        self.DutyBox.setMinimum(0)
        self.DutyBox.setMaximum(100)
        self.DutyBox.setProperty("value", 0)
        self.DutyBox.setObjectName("DutyBox")
        self.verticalLayout_2.addWidget(self.DutyBox)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.frame_3)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(170, 10, 131, 191))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.FrequencyButton = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.FrequencyButton.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FrequencyButton.sizePolicy().hasHeightForWidth())
        self.FrequencyButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.FrequencyButton.setFont(font)
        self.FrequencyButton.setStyleSheet("QPushButton{\n"
"border: 2px solid black;\n"
"border-radius: 10px;\n"
"background-color: rgb(209, 209, 209);\n"
"}\n"
"QPushButton:hover{\n"
"border: 2px solid black;\n"
"border-radius: 10px;\n"
"background-color:rgb(207, 238, 236);\n"
"}\n"
"QPushButton:checked{background-color:rgb(0,128,0); border: none}\n"
"")
        self.FrequencyButton.setCheckable(False)
        self.FrequencyButton.setObjectName("FrequencyButton")
        self.verticalLayout_3.addWidget(self.FrequencyButton)
        self.DutyButton = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.DutyButton.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DutyButton.sizePolicy().hasHeightForWidth())
        self.DutyButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.DutyButton.setFont(font)
        self.DutyButton.setStyleSheet("QPushButton{\n"
"border: 2px solid black;\n"
"border-radius: 10px;\n"
"background-color: rgb(209, 209, 209);\n"
"}\n"
"QPushButton:hover{\n"
"border: 2px solid black;\n"
"border-radius: 10px;\n"
"background-color:rgb(207, 238, 236);\n"
"}\n"
"")
        self.DutyButton.setObjectName("DutyButton")
        self.verticalLayout_3.addWidget(self.DutyButton)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.frame_3)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(310, 10, 151, 191))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.FrequencyValue = QtWidgets.QLCDNumber(self.verticalLayoutWidget_4)
        self.FrequencyValue.setDigitCount(3)
        self.FrequencyValue.setProperty("value", 1.0)
        self.FrequencyValue.setObjectName("FrequencyValue")
        self.verticalLayout_4.addWidget(self.FrequencyValue)
        self.DutyValue = QtWidgets.QLCDNumber(self.verticalLayoutWidget_4)
        self.DutyValue.setDigitCount(3)
        self.DutyValue.setObjectName("DutyValue")
        self.verticalLayout_4.addWidget(self.DutyValue)
        self.RefreshSerial = QtWidgets.QPushButton(self.centralwidget)
        self.RefreshSerial.setGeometry(QtCore.QRect(20, 70, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.RefreshSerial.setFont(font)
        self.RefreshSerial.setFlat(False)
        self.RefreshSerial.setObjectName("RefreshSerial")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.CloseSerial.setText(_translate("MainWindow", "Отключить"))
        self.SerialStatusLabel.setText(_translate("MainWindow", "Статус подключения"))
        self.OpenSerial.setText(_translate("MainWindow", "Подключить"))
        self.StartButton.setText(_translate("MainWindow", "Старт"))
        self.StopButton.setText(_translate("MainWindow", "Стоп"))
        self.FrequencyLabel.setText(_translate("MainWindow", "Частота"))
        self.DutyLabel.setText(_translate("MainWindow", "Заполнение"))
        self.FrequencyButton.setText(_translate("MainWindow", "Ввод"))
        self.DutyButton.setText(_translate("MainWindow", "Ввод"))
        self.RefreshSerial.setText(_translate("MainWindow", "Обновить"))