#import lib
from machine import Pin
from time import sleep
from network import WLAN,STA_IF
from netpie import NETPIE
from neopixel import NeoPixel


#Pin Setup
np = NeoPixel(Pin(23),2)

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

#CallBack Function
def on_message(topic,msg):
    topic,msg = topic.decode('utf8'),msg.decode('utf8')
    
    print('message from{} : {}' .format(topic,msg))
    
    #Check message
    if msg == "led-on":
        np[0] = (10,10,10)
        np[1] = (10,10,10)
        np.write()
    elif msg == "led-off":
        np[0] = (0,0,0)
        np[1] = (0,0,0)
        np.write()

#Create Netpie profile
netpie = NETPIE()
netpie.set_profile(client_id,token,secret)
netpie.set_callback(on_message)
netpie.connect()

netpie.subscribe("@msg/data")

while True :
    netpie.check_message()
    sleep(1)
