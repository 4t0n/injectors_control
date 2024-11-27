from PyQt5 import QtWidgets
from PyQt5.QtCore import QIODevice
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtWidgets import QMessageBox


class SerialPort(QtWidgets.QMainWindow):
    def __init__(self, ui):
        QtWidgets.QWidget.__init__(self)
        self.serial = QSerialPort()
        self.serial.setBaudRate(115200)
        self.ports = QSerialPortInfo().availablePorts()
        self.portlist = [port.portName() for port in self.ports]
        self.ui = ui
        self.ui.ComboSerial.addItems(self.portlist)

    def refresh_serial(self):
        self.ui.ComboSerial.clear()
        self.ports = QSerialPortInfo().availablePorts()
        self.portlist = [port.portName() for port in self.ports]
        self.ui.ComboSerial.addItems(self.portlist)

    def open_serial(self):
        try:
            self.serial.setPortName(self.ui.ComboSerial.currentText())
            if self.serial.open(QIODevice.ReadWrite):
                self.ui.SerialStatus.setStyleSheet(
                    'background-color: green;' 'border: 2px solid black;'
                )
                self.ui.FrequencyButton.setEnabled(True)
                self.ui.DutyButton.setEnabled(True)
                self.ui.StartButton.setEnabled(True)
                self.ui.StopButton.setEnabled(True)
                self.ui.CloseSerial.setEnabled(True)
                self.ui.OpenSerial.setEnabled(False)
                self.ui.DutyValue.display(0)
                self.ui.FrequencyValue.display(1)
                self.ui.FrequencyBox.setValue(1)
                self.ui.DutyBox.setValue(0)
            else:
                raise Exception
        except Exception:
            QMessageBox.critical(self, 'Ошибка', 'Подключите оборудование.')

    def close_serial(self):
        self.serial.setPortName(self.ui.ComboSerial.currentText())
        self.serial.close()
        self.ui.SerialStatus.setStyleSheet(
            'background-color: red;' 'border: 2px solid black;'
        )
        self.ui.FrequencyButton.setEnabled(False)
        self.ui.DutyButton.setEnabled(False)
        self.ui.StartButton.setEnabled(False)
        self.ui.StopButton.setEnabled(False)
        self.ui.CloseSerial.setEnabled(False)
        self.ui.OpenSerial.setEnabled(True)

    def serial_send(self, data):
        self.serial.setPortName(self.ui.ComboSerial.currentText())
        data_str = ','.join(list(map(str, data))) + ';'
        if self.serial.write(data_str.encode()) == -1:
            QMessageBox.critical(self, 'Ошибка', 'Подключите оборудование.')
        print(data_str.encode())

    def check_connect(self, value):
        if value == 2:
            value = 1
        self.serial_send([0, value])
