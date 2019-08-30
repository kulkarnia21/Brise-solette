from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.slider import Slider
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle

#class HomeScreen(GridLayout):
#    def __init__(self, **kwargs):
#        super (HomeScreen,self).__init(**kwargs)
#        self.cols = 2
#        
#        sellf.add_widget (Label(text="lkd"))
        
        
class TestApp(App):
    def build(self):
        return Label(text="hello world")
#        return HomeScreen()

Window.fullscreen = True
TestApp().run()