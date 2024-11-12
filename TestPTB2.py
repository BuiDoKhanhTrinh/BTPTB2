from PyQt6.QtWidgets import QApplication, QMainWindow

from ui.MainWindowPTB2Ext import MainWindowPTB2Ext

app=QApplication([])
window=QMainWindow()
myUI = MainWindowPTB2Ext()
myUI.setupUi(window)
myUI.showWindow()
app.exec()