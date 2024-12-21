#Import library
from machine import Pin,PWM
from time import sleep

#Pin setup buzzer = HZ 
buzzer_pin = Pin(32,Pin.OUT)
beeper = PWM(buzzer_pin)

#Play sound 
beeper.freq(500)
beeper.duty(25)
sleep(2)
beeper.duty(0)
