from ui.funtion import calc
from ui.ptb2 import Ui_MainWindow


class MainWindowPTB2Ext(Ui_MainWindow):


    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()

    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButtonCalc.clicked.connect(self.slot_calc)
        self.pushButtonClose.clicked.connect(self.slot_close)
        self.pushButtonContinue.clicked.connect(self.slot_continue)

    def slot_continue(self):
        self.lineEditA.setText("")
        self.lineEditB.setText("")
        self.lineEditC.setText("")
        self.lineEditKQ.setText("")
        self.lineEditA.setFocus()

    def slot_close(self):
        self.MainWindow.close()

    def slot_calc(self):
        a = int(self.lineEditA.text())
        b = int(self.lineEditB.text())
        c = int(self.lineEditC.text())
        kq = calc(a,b,c)
        self.lineEditKQ.setText(f"Kết quả = {kq}")
