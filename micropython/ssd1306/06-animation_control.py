#Import libary
from machine import Pin,SoftI2C,PWM
from time import sleep
from framebuf import FrameBuffer,MONO_HLSB
from ssd1306 import SSD1306_I2C
from images import miwo_logo , mari_logo

#Variable
show_image = 0
#Pin setup
btn1_pin = Pin(15,Pin.IN)
btn2_pin = Pin(0,Pin.IN,Pin.PULL_UP)
buzzer_pin = Pin(32,Pin.OUT)
beeper = PWM(buzzer_pin)
beeper.duty_u16(0)

#Oled setup
oled_Pin = SoftI2C(scl=Pin(22),sda=Pin(21))

#OLED Interface
oled = SSD1306_I2C(128,64,oled_Pin)

#Screen Invert
oled.fill(0)
oled.invert(1)

#Line x , y , width , height , color 
oled.rect(3,3,122,58,1)
oled.show()

#Create frame buffer
fb_miwo = FrameBuffer(miwo_logo,128,64,MONO_HLSB)
fb_mari = FrameBuffer(mari_logo,128,64,MONO_HLSB)


#Blit the image to the display and show it(Welcome massage) 
oled.text("Option",5,20)
oled.text("1-Show Image1",5,30)
oled.text("2-Show Image2",5,40)
#oled.blit(fb2, 0, 0)
oled.show()

#Main Program
while True:
    #Read button state
    btn1_state = btn1_pin.value()
    btn2_state = btn2_pin.value()
    
    print('btn1:{} btn2:{}'.format(btn1_state,btn2_state))
    
    #Check if button pressed
    if btn1_state == 0 :
        beeper.freq(300)
        beeper.duty(100)
        show_img = 1 

    elif btn2_state == 0 :
        beeper.freq(500)
        beeper.duty(100)
        show_img = 2
    else:
        beeper.duty(0)
        show_img = 0 
    if show_img == 1 :
        oled.fill(0)
        oled.blit(fb_mari,0,0)
        oled.show()
    elif show_img == 2 :
        oled.fill(0)
        oled.blit(fb_miwo,0,0)
        oled.show()
    sleep(0.1)
    
      
    sleep(0.1)

