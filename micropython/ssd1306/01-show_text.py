#Import libary
from machine import Pin,SoftI2C
from time import sleep
from ssd1306 import SSD1306_I2C

#Pin setup
oled_Pin = SoftI2C(scl=Pin(22),sda=Pin(21))

#OLED Interface
oled = SSD1306_I2C(128,64,oled_Pin)

#Show Text
oled.text("Hellow world!",0,0)
oled.show()
