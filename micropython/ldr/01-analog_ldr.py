#import lib
from machine import Pin,ADC
from time import sleep

#Pin setup
ldr_pin = ADC(Pin(36))
 
while True:
     #Read LDR Value
     ldr_value = ldr_pin.read()
     ldr_percentage = (4095 - ldr_value)/4095 * 100
     
     print("LDR Percentage:",ldr_percentage)
     print("LDR Analog Value: ",ldr_value)
     sleep(0.3)
     
     