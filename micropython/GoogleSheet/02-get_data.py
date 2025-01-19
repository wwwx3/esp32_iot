#Import Lib
from network import WLAN,STA_IF
from ggsheet import MicroGoogleSheet

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

# Google Sheet Credential 
google_sheet_url = "https://docs.google.com/spreadsheets/d/17cj6r04YHYg1QOaa2DnE-93ybJkpCxAftzbyhh6B43U/edit?gid=0#gid=0"
google_sheet_name = "工作表1"
google_app_deployment_id = "AKfycbzcxltxRiGw7CfR3FZuxQl3i-24FgnhtERckjFArU8RoLnmBVoNN2sMW7O7zY8e9YoI"

# Create Instance 
ggsheet = MicroGoogleSheet(google_sheet_url,google_sheet_name)
ggsheet.set_DeploymentID(google_app_deployment_id)

#Get Data from googlesheet
data1 = ggsheet.getCell(1,1)
data2 = ggsheet.getCell(1,2)
data3 = ggsheet.getCell(1,3)
print(data1,data2,data3)
