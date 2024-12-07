#import libary 
from machine import Pin
from time import sleep 
#GPIO pin set-up BUT1,2,3,4 : IO15,2,0,4
sw1_pin = Pin(15,Pin.IN)
sw2_pin = Pin(2,Pin.IN,Pin.PULL_UP)
sw3_pin = Pin(0,Pin.IN,Pin.PULL_DOWN)
sw4_pin = Pin(4,Pin.IN)

#Main Program
while True:
    #Read State
    sw1_state = sw1_pin.value()
    sw2_state = sw2_pin.value()
    sw3_state = sw3_pin.value()
    sw4_state = sw4_pin.value()
    
    #Show State
    print("swl: {}".format(sw3_state))
    sleep(0.5)
