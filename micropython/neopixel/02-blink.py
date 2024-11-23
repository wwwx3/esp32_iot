#Import Libary
from machine import Pin
from neopixel import NeoPixel
from time import sleep

#Pin set up
rgb_pin = Pin(23,Pin.OUT)
rgb_pixel_num = 2
rgb_led = NeoPixel(rgb_pin,rgb_pixel_num)

#Main
while True:
    #Set color (open)
    rgb_led[0] = (20,0,30)
    rgb_led[1] = (0,10,20)
    #Show Color (open)
    rgb_led.write()
    #Wait 0.1 sec
    sleep(0.1)
    #Set color (close)
    rgb_led[0] = (0,0,0)
    rgb_led[1] = (0,0,0)
    #Show color (close)
    rgb_led.write()
    sleep(0.1)
    