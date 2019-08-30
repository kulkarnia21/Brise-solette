#Status 1 = clear, 0 = opaque
#Output: LOW = Clear, HIGH = Opaque,
#Button Press: 'down' = Clear, 'normal' = Opaque

##Setting up communication with Arduino
from nanpy import (ArduinoApi, SerialManager)
from time import sleep
try:
    connection = SerialManager()
    a = ArduinoApi(connection = connection)
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

AllStatus = 1
BaseSidesStatus = 0
BasefbStatus = 0
TopfbStatus = 0
TopStatus = 0
TopSidesStatus = 0

interval = 3
Timer = 0
LightCyclingStatus = 0

##Importing and Setup
from kivy.app import App
from kivy.core.window import Window #Required to toggle fullscreen and set resolution
from kivy.uix.gridlayout import GridLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.clock import Clock

#Adding Function for light cycling-------------------------------------------------
def cycling():
    global Timer
    global LightCyclingStatus
    if(LightCyclingStatus == 1):
        if((Timer%interval) == 0):
            if ((Timer/3) %2 == 0):
                a.digitalWrite(BaseSidesPin, a.LOW)
                a.digitalWrite(BasefbPin, a.LOW)
                a.digitalWrite(TopfbPin, a.LOW)
                a.digitalWrite(TopPin, a.LOW)
                a.digitalWrite(TopSidesPin, a.LOW)
            else:
                a.digitalWrite(BaseSidesPin, a.HIGH)
                a.digitalWrite(BasefbPin, a.HIGH)
                a.digitalWrite(TopfbPin, a.HIGH)
                a.digitalWrite(TopPin, a.HIGH)
                a.digitalWrite(TopSidesPin, a.HIGH)
                Timer = Timer + 1
        else:
            Timer = Timer + 1
    else:
        Timer = 0
        teststatus()

Clock.schedule_interval(cycling, 1)

#---------------------------------------------------------------------------

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
        a.digitalWrite(BaseSidesPin, a.HIGH)
        a.digitalWrite(BasefbPin, a.HIGH)
        a.digitalWrite(TopfbPin, a.HIGH)
        a.digitalWrite(TopPin, a.HIGH)
        a.digitalWrite(TopSidesPin, a.HIGH)
        
        
    else:
        if BaseSidesStatus == 1:
            a.digitalWrite(BaseSidesPin, a.HIGH)
        else:
            a.digitalWrite(BaseSidesPin, a.LOW)
               
        if BasefbStatus == 1:
            a.digitalWrite(BasefbPin, a.HIGH)
        else:
            a.digitalWrite(BasefbPin, a.LOW)   
    
        if TopfbStatus == 1:
            a.digitalWrite(TopfbPin, a.HIGH)
        else:
            a.digitalWrite(TopfbPin, a.LOW)
        
        if TopStatus == 1:
            a.digitalWrite(TopPin, a.HIGH)
        else:
            a.digitalWrite(TopPin, a.LOW)
              
        if TopSidesStatus == 1:
            a.digitalWrite(TopSidesPin, a.HIGH)
        else:
            a.digitalWrite(TopSidesPin, a.LOW)
            
# End of function to test all statuses---------------------------------------------

