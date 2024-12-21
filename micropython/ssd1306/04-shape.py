#Import libary
from machine import Pin,SoftI2C
from time import sleep
from framebuf import FrameBuffer,MONO_HLSB
from ssd1306 import SSD1306_I2C
from images import miwo_logo
from images import mari_logo

#Pin setup
oled_Pin = SoftI2C(scl=Pin(22),sda=Pin(21))

#OLED Interface
oled = SSD1306_I2C(128,64,oled_Pin)

#Screen Invert
oled.invert(1)

#Line x , y , width , height , color 
oled.rect(3,3,122,58,1)
oled.show()

#Fill Rect x , y , width , height , color 
oled.fill_rect(25,20,20,20,1)
oled.text("Fill Rect",50,25)
oled.show()

#Create frame buffer
fb = FrameBuffer(miwo_logo,128,64,MONO_HLSB)

#Blit the image to the display and show it
oled.fill(0)
oled.blit(fb, 0, 0)
oled.show()

