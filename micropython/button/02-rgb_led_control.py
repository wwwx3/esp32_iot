#Import libary 
from machine import Pin
from neopixel import NeoPixel
from time import sleep

#Pin setup 
sw1_pin = Pin(15,Pin.IN)
sw2_pin = Pin(2,Pin.IN,Pin.PULL_UP)
sw3_pin = Pin(0,Pin.IN)
sw4_pin = Pin(4,Pin.IN)

np_pin = Pin(23,Pin.OUT)
np = NeoPixel(np_pin,2)
                  
#Main Program
while True:
    #Read state
    sw1_state = sw1_pin.value()
    sw2_state = sw2_pin.value()
    print("SW1: {} SW2: {}".format(sw1_state,sw2_state))
    
    if sw1_state == 0:
        np[0] = (10,0,10)
        np.write()
        print("SW1 Pressed")
    else:
        np[0] = (0,0,0)
        np.write()
        print("SW1 Not Pressed")
    if sw2_state == 0:
        np[1] = (0,20,30)
        np.write()
        print("SW2 Pressed")
    else:
        np[1] = (0,0,0)
        np.write()
        print("SW2 Not pressed")

    
    sleep(0.1)
    
    