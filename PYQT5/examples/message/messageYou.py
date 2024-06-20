
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.resize(400, 425)
        Form.setMinimumSize(QtCore.QSize(400, 425))
        Form.setMaximumSize(QtCore.QSize(400, 425))
        Form.setSizeIncrement(QtCore.QSize(0, 0))
        Form.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        Form.setStyleSheet("background-color: rgb(157, 220, 231);")
        self.pushButton_you = QtWidgets.QPushButton(Form)
        self.pushButton_you.setGeometry(QtCore.QRect(140, 380, 100, 32))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.pushButton_you.setFont(font)
        self.pushButton_you.setStyleSheet("background-color: rgb(150, 41, 33);")
        self.pushButton_you.setObjectName("pushButton_you")
        self.textEdit_from_you = QtWidgets.QTextEdit(Form)
        self.textEdit_from_you.setGeometry(QtCore.QRect(40, 200, 311, 171))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        self.textEdit_from_you.setFont(font)
        self.textEdit_from_you.setStyleSheet("color: rgb(13, 15, 6);\n"
"font: 14pt \"Times New Roman\";")
        self.textEdit_from_you.setFrameShape(QtWidgets.QFrame.Panel)
        self.textEdit_from_you.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.textEdit_from_you.setLineWidth(2)
        self.textEdit_from_you.setObjectName("textEdit_from_you")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(20, 45, 271, 21))
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.toolButton = QtWidgets.QToolButton(Form)
        self.toolButton.setEnabled(False)
        self.toolButton.setGeometry(QtCore.QRect(0, 10, 61, 41))
        self.toolButton.setAutoFillBackground(False)
        self.toolButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/heart/heart.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/heart/heart.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setAutoRaise(True)
        self.toolButton.setObjectName("toolButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 20, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Baskerville")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(150, 41, 33);")
        self.label.setObjectName("label")
        self.toolButton_2 = QtWidgets.QToolButton(Form)
        self.toolButton_2.setEnabled(False)
        self.toolButton_2.setGeometry(QtCore.QRect(170, 10, 71, 41))
        self.toolButton_2.setFocusPolicy(QtCore.Qt.TabFocus)
        self.toolButton_2.setAcceptDrops(False)
        self.toolButton_2.setAutoFillBackground(False)
        self.toolButton_2.setText("")
        self.toolButton_2.setIcon(icon)
        self.toolButton_2.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.toolButton_2.setAutoRaise(True)
        self.toolButton_2.setObjectName("toolButton_2")
        self.label_message_me = QtWidgets.QLabel(Form)
        self.label_message_me.setGeometry(QtCore.QRect(20, 70, 361, 111))
        self.label_message_me.setStyleSheet("color: rgb(8, 5, 17);\n"
"font: 13pt \"Gill Sans\";")
        self.label_message_me.setText("")
        self.label_message_me.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_message_me.setObjectName("label_message_me")
        self.pushButton_you.raise_()
        self.textEdit_from_you.raise_()
        self.line.raise_()
        self.toolButton.raise_()
        self.toolButton_2.raise_()
        self.label.raise_()
        self.label_message_me.raise_()
        
        Form.move(800,300)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "YOU"))
        self.pushButton_you.setText(_translate("Form", "SEND"))
        self.textEdit_from_you.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p></body></html>"))
        self.label.setText(_translate("Form", "Message From Me"))
import heart_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
