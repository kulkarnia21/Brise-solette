#Status 1 = clear, 0 = opaque
#Output: LOW = Clear, HIGH = Opaque,
#Button Press: 'down' = Clear, 'normal' = Opaque

##Setting up communication with Arduino-----------------------------------
from nanpy import (ArduinoApi, SerialManager)
from time import sleep
try:
    connection = SerialManager()
    a = ArduinoApi(connection = connection)
except:
    print("Failed to connect to Arduino")
    
#Setup Pin Modes----------------------------------------------------------
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

#Declaring sides status
# 0 is opaque, 1 is clear
AllStatus = 0
BaseSidesStatus = 0
BasefbStatus = 0
TopfbStatus = 0
TopStatus = 0
TopSidesStatus = 0

# Declaring vitals status
# True = within range, False = out of range
HRstatus = True
RRstatus = True
Osatstatus = True
Tempstatus = True
Sysstatus = True
Diastatus = True

interval = 3
timer = 0
LightCyclingStatus = 0

##Importing and Setup----------------------------------------------------------------
from kivy.app import App
from kivy.core.window import Window  # Required to toggle fullscreen and set resolution
from kivy.uix.gridlayout import GridLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.clock import Clock  # For Scheduling tasks
from kivy.uix.slider import Slider  # For vitals tab
from kivy.properties import NumericProperty  # For Vitals tab

Window.fullscreen = True
Window.show_cursor = False
Window.size = (800, 480)

#Adding Function for light cycling-------------------------------------------------
def cycling(dt):
    global Timer
    global LightCyclingStatus

    global AllStatus
    global BaseSidesStatus
    global BasefbStatus
    global TopfbStatus
    global TopStatus
    global TopSidesStatus

    global HRstatus
    global RRstatus
    global Osatstatus
    global Tempstatus
    global Sysstatus
    global Diastatus

    if(LightCyclingStatus == 1 and AllStatus == 0 and BaseSidesStatus == 0 and BasefbStatus == 0 and TopfbStatus == 0 and TopStatus == 0 and TopSidesStatus == 0 and HRstatus == True and RRstatus == True and Osatstatus == True and Tempstatus == True and Sysstatus == True and Diastatus == True):
        #print("Light cycling status is 1")
        if((Timer%interval) == 0):
            #print("interval")
            if ((Timer/interval) %2 == 0):
                a.digitalWrite(BaseSidesPin, a.LOW)
                a.digitalWrite(BasefbPin, a.LOW)
                a.digitalWrite(TopfbPin, a.LOW)
                a.digitalWrite(TopPin, a.LOW)
                a.digitalWrite(TopSidesPin, a.LOW)
                Timer = Timer + 1
                #print(Timer)
            else:
                a.digitalWrite(BaseSidesPin, a.HIGH)
                a.digitalWrite(BasefbPin, a.HIGH)
                a.digitalWrite(TopfbPin, a.HIGH)
                a.digitalWrite(TopPin, a.HIGH)
                a.digitalWrite(TopSidesPin, a.HIGH)
                Timer = Timer + 1
                #print(Timer)
        else:
            Timer = Timer + 1
            #print(Timer)
    else:
        #print("Light cycling status is 0")
        Timer = 0

#---------------------------------------------------------------------------

