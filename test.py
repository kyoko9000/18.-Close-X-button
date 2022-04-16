#no need to install anything
import sys
# pip install pyqt6
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
# just change the name
from gui1 import Ui_Form
import time
import threading

class MainWindow(QWidget):
    def __init__(self):

        super().__init__()
        # the way app working
        self.uic = Ui_Form()
        self.uic.setupUi(self)
        # khai bai nut nhan
        self.uic.Button_start.clicked.connect(self.start_loop)

    def start_loop(self):
        print("press start")
        global a
        a = True
        self.loop()
    def closeEvent(self, event):
        print("press stop")
        global a
        a = False
    def loop(self):
        print("ready")
        def run():
            while a == True:
                print("run")
                time.sleep(0.5)
                if a == False:
                    break
        t1 = threading.Thread(target=run)
        t1.start()

if __name__ == "__main__":
    # run app
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())