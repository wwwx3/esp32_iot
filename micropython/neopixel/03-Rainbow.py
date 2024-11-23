from machine import Pin, PWM
from time import sleep

# Define PWM pins for Red, Green, and Blue
red = PWM(Pin(23))  # Replace with your GPIO pin
green = PWM(Pin(23))
blue = PWM(Pin(23))

# Set PWM frequency
red.freq(1000)
green.freq(1000)
blue.freq(1000)

# Function to set RGB values (0-1023 for MicroPython PWM duty cycle)
def set_color(r, g, b):
    red.duty_u16(int(r * 65535 / 255))   # Scale to 16-bit for MicroPython
    green.duty_u16(int(g * 65535 / 255))
    blue.duty_u16(int(b * 65535 / 255))

# Rainbow effect function
def rainbow_cycle(wait=0.1):
    while True:
        for i in range(255):
            r = (i & 0x80) >> 7 * 255
            g = (i & 0x40) -->
 sleep
