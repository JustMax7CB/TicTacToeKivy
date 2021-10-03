import threading
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, NumericProperty
from kivymd.app import MDApp


class InvalidPopup(FloatLayout):
    pass


class EndGame(BoxLayout):
    pass


class GameWindow(Widget):
    Window.size = (500, 500)
    InvalidPopupShow = InvalidPopup()
    InvalidpopupWindow = Popup(title="Invalid Move", content=InvalidPopupShow, size_hint=(None, None), size=(200, 100))

    b1 = ObjectProperty(None)
    b2 = ObjectProperty(None)
    b3 = ObjectProperty(None)
    b4 = ObjectProperty(None)
    b5 = ObjectProperty(None)
    b6 = ObjectProperty(None)
    b7 = ObjectProperty(None)
    b8 = ObjectProperty(None)
    b9 = ObjectProperty(None)
    x_win = NumericProperty()
    o_win = NumericProperty()
    playerTimer = NumericProperty()
    WinFlag = False
    
    def restart(self, *args):
        for x in args:
            x.text = ""
        self.playerTimer = 0
        
    def WinFlagMethod(self, winner):
        if self.WinFlag:
            self.WinFlag = False
        EndGamePopup = EndGame()
        EndGamePopupWindow = Popup(title=f"{winner} has won the game!", content=EndGamePopup, size_hint=(None, None),
                                   size=(200, 100))
        EndGamePopupWindow.bind(on_dismiss=self.restart(self.b1,self.b2,self.b3,self.b4,self.b5,self.b6,self.b7,self.b8,self.b9))
        EndGamePopupWindow.open()



    def Play(self, button, *args):
        if button.text != "":
            self.InvalidpopupWindow.open()
        else:
            if self.playerTimer % 2 == 0:
                button.text = "X"
            else:
                button.text = "O"
            self.CheckWin(*args)

    def CheckWin(self, *args):
        # Possible Winning Combinations:
        # b1,b2,b3 ; b4,b5,b6 ; b7,b8,b9
        # b1,b4,b7 ; b2,b5,b8 ; b3,b6,b9
        # b1,b5,b9 ; b3,b5,b7
        if self.playerTimer % 2 == 0:
            Option1 = args[0].text == "X" and args[1].text == "X" and args[2].text == "X"
            Option2 = args[3].text == "X" and args[4].text == "X" and args[5].text == "X"
            Option3 = args[6].text == "X" and args[7].text == "X" and args[8].text == "X"
            Option4 = args[0].text == "X" and args[3].text == "X" and args[6].text == "X"
            Option5 = args[1].text == "X" and args[4].text == "X" and args[7].text == "X"
            Option6 = args[2].text == "X" and args[5].text == "X" and args[8].text == "X"
            Option7 = args[0].text == "X" and args[4].text == "X" and args[8].text == "X"
            Option8 = args[2].text == "X" and args[4].text == "X" and args[6].text == "X"

        else:
            Option1 = args[0].text == "O" and args[1].text == "O" and args[2].text == "O"
            Option2 = args[3].text == "O" and args[4].text == "O" and args[5].text == "O"
            Option3 = args[6].text == "O" and args[7].text == "O" and args[8].text == "O"
            Option4 = args[0].text == "O" and args[3].text == "O" and args[6].text == "O"
            Option5 = args[1].text == "O" and args[4].text == "O" and args[7].text == "O"
            Option6 = args[2].text == "O" and args[5].text == "O" and args[8].text == "O"
            Option7 = args[0].text == "O" and args[4].text == "O" and args[8].text == "O"
            Option8 = args[2].text == "O" and args[4].text == "O" and args[6].text == "O"

        if True in (Option1, Option2, Option3, Option4, Option5, Option6, Option7, Option8):
            self.Win()
        self.playerTimer = str(int(self.playerTimer) + 1)

    def Win(self):
        if self.playerTimer % 2 == 0:
            self.ids.x_win_label.text = f"X Wins:{str(int(self.x_win) + 1)}"
            self.x_win += 1
            print('X Wins')
            self.WinFlag = True
            self.WinFlagMethod("X")



        else:
            self.ids.o_win_label.text = f"O Wins:{str(int(self.o_win) + 1)}"
            self.o_win += 1
            print('O Wins')
            self.WinFlag = True
            self.WinFlagMethod("O")

    


class TicTacToeApp(MDApp):
    def build(self):
        return GameWindow()


if __name__ == "__main__":
    TicTacToeApp().run()
