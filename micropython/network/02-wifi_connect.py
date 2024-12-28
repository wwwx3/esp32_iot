from network import STA_IF, WLAN

# Network Credential
ssid = "iMakeEDU"
pwd = "imake1234"

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


