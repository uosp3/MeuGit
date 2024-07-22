# from PyQt5 import QtCore, QtGui, QtWidgets
from PySide6 import QtCore, QtGui, QtWidgets


class Ui_myWidget(object):
    def setupUi(self, myWidget):
        myWidget.setObjectName("myWidget")
        myWidget.resize(400, 300)
        font = QtGui.QFont()
        font.setPointSize(40)
        myWidget.setFont(font)
        self.horizontalLayout = QtWidgets.QHBoxLayout(myWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label1 = QtWidgets.QLabel(myWidget)
        self.label1.setObjectName("label1")
        self.gridLayout.addWidget(self.label1, 0, 0, 1, 1)
        self.label2 = QtWidgets.QLabel(myWidget)
        font = QtGui.QFont()
        font.setPointSize(40)
        self.label2.setFont(font)
        self.label2.setObjectName("label2")
        self.gridLayout.addWidget(self.label2, 0, 1, 1, 1)
        self.button1 = QtWidgets.QPushButton(myWidget)
        self.button1.setObjectName("button1")
        self.gridLayout.addWidget(self.button1, 1, 0, 1, 1)
        self.button2 = QtWidgets.QPushButton(myWidget)
        self.button2.setObjectName("button2")
        self.gridLayout.addWidget(self.button2, 1, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)

        self.retranslateUi(myWidget)
        QtCore.QMetaObject.connectSlotsByName(myWidget)

    def retranslateUi(self, myWidget):
        _translate = QtCore.QCoreApplication.translate
        myWidget.setWindowTitle(_translate("myWidget", "Form"))
        self.label1.setText(_translate("myWidget", "L1"))
        self.label2.setText(_translate("myWidget", "L2"))
        self.button1.setText(_translate("myWidget", "B1"))
        self.button2.setText(_translate("myWidget", "B2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myWidget = QtWidgets.QWidget()
    ui = Ui_myWidget()
    ui.setupUi(myWidget)
    myWidget.show()
    sys.exit(app.exec_())