## Adding recurring task to test everything
def allsystemscheck(dt):
    global AllStatus
    global BaseSidesStatus
    global BasefbStatus
    global TopfbStatus
    global TopStatus
    global TopSidesStatus

    global LightCyclingStatus

    global HRstatus
    global RRstatus
    global Osatstatus
    global Tempstatus
    global Sysstatus
    global Diastatus

    if(LightCyclingStatus == 1 and AllStatus == 0 and BaseSidesStatus == 0 and BasefbStatus == 0 and TopfbStatus == 0 and TopStatus == 0 and TopSidesStatus == 0 and HRstatus == True and RRstatus == True and Osatstatus == True and Tempstatus == True and Sysstatus == True and Diastatus == True):
        print("testing")
    else:
        if(HRstatus == True and RRstatus == True and Osatstatus == True and Tempstatus == True and Sysstatus == True and Diastatus == True):
            teststatus()
        else:
            a.digitalWrite(BaseSidesPin, a.HIGH)
            a.digitalWrite(BasefbPin, a.HIGH)
            a.digitalWrite(TopfbPin, a.HIGH)
            a.digitalWrite(TopPin, a.HIGH)
            a.digitalWrite(TopSidesPin, a.HIGH)

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
#making callback to change value
def press_callback(obj):
    global AllStatus
    global BaseSidesStatus
    global BasefbStatus
    global TopfbStatus
    global TopStatus
    global TopSidesStatus

    global LightCyclingStatus

    #Callback for All Function
    if(obj.text == 'All'):
        if(obj.state == "down"):
            AllStatus = 1
            #teststatus()
        else:
            AllStatus = 0
            #teststatus()
    # End of All Function Callback-------------------------------------------
    
    # Callback for Top f/b Function
    if(obj.text == 'Top f/b'):
        if(obj.state == "down"):
            TopfbStatus = 1
            #teststatus()
        else:
            TopfbStatus = 0
            #teststatus()
    # End of Top f/b Callback-----------------------------------------------
    
    # Callback for Base f/b Function
    if(obj.text == 'Base f/b'):
        if(obj.state == "down"):
            BasefbStatus = 1
            #teststatus()
        else:
            BasefbStatus = 0
            #teststatus()
    # End of Base f/b Callback----------------------------------------------
    
    #Callback for Top Function
    if (obj.text == 'Top'):
        if(obj.state == "down"):
            TopStatus = 1
            #teststatus()
        else:
            TopStatus = 0
            #teststatus()
    # End of Top Callback---------------------------------------------------

    # Callback for Top Sides Function
    if(obj.text == 'Top Sides'):
        if (obj.state == "down"):
            TopSidesStatus = 1
            #teststatus()
        else:
            TopSidesStatus = 0
            #teststatus()
    # End of Top Sides Callback----------------------------------------------
            
    # Callback for Base Sides Function
    if(obj.text == 'Base Sides'):
        if obj.state == "down":
            BaseSidesStatus = 1
            #teststatus()
        else:
            BaseSidesStatus = 0
            #teststatus()
    # End of Base Sides Callback--------------------------------------------

    # Callback for Light Cycling
    if(obj.text == 'Light Cycling'):
        if obj.state == "down":
            LightCyclingStatus = 1
            #print("Light Cycling Status: ", LightCyclingStatus)
        else:
            LightCyclingStatus = 0
            #print("Light Cycling Status: ",  LightCyclingStatus)
    # End of Light Cycling Callback-----------------------------------------
# End of Callback functions


