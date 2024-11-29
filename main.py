import sys

from PyQt5 import QtGui
from PyQt5 import QtWidgets
from injectors_control import Ui_MainWindow
from serialport import SerialPort

# Конвертация .ui to .py pyuic5 injectors_control.ui -o injectors_control.py


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.serial_port = SerialPort(self.ui)
        self.ui.OpenSerial.clicked.connect(self.serial_port.open_serial)
        self.ui.CloseSerial.clicked.connect(self.serial_port.close_serial)
        self.ui.RefreshSerial.clicked.connect(self.serial_port.refresh_serial)
        self.ui.FrequencyButton.clicked.connect(self.change_frequency)
        self.ui.DutyButton.clicked.connect(self.change_duty)
        self.ui.StartButton.clicked.connect(self.start_work)
        self.ui.StopButton.clicked.connect(self.stop_work)
        self.serial_port.serial.readyRead.connect(self.on_read)
        try:
            from PyQt5.QtWinExtras import QtWin

            myappid = "0.1"
            QtWin.setCurrentProcessExplicitAppUserModelID(myappid)
        except ImportError:
            pass

    def change_frequency(self):
        self.serial_port.serial_send([0, self.ui.FrequencyBox.value()])

    def change_duty(self):
        self.serial_port.serial_send([1, self.ui.DutyBox.value()])

    def start_work(self):
        self.serial_port.serial_send([2])

    def stop_work(self):
        self.serial_port.serial_send([3])
        self.ui.FrequencyValue.display(0)
        self.ui.FrequencyBox.setValue(1)
        self.ui.DutyValue.display(0)
        self.ui.DutyBox.setValue(0)

    def on_read(self):
        if self.serial_port.serial.canReadLine():
            rx = self.serial_port.serial.readLine()
            try:
                rxs = str(rx, "utf-8").strip()
                data = rxs.split(",")
                if data[0] == "0":
                    self.ui.FrequencyValue.display(data[1])
                    self.ui.DutyValue.display(data[2])
                    if data[3] == "1":
                        self.ui.WorkStatus.setStyleSheet(
                            "background-color: green;"
                        )
                    else:
                        self.ui.WorkStatus.setStyleSheet(
                            "background-color: red;"
                        )
                    self.ui.ImpulseTime.display(
                        f"{((1 / int(data[1])) * (int(data[2]) / 255)) * 1000:.3f}"
                    )
                print(data)
            except (IndexError, UnicodeDecodeError, ValueError):
                print(f"Ошибка при передаче данных: {rx}")


app = QtWidgets.QApplication([])
application = MyWindow()
app.setWindowIcon(QtGui.QIcon("static/icon.png"))
application.setWindowIcon(QtGui.QIcon("static/icon.png"))
application.show()
sys.exit(app.exec())
