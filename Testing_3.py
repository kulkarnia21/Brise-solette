#Setting up communication with Arduino
from nanpy import (ArduinoApi, SerialManager)
from time import sleep
try:
    connection = SerialManager()
    a = ArduinoApi (connection = connection)
except:
    print("Failed to connect to Arduino")
#Setup Pinmodes
    
led = 13
a.pinMode(led, a.OUTPUT)
#-------------------------------------------------------------

from kivy.app import App
from kivy.core.window import Window #Required to toggle fullscreen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.togglebutton import ToggleButton
#from kivy.uix.textinput import TextInput
#from kivy.uix.image import Image
#from kivy.uix.slider import Slider
#from kivy.clock import Clock
#from kivy.graphics import Color, Rectangle

#Define Callback for Toggle
def press_callback(obj):
    if obj.text == 'self.LED':
        if obj.state == "down":
            a.digitalWrite(led, a.HIGH)
        else:
            a.digitalWrite(led, a.LOW)
                

class HomeScreen(GridLayout):
    def __init__(self, **kwargs):
        super(HomeScreen,self).__init__(**kwargs)
        self.cols = 2
        
        
        #Define and Add UI Elements to the layout
        self.add_widget(Label(text="Arduino LED"))       
        
        #Output toggle
        self.LED = ToggleButton(text="LED")
        self.LED.bind(on_press = press_callback)
        self.add_widget(self.LED)
        
        
        
        
class TestApp(App):
    def build(self):
#        return Label(text="Hello World!")
        return HomeScreen()

Window.fullscreen = True
TestApp().run()

print('hello world')
