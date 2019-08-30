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
BaseSidesPin = 2
BasefbPin = 3
TopfbPin = 4
TopPin = 5
TopSidesPin = 6

a.pinMode(led, a.OUTPUT)
a.pinMode(BaseSidesPin, a.OUTPUT)
a.pinMode(BasefbPin, a.OUTPUT)
a.pinMode(TopfbPin, a.OUTPUT)
a.pinMode(TopPin, a.OUTPUT)
a.pinMode(TopSidesPin, a.OUTPUT)

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


#function to test all status
def teststatus():
    print("teststatus activated")
    
    
    if(AllStatus == 0):
        a.digitalWrite(BaseSidesPin, a.LOW)
        a.digitalWrite(BasefbPin, a.LOW)
        a.digitalWrite(TopfbPin, a.LOW)
        a.digitalWrite(TopPin, a.LOW)
        a.digitalWrite(TopSidesPin, a.LOW)
    else:   
        if(BaseSidesStatus == 1):
            a.digitalWrite(BaseSidesPin, a.HIGH)
        else:
            a.digitalWrite(BaseSidesPin, a.LOW)
            
            
        if(BasefbStatus == 1):
            a.digitalWrite(BasefbStatus, a.HIGH)
        else:
            a.digitalWrite(BaseSidesPin, a.LOW)   
    
        
        
        if(TopfbStatus == 1):
            a.digitalWrite(TopfbStatus, a.HIGH)
        else:
            a.digitalWrite(BaseSidesPin, a.LOW)
        
        
        if(TopStatus == 1):
            a.digitalWrite(TopStatus, a.HIGH)
        else:
            a.digitalWrite(BaseSidesPin, a.LOW)
        
                
        if(TopSidesStatus == 1):
            a.digitalWrite(TopSidesStatus, a.HIGH)
        else:
            a.digitalWrite(BaseSidesPin, a.LOW)
        
#Status 1=clear, 0= opaque
AllStatus= 0
BaseSidesStatus = 0
BasefbStatus= 0
TopfbStatus = 0
TopStatus = 0
TopSidesStatus = 0        
#---------------------------------------------------------
teststatus()

#Define Callback for Toggle
def press_callback(obj):
#Programmed so that 'normal'or HIGH means opaque
#'down' or LOW means clear
    if(obj.text == 'All'):
        if(obj.state == "down"):
            Allstatus = 0
            print ("Allstatus Value:")
            print(Allstatus)
            if(AllStatus == 0):
                a.digitalWrite(BaseSidesPin, a.LOW)
                a.digitalWrite(BasefbPin, a.LOW)
                a.digitalWrite(TopfbPin, a.LOW)
                a.digitalWrite(TopPin, a.LOW)
                a.digitalWrite(TopSidesPin, a.LOW)
            else:
                Allstatus = 1
            print ("Allstatus Value:")
            print(Allstatus)
            print(led)
            teststatus()


    if(obj.text == 'Top f/b'):
        if(obj.state == "down"):
            TopfbStatus = 0
            teststatus()
        else:
            TopfbStatus = 1
            teststatus()


    if(obj.text == 'Base f/b'):
        if(obj.state == "down"):
            BasefbStatus = 0
            teststatus()
        else:
            BasefbStatus = 1
            teststatus()


    if (obj.text == 'Top'):
        if(obj.state == "down"):
            TopStatus = 0
            teststatus()
        else:
            TopStatus = 1
            teststatus()


    if(obj.text == 'Base Sides'):
        if obj.state == "down":
            BaseSidesStatus = 0
            teststatus()
        else:
            BaseSidesStatus = 1
            teststatus()


    if(obj.text == 'Top Sides'):
        if (obj.state == "down"):
            TopSidesStatus = 0
            teststatus()
        else:
            TopSidesStatus = 1
            teststatus()
            
            
#    if (obj.text == "LED"):
#        if(obj.state == "down"):
#            a.digitalWrite(3, a.HIGH)
#        else:
#            a.digitalWrite(3, a.LOW)

#--------------------------------------------------------------
class HomeScreen(GridLayout):
    def __init__(self, **kwargs):
        super(HomeScreen,self).__init__(**kwargs)
        self.cols = 3
#Status 1=clear, 0= opaque
        AllStatus= 0
        BaseSidesStatus = 0
        BasefbStatus= 0
        TopfbStatus = 0
        TopStatus = 0
        TopSidesStatus = 0
        
        #Output toggle
#        self.LED = ToggleButton(text="LED")
#        self.LED.bind(on_press = press_callback)
#        self.add_widget(self.LED)
        
        self.All = ToggleButton(text='All')
        self.All.bind(on_press = press_callback)
        self.add_widget(self.All)
        
        self.Top_fb = ToggleButton(text= 'Top f/b')
        self.Top_fb.bind(on_press = press_callback)
        self.add_widget(self.Top_fb)
        
        self.Base_fb = ToggleButton(text='Base f/b')
        self.Base_fb.bind (on_press = press_callback)
        self.add_widget(self.Base_fb)
        
        self.Top = ToggleButton(text = 'Top')
        self.Top.bind(on_press = press_callback)
        self.add_widget(self.Top)
        
        self.BaseSides = ToggleButton(text= 'Base Sides')
        self.BaseSides.bind(on_press = press_callback)
        self.add_widget(self.BaseSides)
        
        self.TopSides = ToggleButton(text = 'Top Sides')
        self.TopSides.bind(on_press = press_callback)
        self.add_widget(self.TopSides)              


class TestApp(App):
    def build(self):
#        return Label(text="Hello World!")
        return HomeScreen()

Window.fullscreen = True
TestApp().run()

#print('hello world')
#for i in range(10):
#    a.digitalWrite(led, a.LOW)
#    sleep(1)
#    a.digitalWrite(led, a.HIGH)
#    sleep(1)

