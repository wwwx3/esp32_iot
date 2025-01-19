#import lib
from machine import Pin
from dht import DHT11
from time import sleep
from network import WLAN,STA_IF
from netpie import NETPIE

#Pin Setup
dht_pin = DHT11(Pin(13))

#Network Credential
ssid = "iMakeEDU"
pwd = "imake1234"

#Connect to network
wlan = WLAN(STA_IF)
wlan.active(True)

if not wlan.isconnected() :
    print("Connect to network:",ssid)
    wlan.connect(ssid,pwd)
    while not wlan.isconnected() :
        pass
print("Connected",ssid)


#NETPIE credential
client_id = "a7925eb5-3128-4e5e-ba1c-0d91293ddd48"
token = "Zs7xdceKaxLaU5Q4QHDyytxTh1PkYN9c"
secret = "5Vk7NyTJht8aqUCcMtN8EKNTmBbxRE6y"

#Create Netpie profile
netpie = NETPIE()
netpie.set_profile(client_id,token,secret)
netpie.connect()

while True :
    #Temp/Humidity Measurement
    dht_pin.measure()
    #Read Temperature
    temperature = dht_pin.temperature()
    humidity = dht_pin.humidity()
    
    payload = {
        "Temperature": temperature,
        "Humidity": humidity,
        }
    #Publish payload to NETPIE Shadow
    netpie.publishShadow(payload)