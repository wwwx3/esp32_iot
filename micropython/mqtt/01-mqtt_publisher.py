#Import Lib
from umqtt . simple import MQTTClient
from network import STA_IF, WLAN

# Network Credential
ssid = "iMakeEDU"
pwd = "imake1234"

#MQTT Credential
broker = "broker.hivemq.com"
port = 1883

# Create Network Interface
wlan = WLAN(STA_IF)
wlan.active(True)

# Start Connection
if not wlan.isconnected():
    print("(￣^￣)ゞ Network Not Connected!~")
    wlan.connect(ssid, pwd)
    print("ヽ(・∀・)ﾉ Connecting...")

    # Wait until connected
    while not wlan.isconnected():
        pass

print("(★^O^★) Connected~!")
