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

x_pos = 0
y_pos = 0
while True:
    oled.text("Hellow!",x_pos,y_pos)
    oled.show()
    sleep(0.1)
    oled.fill(0)
    oled.show()
    if x_pos > 125:
        x_pos = 0;
    else :
        x_pos = x_pos+5
    