# Define Callback for Toggle-------------------------------------------------------

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
    # End of All Function Callback-------------------------------------------
    
    # Callback for Top f/b Function
    if(obj.text == 'Top f/b'):
        if(obj.state == "down"):
            global TopfbStatus
            TopfbStatus = 1
            teststatus()
        else:
            global TopfbStatus
            TopfbStatus = 0
            teststatus()
    # End of Top f/b Callback-----------------------------------------------
    
    # Callback for Base f/b Function
    if(obj.text == 'Base f/b'):
        if(obj.state == "down"):
            global BasefbStatus
            BasefbStatus = 1
            teststatus()
        else:
            global BasefbStatus
            BasefbStatus = 0
            teststatus()
    # End of Base f/b Callback----------------------------------------------
    
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
    # End of Top Callback---------------------------------------------------

    # Callback for Top Sides Function
    if(obj.text == 'Top Sides'):
        if (obj.state == "down"):
            global TopSidesStatus
            TopSidesStatus = 1
            teststatus()
        else:
            global TopSidesStatus
            TopSidesStatus = 0
            teststatus()
    # End of Top Sides Callback----------------------------------------------
            
    # Callback for Base Sides Function
    if(obj.text == 'Base Sides'):
        if obj.state == "down":
            global BaseSidesStatus
            BaseSidesStatus = 1
            teststatus()
        else:
            global BaseSidesStatus
            BaseSidesStatus = 0
            teststatus()
    # End of Base Sides Callback--------------------------------------------

    # Callback for Light Cycling
    if(obj.text == 'Light Cycling'):
        if obj.state == "down":
            global LightCyclingStatus
            LightCyclingStatus = 1
        else:
            global LightCyclingStatus
            LightCyclingStatus = 0
    # End of Light Cycling Callback-----------------------------------------
cycling()
# End of Callback functions


class Brisesolette(App):
    def build(self):
        root = Accordion(orientation='vertical')

        # Building manual Control Tab---------------------------------------
        ManualControl = AccordionItem(title='Manual Control',)
        
        # Adding Layout Layer
        Layout=GridLayout(cols=3)

        # Build All Button
        Layout.All = ToggleButton(text= 'All', state='down')
        Layout.All.bind(on_press = press_callback)
        Layout.add_widget(Layout.All)
        
        # Build Top F/B Button
        Layout.Top_fb = ToggleButton(text= 'Top f/b')
        Layout.Top_fb.bind(on_press = press_callback)
        Layout.add_widget(Layout.Top_fb)
        
        # Build Base F/B Button
        Layout.Base_fb = ToggleButton(text='Base f/b')
        Layout.Base_fb.bind(on_press = press_callback)
        Layout.add_widget(Layout.Base_fb)
        
        # Build Top Button
        Layout.Top = ToggleButton(text = 'Top')
        Layout.Top.bind(on_press = press_callback)
        Layout.add_widget(Layout.Top)
        
        # Build Base Sides Button
        Layout.BaseSides = ToggleButton(text= 'Base Sides')
        Layout.BaseSides.bind(on_press = press_callback)
        Layout.add_widget(Layout.BaseSides)
        
        # Build Top Sides Button
        Layout.TopSides = ToggleButton(text = 'Top Sides')
        Layout.TopSides.bind(on_press = press_callback)
        Layout.add_widget(Layout.TopSides)

        # Adding Buttons to Manual Control
        ManualControl.add_widget(Layout)
        # Add Accordion Tab
        root.add_widget(ManualControl)

        # End of Manual Control Tab---------------------------------------------
        
        
        # Light Cycling Tab-----------------------------------------------------

        LC = AccordionItem(title='Light Cycling')
        LCLayout = GridLayout(cols=2)

        #Declaring Elements
        logo = Image(source='Brise-solette_Logo.png', allow_stretch='True')
        LCLayout.add_widget(logo)

        LCLayout.LCButton = ToggleButton(text = "Light Cycling")
        LCLayout.LCButton.bind(on_press = press_callback)
        LCLayout.add_widget(LCLayout.LCButton)

        LC.add_widget(LCLayout)  # Adding layout to LC
        
        root.add_widget(LC)  # Adding LC Accordion Tab

        # End of Light Cycling Tab----------------------------------------------

        # Vitals Tab -----------------------------------------------------------

        Vitals = AccordionItem(title='Vitals')

        # Declaring Elements
        logo = Image(source='Brise-solette_Logo.png', allow_stretch='True')


        # Setting up grid layout
        VitalsLayout = GridLayout(cols=2)

        # Adding elements
        VitalsLayout.add_widget(logo)

        Vitals.add_widget(VitalsLayout)  # Adding layout to Vitals

        root.add_widget(Vitals)  # Adding Vitals accordion Tab

        # End of Vitals Tab------------------------------------------------------





        return root


if __name__ == '__main__':
    Window.show_cursor = False
    Window.size = (800,480)
    Window.fullscreen = True
    Brisesolette().run()


