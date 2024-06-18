import sys
import requests
from bs4 import BeautifulSoup
from PyQt5 import QtWidgets, QtGui, QtCore

#NOT COMPLETED!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

class Window(QtWidgets.QWidget):
    
    def __init__(self):
        
        super().__init__()
        
        
        self.homepage()
        
        self.connectNet()
        
    def homepage(self):
        
        self.labelGold = QtWidgets.QLabel("")
        self.labelDollar = QtWidgets.QLabel("")
        self.labelEuro = QtWidgets.QLabel("")
        self.labelSterlin = QtWidgets.QLabel("")
        self.labelBitcoin = QtWidgets.QLabel("")
        
        self.image = QtWidgets.QLabel("")
        self.image.setPixmap(QtGui.QPixmap("/Users/zeynepkaplan/Desktop/PythonProjects/PYQT5/examples/Currency/currencyHome.jpeg"))
        self.image.setAlignment(QtCore.Qt.AlignCenter)
        
        
        h_box = QtWidgets.QHBoxLayout()
        
        h_box.addWidget(self.labelGold)
        h_box.addWidget(self.labelDollar)
        h_box.addWidget(self.labelEuro)
        h_box.addWidget(self.labelSterlin)
        h_box.addWidget(self.labelBitcoin)
        
        v_box = QtWidgets.QVBoxLayout()
        
        v_box.addLayout(h_box)
        v_box.addWidget(self.image)
        v_box.addStretch()
        
        self.setLayout(v_box)
        
    def connectNet(self):
        
        self.homeCurrency = {}
        
        url = "https://www.doviz.com/"

        response = requests.get(url)

        content = response.content

        soup = BeautifulSoup(content,"html.parser")

        for i, j, k in zip(soup.find_all("span", {"class" : "name"}), soup.find_all("span",{"class" : "value"}), soup.find_all("div", {"class" : "change-rate status down"})):
            
            name = i.text.strip()
            value = j.text.strip()
            down = k.text.strip()
            
            print(name)
            
            if name == "GRAM ALTIN":
                self.labelGold.setText("Gram Gold" + "\n" + value + "\n" + down)
                
            elif name == "DOLAR":
                self.labelDollar.setText("Dollar" + "\n" + value + "\n" + down)
                
            elif name == "EURO":
                self.labelEuro.setText("Euro" + "\n" + value + "\n" + down)
                
            elif name == "STERLİN":
                self.labelSterlin.setText("Sterlin" + "\n" + value + "\n" + down)
                
            elif name == "BITCOIN":
                self.labelBitcoin.setText("Bitcoin" + "\n" + value + "\n" + down)

class Menu(QtWidgets.QMainWindow):
    
    def __init__(self):
        
        super().__init__()
        
        self.window = Window()
        
        self.setCentralWidget(self.window)
        
        self.create_menu()
        
        self.show()
        
    def create_menu(self):
        
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        
        home = menubar.addMenu("Home")
        gold = menubar.addMenu("Gold")
        crypto = menubar.addMenu("Crypto")
        news = menubar.addMenu("News")
        
        
app = QtWidgets.QApplication(sys.argv)

menu = Menu()

sys.exit(app.exec_())
        
        