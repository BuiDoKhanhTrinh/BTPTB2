# Form implementation generated from reading ui file 'D:\hoccode\QT Designer\TEST\BTPTB2\ui\ptb2.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 30, 311, 51))
        self.label.setObjectName("label")
        self.lineEditA = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditA.setGeometry(QtCore.QRect(230, 100, 113, 20))
        self.lineEditA.setObjectName("lineEditA")
        self.lineEditB = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditB.setGeometry(QtCore.QRect(230, 130, 113, 20))
        self.lineEditB.setObjectName("lineEditB")
        self.lineEditC = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditC.setGeometry(QtCore.QRect(230, 160, 113, 20))
        self.lineEditC.setObjectName("lineEditC")
        self.lineEditKQ = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditKQ.setGeometry(QtCore.QRect(230, 190, 113, 20))
        self.lineEditKQ.setObjectName("lineEditKQ")
        self.pushButtonCalc = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonCalc.setGeometry(QtCore.QRect(70, 270, 75, 23))
        self.pushButtonCalc.setObjectName("pushButtonCalc")
        self.pushButtonContinue = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonContinue.setGeometry(QtCore.QRect(250, 270, 75, 23))
        self.pushButtonContinue.setObjectName("pushButtonContinue")
        self.pushButtonClose = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonClose.setGeometry(QtCore.QRect(420, 270, 75, 23))
        self.pushButtonClose.setObjectName("pushButtonClose")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 100, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 130, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(100, 160, 47, 13))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(100, 190, 47, 13))
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">PHƯƠNG TRÌNH BẬC 2</span></p></body></html>"))
        self.pushButtonCalc.setText(_translate("MainWindow", "Calc"))
        self.pushButtonContinue.setText(_translate("MainWindow", "Continue"))
        self.pushButtonClose.setText(_translate("MainWindow", "Close"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Hệ số a</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Hệ số b</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Hệ số c</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p>Kết quả</p></body></html>"))