#Import Libary 
from machine import Pin
from neopixel import NeoPixel

#Pin Setup  : (pin,number of Led)
rgb_pin = Pin(23,Pin.OUT)
rgb_pixel_num = 2
rgb_led = NeoPixel(rgb_pin,rgb_pixel_num)

#Set Color
#              R,G,B
rgb_led[0] = (20,0,30)
rgb_led[1] = (10,10,10,)

rgb_led.write()