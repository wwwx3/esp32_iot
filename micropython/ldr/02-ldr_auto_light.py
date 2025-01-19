#import lib
from machine import Pin,ADC
from time import sleep
from neopixel import NeoPixel 

#Pin setup
ldr_pin = ADC(Pin(36))
np = NeoPixel(Pin(23),2)
 
while True:
    #Read LDR Value
    ldr_value = ldr_pin.read()
    ldr_percentage = (4095 - ldr_value)/4095 * 100
    print("LDR Percentage:",ldr_percentage)
    print("LDR Analog Value: ",ldr_value)
     
    if ldr_percentage < 50:
         print("Too dark ( •́ ‸ •̀ )")
         np[0] = (10,10,10)
         np[1] = (10,10,10)
         np.write()
    else:
        print("Normal light (✿◕‿◕)")
        np[0] = (0,0,0)
        np[1] = (0,0,0)
        np.write()
    sleep(0.3)