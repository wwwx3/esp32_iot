#Import Lib
from network import STA_IF , WLAN

#Create WLAN station interface (Client) 
wlan = WLAN(STA_IF)

#Activate WLAN station Mode
wlan.active(True)

#Check WLAN Status
#True == Connected / False == Unconected 
wlan_status = wlan.isconnected()
print (wlan_status)

#WLAN Nearby Scanning
wlan_list = wlan.scan()

#Print all informations
print("✨(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ Nearby Wi-Fi Networks ✧ﾟ･: *ヽ(◕ヮ◕ヽ)✨\n")
for i, wlan in enumerate(wlan_list):
    ssid = wlan[0].decode('utf-8')  # Decode SSID from bytes
    bssid = ':'.join(f'{b:02x}' for b in wlan[1])  # Format BSSID
    channel = wlan[2]
    rssi = wlan[3]
    authmode = wlan[4]
    print(f"{i + 1}. 🌟 SSID: {ssid}")
    print(f"    📡 BSSID: {bssid}")
    print(f"    📻 Channel: {channel}")
    print(f"    📶 Signal Strength (RSSI): {rssi} dBm")
    print(f"    🔒 Authentication Mode: {authmode}")
    print("    ｡*:☆彡 ~~~~~~~~~~~~~~ ｡*:☆彡\n")
