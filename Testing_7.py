#Status 1 = clear, 0 = opaque
#Output: LOW = Clear, HIGH = Opaque,
#Button Press: 'down' = Clear, 'normal' = Opaque

##Setting up communication with Arduino
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

AllStatus= 1
BaseSidesStatus = 0
BasefbStatus= 0
TopfbStatus = 0
TopStatus = 0
TopSidesStatus = 0 
#---------------------------------------------------------------------------


##Importing and Setup
from kivy.app import App
from kivy.core.window import Window #Required to toggle fullscreen and set resolution
from kivy.uix.gridlayout import GridLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.label import Label
#---------------------------------------------------------------------------

##function to test all status
def teststatus():
    global AllStatus
    global BaseSidesStatus
    global BasefbStatus
    global TopfbStatus
    global TopStatus
    global TopSidesStatus
    
    if AllStatus == 1:
        a.digitalWrite(BaseSidesPin, a.LOW)
        a.digitalWrite(BasefbPin, a.LOW)
        a.digitalWrite(TopfbPin, a.LOW)
        a.digitalWrite(TopPin, a.LOW)
        a.digitalWrite(TopSidesPin, a.LOW)
        
        
    else:        
        if BaseSidesStatus == 1:
            a.digitalWrite(BaseSidesPin, a.LOW)
        else:
            a.digitalWrite(BaseSidesPin, a.HIGH)
               
        if BasefbStatus == 1:
            a.digitalWrite(BasefbPin, a.LOW)
        else:
            a.digitalWrite(BasefbPin, a.HIGH)   
    
        if TopfbStatus == 1:
            a.digitalWrite(TopfbPin, a.LOW)
        else:
            a.digitalWrite(TopfbPin, a.HIGH)
        
        if TopStatus == 1:
            a.digitalWrite(TopPin, a.LOW)
        else:
            a.digitalWrite(TopPin, a.HIGH)
              
        if TopSidesStatus == 1:
            a.digitalWrite(TopSidesPin, a.LOW)
        else:
            a.digitalWrite(TopSidesPin, a.HIGH)
            
# End of function to test all statuses---------------------------------------------


#Define Callback for Toggle
def press_callback(obj):
    #Callback for All Function
    if(obj.text == 'All'):
        if(obj.state == "down"):
            global AllStatus
            AllStatus = 1
            teststatus()
        else:
            global AllStatus
            AllStatus=0
            teststatus()
    #End of All Function Callback-------------------------------------------
    
    #Callback for Top f/b Function
    if(obj.text == 'Top f/b'):
        if(obj.state == "down"):
            global TopfbStatus
            TopfbStatus = 1
            teststatus()
        else:
            global TopfbStatus
            TopfbStatus = 0
            teststatus()
    #End of Top f/b Callback-----------------------------------------------
    
    #Callback for Base f/b Function
    if(obj.text == 'Base f/b'):
        if(obj.state == "down"):
            global BasefbStatus
            BasefbStatus = 1
            teststatus()
        else:
            global BasefbStatus
            BasefbStatus = 0
            teststatus()
    #End of Base f/b Callback----------------------------------------------
    
    #Callback for Top Function
    if (obj.text == 'Top'):
        if(obj.state == "down"):
            global TopStatus
            TopStatus = 1
            teststatus()
        else:
            global TopStatus
            TopStatus = 0
            teststatus()
    #End of Top Callback---------------------------------------------------

    #Callback for Top Sides Function
    if(obj.text == 'Top Sides'):
        if (obj.state == "down"):
            global TopSidesStatus
            TopSidesStatus = 1
            teststatus()
        else:
            global TopSidesStatus
            TopSidesStatus = 0
            teststatus()
    #End of Top Sides Callback----------------------------------------------
            
    #Callback for Base Sides Function
    if(obj.text == 'Base Sides'):
        if obj.state == "down":
            global BaseSidesStatus
            BaseSidesStatus = 1
            teststatus()
        else:
            global BaseSidesStatus
            BaseSidesStatus = 0
            teststatus()
    #End of Base Sides Callback--------------------------------------------

# End of Callback functions

class Brisesolette(App):
    def build(self):
        root = Accordion(orientation='vertical')
        
#        item_1 = AccordionItem(title='Title 1')
#        item_1.add_widget(Label(text='Very big content\n' *10))
#        root.add_widget(item_1)
        
        #Building manual Control Tab
        ManualControl = AccordionItem(title='Manual Control')
        #Build All Button
        ManualControl.All = ToggleButton(text= 'All', state='down')
        ManualControl.All.bind(on_press = press_callback)
        ManualControl.add_widget(ManualControl.All)
        
        #Build Top F/B Button
        ManualControl.Top_fb = ToggleButton(text= 'Top f/b')
        ManualControl.Top_fb.bind(on_press = press_callback)
        ManualControl.add_widget(ManualControl.Top_fb)
        
        #Build Base F/B Button
        ManualControl.Base_fb = ToggleButton(text='Base f/b')
        ManualControl.Base_fb.bind(on_press = press_callback)
        ManualControl.add_widget(ManualControl.Base_fb)
        
        #Build Top Button
        ManualControl.Top = ToggleButton(text = 'Top')
        ManualControl.Top.bind(on_press = press_callback)
        ManualControl.add_widget(ManualControl.Top)
        
        #Build Base Sides Button
        ManualControl.BaseSides = ToggleButton(text= 'Base Sides')
        ManualControl.BaseSides.bind(on_press = press_callback)
        ManualControl.add_widget(ManualControl.BaseSides)
        
        #Build Top Sides Button
        ManualControl.TopSides = ToggleButton(text = 'Top Sides')
        ManualControl.TopSides.bind(on_press = press_callback)
        ManualControl.add_widget(ManualControl.TopSides)
        
        #Add Accordion Tab
        root.add_widget(ManualControl)
        #End of Manual Control Tab---------------------------------------------
        
        
        #Vitals and Light Cycling Tab
        VLC = AccordionItem(title='Vitals and Light Cycling')
        root.add_widget(VLC)

        return root


if __name__ == '__main__':
    Window.size = (800,480)
    Window.fullscreen = True
    Brisesolette().run()