import sys
import os
from PyQt5.QtWidgets import QWidget,QApplication,QTextEdit,QLabel,QPushButton,QVBoxLayout,QFileDialog,QHBoxLayout
from PyQt5.QtWidgets import QAction,qApp,QMainWindow
class Notepad(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.text_area = QTextEdit()
        self.clean = QPushButton("Clean")
        self.open = QPushButton("Open")
        self.save = QPushButton("Save")
        self.exit = QPushButton("Exit")

        h_box = QHBoxLayout()
        h_box.addWidget(self.clean)
        h_box.addWidget(self.open)
        h_box.addWidget(self.save)
        h_box.addWidget(self.exit)

        v_box = QVBoxLayout()
        v_box.addWidget(self.text_area)
        v_box.addLayout(h_box)
        self.setLayout(v_box)
        self.setWindowTitle("NotePad")
        self.clean.clicked.connect(self.cleaner)
        self.open.clicked.connect(self.opener)
        self.save.clicked.connect(self.saver)
        self.exit.clicked.connect(self.Exit)


    def cleaner(self):
        self.text_area.clear()
    def opener(self):
        file_name = QFileDialog.getOpenFileName(self,"File Open",os.getenv("HOME"))
        with open(file_name[0],"r") as file:
            self.text_area.setText(file.read())
    def saver(self):
        file_name = QFileDialog.getSaveFileName(self,"File Save",os.getenv("HOME"))
        with open(file_name[0],"w") as file:
            file.write(self.text_area.toPlainText())
    def Exit(self):
        qApp.quit()

class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.window = Notepad()
        self.setCentralWidget(self.window)
        self.creates_menu()
    def creates_menu(self):
        menubar = self.menuBar()
        file = menubar.addMenu("File")
        open_file = QAction("Open File",self)
        open_file.setShortcut("Ctrl+O")

        save_file = QAction("Save File",self)
        save_file.setShortcut("Ctrl+S")

        clean = QAction("Clean",self)
        clean.setShortcut("Ctrl+D")

        exit = QAction("Exit",self)
        exit.setShortcut("Ctrl+Q")

        file.addAction(open_file)
        file.addAction(save_file)
        file.addAction(clean)
        file.addAction(exit)

        file.triggered.connect(self.response)
        self.setWindowTitle("Text Editor")
        self.show()
    def response(self,action):
        if action.text() == "Open File":
            self.window.opener()
        elif action.text() == "Save File":
            self.window.saver()
        elif action.text() == "Clean":
            self.window.cleaner()
        elif action.text() == "Exit":
            qApp.quit()

app = QApplication(sys.argv)
menu = Menu()
sys.exit(app.exec_())