class Brisesolette(App):
    def build(self):
        root = Accordion(orientation='vertical')

        # Building manual Control Tab---------------------------------------
        ManualControl = AccordionItem(title='Manual Control',)
        
        # Adding Layout Layer
        Layout=GridLayout(cols=3)

        # Build All Button
        Layout.All = ToggleButton(text= 'All') #state='down'
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

        # Setting up grid layout
        global VitalsLayout
        VitalsLayout = GridLayout(cols=6)

        ##Adding in HR Vitals
        #HR Label
        VitalsLayout.add_widget(Label(text = "Heart Rate(BPM)"))
        #HR slider
        VitalsLayout.HRVitals = Slider(min = 70, max = 190, value = 130)
        VitalsLayout.add_widget(VitalsLayout.HRVitals)
        #HR value display
        VitalsLayout.HRdisplay = Label(text = '130')
        VitalsLayout.add_widget(VitalsLayout.HRdisplay)
        #HR value updating
        VitalsLayout.HRVitals.bind(value = self.HRValue)

        ##Adding in RR Vitals
        # RR Label
        VitalsLayout.add_widget(Label(text="Respiratory Rate"))
        # RR slider
        VitalsLayout.RRVitals = Slider(min=15, max=75, value=45)
        VitalsLayout.add_widget(VitalsLayout.RRVitals)
        # RR value display
        VitalsLayout.RRdisplay = Label(text='45')
        VitalsLayout.add_widget(VitalsLayout.RRdisplay)
        # RR value updating
        VitalsLayout.RRVitals.bind(value=self.RRValue)

        ##Adding in Osat Vitals
        # Osat Label
        VitalsLayout.add_widget(Label(text="Oxygen Saturation(%)"))
        # Osat slider
        VitalsLayout.OsatVitals = Slider(min=50, max=100, value=95)
        VitalsLayout.add_widget(VitalsLayout.OsatVitals)
        # Osat value display
        VitalsLayout.Osatdisplay = Label(text='95')
        VitalsLayout.add_widget(VitalsLayout.Osatdisplay)
        # Osat value updating
        VitalsLayout.OsatVitals.bind(value=self.OsatValue)

        ##Adding in Temp Vitals
        # Temp Label
        VitalsLayout.add_widget(Label(text="Temperature(F)"))
        # Temp slider
        VitalsLayout.TempVitals = Slider(min=90, max=105, value=97)
        VitalsLayout.add_widget(VitalsLayout.TempVitals)
        # Temp value display
        VitalsLayout.Tempdisplay = Label(text='97')
        VitalsLayout.add_widget(VitalsLayout.Tempdisplay)
        # Temp value updating
        VitalsLayout.TempVitals.bind(value=self.TempValue)

        ##Adding in Sys Vitals
        # Sys Label
        VitalsLayout.add_widget(Label(text="Systolic BP(mmHg)"))
        # Sys slider
        VitalsLayout.SysVitals = Slider(min=58, max=93, value=76)
        VitalsLayout.add_widget(VitalsLayout.SysVitals)
        # Sys value display
        VitalsLayout.Sysdisplay = Label(text='76')
        VitalsLayout.add_widget(VitalsLayout.Sysdisplay)
        # Sys value updating
        VitalsLayout.SysVitals.bind(value=self.SysValue)

        ##Adding in Dia Vitals
        # Dia Label
        VitalsLayout.add_widget(Label(text="Diastolic BP(mmHg)"))
        # Dia slider
        VitalsLayout.DiaVitals = Slider(min=26, max=62, value=44)
        VitalsLayout.add_widget(VitalsLayout.DiaVitals)
        # Dia value display
        VitalsLayout.Diadisplay = Label(text='44')
        VitalsLayout.add_widget(VitalsLayout.Diadisplay)
        # Dia value updating
        VitalsLayout.DiaVitals.bind(value=self.DiaValue)

        # End of updating vitals tab-------------------------------------------------------

        Vitals.add_widget(VitalsLayout)  # Adding layout to Vitals

        root.add_widget(Vitals)  # Adding Vitals accordion Tab

        # End of Vitals Tab------------------------------------------------------

        # Scheduled task----------------------------------------------------------
        Clock.schedule_interval(cycling, 1.0)
        Clock.schedule_interval(allsystemscheck, 0.1)
        return root

    # Updating Vitals tab--------------------------------------------------------------
    def HRValue(self, instance, HR):
        global VitalsLayout
        global HRstatus
        if(HR > 100 and HR < 160):
            HRstatus = True
            #print("HRstatus true")
        else:
            HRstatus = False
            #print("HRstatus False")
        VitalsLayout.HRdisplay.text = "%d" % HR

    def RRValue(self, instance, RR):
        global VitalsLayout
        global RRstatus
        if(RR > 30 and RR < 60):
            RRstatus = True
        else:
            RRstatus = False
        VitalsLayout.RRdisplay.text = "%d" % RR

    def OsatValue(self, instance, Osat):
        global VitalsLayout
        global Osatstatus
        if(Osat > 90):
            Osatstatus = True
        else:
            Osatstatus = False
        VitalsLayout.Osatdisplay.text = "%d" % Osat

    def TempValue(self, instance, Temp):
        global VitalsLayout
        global Tempstatus
        if(Temp > 95 and Temp < 100):
            Tempstatus = True
        else:
            Tempstatus = False
        VitalsLayout.Tempdisplay.text = "%d" % Temp

    def SysValue(self, instance, Sys):
        global VitalsLayout
        global Sysstatus
        if(Sys > 67 and Sys < 84):
            Sysstatus = True
        else:
            Sysstatus = False
        VitalsLayout.RRdisplay.text = "%d" % Sys

    def DiaValue(self, instance, Dia):
        global VitalsLayout
        global Diastatus
        if(Dia > 35 and Dia < 53):
            Diastatus = True
        else:
            Diastatus = False
        VitalsLayout.Diadisplay.text = "%d" % Dia

if __name__ == '__main__':
    Brisesolette().run()
    #Failsafe: Adding statements to execute on close, will drive all relays to closed position (allowing current through)


print("Bye Bye!")
a.digitalWrite(BaseSidesPin, a.HIGH)
a.digitalWrite(BasefbPin, a.HIGH)
a.digitalWrite(TopfbPin, a.HIGH)
a.digitalWrite(TopPin, a.HIGH)
a.digitalWrite(TopSidesPin, a.HIGH)