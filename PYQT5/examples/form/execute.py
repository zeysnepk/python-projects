
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from form import Ui_MainWindow


class main(QMainWindow):
    
    def __init__(self):
        
        super().__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.pushButton_send.clicked.connect(self.click)
        
    def click(self):
        
        name = self.ui.lineEdit_name.text()
        no = self.ui.lineEdit_no.text()
        
        if self.ui.radioButton_man.isChecked():
            gender = "Man"
            
        elif self.ui.radioButton_woman.isChecked():
            gender = "Woman"
            
        else:
            gender = "Unknown"
            
        age = self.ui.spinBox_age.value()
        
        row_count = self.ui.tableWidget_data.rowCount()
        self.ui.tableWidget_data.insertRow(row_count)
        self.ui.tableWidget_data.setItem(row_count, 0, QTableWidgetItem(str(row_count + 1)))
        self.ui.tableWidget_data.setItem(row_count, 1, QTableWidgetItem(name))
        self.ui.tableWidget_data.setItem(row_count, 2, QTableWidgetItem(no))
        self.ui.tableWidget_data.setItem(row_count, 3, QTableWidgetItem(gender))
        self.ui.tableWidget_data.setItem(row_count, 4, QTableWidgetItem(str(age)))
        
        
    
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = main()
    main_window.show()
    sys.exit(app.exec_())