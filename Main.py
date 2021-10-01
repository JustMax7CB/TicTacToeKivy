from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, NumericProperty
from kivymd.app import MDApp

Window.size = (500, 500)


class GameWindow(Widget):
    x_win = NumericProperty(0)
    o_win = NumericProperty(0)


class TicTacToeApp(MDApp):
    def build(self):
        return GameWindow()

    def CheckWin(self, player, *args):
        print('this is a test')

    def Win(self, player, *args):
        player += 1
        print(player)

    def Restart(self, *args):
        for x in args:
            x.text = ""


if __name__ == "__main__":
    TicTacToeApp().run()
