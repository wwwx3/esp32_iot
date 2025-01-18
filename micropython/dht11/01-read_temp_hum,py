#Import Library
from machine import Pin
from dht import DHT11
from time import sleep

#Pin Setup
dht_pin = DHT11(Pin(13))

while True :
    #Start measuring temperature/humidity
    dht_pin.measure()
    
    temperature = dht_pin.temperature()
    humidity = dht_pin.humidity()
    
    print("Temperature:{} Humidity: {}" .format(temperature,humidity))
    sleep(1)
    
