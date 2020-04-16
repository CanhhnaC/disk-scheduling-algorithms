from PyQt5 import QtGui, QtWidgets, QtCore, uic
from diskScheduling import *

qt_creator_file = "untitled.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qt_creator_file)


class getValue(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(getValue, self).__init__(*args, **kwargs)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.pushButton.pressed.connect(self.getData)

    def keyPressEvent(self, event):
        if event.key() == 16777220 or event.key() == QtCore.Qt.Key_Enter:
            self.getData()

    def getData(self):
        try:
            # Get values in line edit
            number1 = int(self.number1.text())
            number2 = self.number2.text()

            # Convert string number 2 to list
            distance = number2.split(',')
            distance = list(map(int, distance))

            # Chose disk
            name = str(self.comboBox.currentText())
            if name == "FCFS - First Come First Serve":
                FCFS(number1, distance)
            elif name == "SSTF - Shortest Seek Time First":
                SSTF(number1, distance)
            elif name == "SCAN - Elevator":
                SCAN(number1, distance)
            elif name == "C-SCAN - Circular SCAN":
                C_SCAN(number1, distance)
            elif name == "LOOK":
                LOOK(number1, distance)
            else:
                C_LOOK(number1, distance)

            self.handle()

        except Exception:
            QtWidgets.QMessageBox.warning(
                self, "Error", "Nhap sai roi, nhap lai")

    def handle(self):
        self.graphWidget.clear()
        self.result.setText(
            "Total number of seek operations =" + str(load('total')))
        self.graphWidget.plot(load('distance'), symbol='o')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = getValue()
    window.show()
    sys.exit(app.exec_())
