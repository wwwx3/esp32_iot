from machine import Pin, SoftI2C
from ssd1306 import SSD1306_I2C
from dht import DHT11
from time import sleep

#Pin Setup
dht_pin = DHT11(Pin(13))

i2c = SoftI2C( sda=Pin(21),scl=Pin(22))
oled = SSD1306_I2C(128,64,i2c)

while True :
    #Start measuring temperature/humidity
    dht_pin.measure()
    
    #Read 
    temperature = dht_pin.temperature()
    humidity = dht_pin.humidity()
    
    print("Temperature:{} Humidity: {}" .format(temperature,humidity))
    sleep(1)
    
    oled.fill(0)
    oled.text("Temp:",0,0)
    oled.text(str(temperature),50,0)
    oled.text("Humid",0,10)
    oled.text(str(humidity),50,10)
    oled.show()
    sleep(1)
