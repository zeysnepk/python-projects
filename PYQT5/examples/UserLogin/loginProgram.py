import sys
import sqlite3
from PyQt5 import QtWidgets, QtGui, QtCore


class Window(QtWidgets.QWidget):
    
    def __init__(self):
        
        super().__init__()
        
        self.connect()
        self.init_gui()
        
    
    def connect(self):
            
        connect = sqlite3.connect("database.db")
        
        self.cursor = connect.cursor()
        
        self.cursor.execute("CREATE TABLE IF NOT EXISTS members (username TEXT, password TEXT)")
        
        connect.commit()
    
    def init_gui(self):
        
        imagelabel = QtWidgets.QLabel()
        image = QtGui.QPixmap("/Users/zeynepkaplan/Desktop/PythonProjects/PYQT5/examples/UserLogin/user.png")
        scaled = image.scaled(200, 150, aspectRatioMode=QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
        imagelabel.setPixmap(scaled)
        imagelabel.setAlignment(QtCore.Qt.AlignCenter)
        
        self.username = QtWidgets.QLineEdit()
        self.password = QtWidgets.QLineEdit()
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        
        label_name = QtWidgets.QLabel("Username: ")
        label_password = QtWidgets.QLabel("Password: ")
        
        self.login_box = QtWidgets.QPushButton("LOGIN")
        
        self.text = QtWidgets.QLabel("")
        self.text.setAlignment(QtCore.Qt.AlignCenter)
        
        v_box = QtWidgets.QVBoxLayout()
        h_box1 = QtWidgets.QHBoxLayout()
        h_box2 = QtWidgets.QHBoxLayout()
        h_box3 = QtWidgets.QHBoxLayout()
        
        h_box1.addWidget(label_name)
        h_box1.addWidget(self.username)
        
        h_box2.addWidget(label_password)
        h_box2.addWidget(self.password)
        
        h_box3.addStretch()
        h_box3.addWidget(self.login_box)
        
        v_box.addWidget(imagelabel)
        v_box.addLayout(h_box1)
        v_box.addLayout(h_box2)
        v_box.addLayout(h_box3)
        v_box.addWidget(self.text)
        
        self.setLayout(v_box)
        
        self.setWindowTitle("LOGIN PAGE")
        
        self.login_box.clicked.connect(self.login)
        
        self.show()
        
    def login(self):
        
        usernameInput = self.username.text()
        passwordInput = self.password.text()
        
        self.cursor.execute("SELECT *FROM members WHERE username = ? and password = ?",(usernameInput,passwordInput))
        dataList = self.cursor.fetchall()
        
        if len(dataList) == 0:
            
            self.text.setText("Please Try Again!")
            self.username.clear()
            self.password.clear()
            
        else:
            self.text.setText("Welcome " + usernameInput + " !")
        

app = QtWidgets.QApplication(sys.argv)

window = Window()

sys.exit(app.exec_())