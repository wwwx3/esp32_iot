#Import libary
from machine import Pin,SoftI2C
from time import sleep
from ssd1306 import SSD1306_I2C

#Pin setup
oled_Pin = SoftI2C(scl=Pin(22),sda=Pin(21))

#OLED Interface
oled = SSD1306_I2C(128,64,oled_Pin)

#Screen Invert
oled.invert(1)

#Example
while True :
    #Show Text
    oled.text("Hiii~!",64,32)
    oled.show()
    sleep(1)
    oled.text("Hiii~!",64,32,0)
    oled.show()
    sleep(1)
    oled.text("Hiii~!",16,32,1)
    oled.show()
    sleep(1)
    oled.fill(0)
    oled.show()
