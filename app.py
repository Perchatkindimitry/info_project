from PyQt6 import QtWidgets
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import QTimer, QTime
from screen_manager import Screen
from screens import about_screen, code_screen, decode_screen, start_screen, game_screen
from screens.main_app import Ui_MainWindow

import algorithms


class App(QtWidgets.QMainWindow):
    """
    The main class of app
    """
    def __init__(self):
        super(App, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.screen_loader()
        self.button_loader()


        self.size_timer = QTimer(self)
        self.size_timer.timeout.connect(self.size_check)
        self.size_timer.start(100)

        #self.scene = QtWidgets.QGraphicsScene()
        #self.game_screen.ui.graphicsView.setScene(self.scene)

        self.img = [QPixmap('resourses/img/00.jpg'),
                    QPixmap('resourses/img/01.jpg'),
                    QPixmap('resourses/img/02.jpg'),
                    QPixmap('resourses/img/03.jpg')]

    
    def button_loader(self):
        """
        Connecting buttons to functions
        """
        self.start_screen.ui.menu.buttonClicked.connect(self.menu_click)

        back = lambda: self.ui.stackedWidget.setCurrentIndex(0)
        self.code_screen.ui.back_button.clicked.connect(back)
        self.decode_screen.ui.back_button.clicked.connect(back)
        self.about_screen.ui.back_button.clicked.connect(back)
        self.game_screen.ui.back_button.clicked.connect(back)


        self.start_screen.ui.game_button.clicked.connect(self.start_game)
        self.code_screen.ui.run_button.clicked.connect(self.code)
        self.decode_screen.ui.run_button.clicked.connect(self.decode)



    def size_check(self):
        h = self.game_screen.ui.img.height()
        self.game_screen.ui.img.setPixmap(self.img[1].scaledToHeight(h))
        #w, h = self.game_screen.ui.graphicsView.width(), self.game_screen.ui.graphicsView.height()
        #print(w, h)
        #for i in range(len(self.img)):
           # self.img[i] = self.img[i].scaledToHeight(h)
           # self.img[i] = self.img[i].scaledToHeight(w)
        #img = QtWidgets.QGraphicsPixmapItem(self.img[0])
        #self.scene.addItem(img)


    def screen_loader(self):
        """
        Loading all screens for app
        """
        self.start_screen = Screen(start_screen.Ui_Form())
        self.ui.stackedWidget.addWidget(self.start_screen)

        self.code_screen = Screen(code_screen.Ui_Form())
        self.ui.stackedWidget.addWidget(self.code_screen)
        
        self.decode_screen = Screen(decode_screen.Ui_Form())
        self.ui.stackedWidget.addWidget(self.decode_screen)
        
        self.about_screen = Screen(about_screen.Ui_Form())
        self.ui.stackedWidget.addWidget(self.about_screen)

        self.game_screen = Screen(game_screen.Ui_Form())
        self.ui.stackedWidget.addWidget(self.game_screen)



    def menu_click(self, pressed_button):
        """
        Checking press button in start menu
        """
        for i, button in enumerate(self.start_screen.ui.menu.buttons()):
            if button == pressed_button:
                self.ui.stackedWidget.setCurrentIndex(i + 1)
                break


    def code(self):
        text = self.code_screen.ui.input.text()
        code = algorithms.Code(text)
        self.code_screen.ui.output.setText(code.result)


    def decode(self):
        text = self.decode_screen.ui.input.text()
        code = algorithms.Decode(text)
        self.decode_screen.ui.output.setText(code + 'расшифровал')


    def start_game(self):
       
        self.ui.stackedWidget.setCurrentIndex(4)
