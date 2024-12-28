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


# Show Network DATA
ip, subnet, gateway, dns = wlan.ifconfig()
print("\n｡*:☆ Detailed Network Information ☆:*｡\n")
print(f"🌐 IP Address      : {ip}")
print(f"🌐 Subnet Mask     : {subnet}")
print(f"🌐 Default Gateway : {gateway}")
print(f"🌐 DNS Server      : {dns}")
print("\n٩(｡•́‿•̀｡)۶ All set! Happy Networking~! ✨")

def mqtt_callback(topic,msg):
    topic,msg = topic.decode('utf8'),msg.decode('utf8')
    print("message from {} : {}" .format(topic,msg))
    
# Create MQTT Profile
mqtt = MQTTClient("myuuu", server=broker, port=port)
mqtt.set_callback(mqtt_callback)



print("\n (￣▽￣)ゞ MQTT Connecting... Please wait!~")

# Start MQTT connection
mqtt.connect()
print("(*^▽^*) MQTT Connected~! Ready to go! 🚀✨")

#Subscribe to topic
mqtt.subscribe("@msg/data")

while True:
    mqtt.check_msg()
    

