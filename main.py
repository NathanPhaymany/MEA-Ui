from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.config import Config
from kivy.uix.widget import Widget
from kivy.properties import Property
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.core.window import Window


class MainWindow(Screen):
    pass

class FireWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("my.kv")


Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '480')



class MyApp(App):
    def build(self):
        return kv

if __name__ == '__main__':
    MyApp().run()