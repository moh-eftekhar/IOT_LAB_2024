import json

with open("catalog.json", "r") as f:
    catalog = json.load(f)
# a = catalog["devicesList"][*]["availableServices"]
# print(json.dumps(a, indent=4))

# get the value of the key devicesList
def searchByname (devicename):
    device = catalog.get("devicesList",[])
    for devices in device:
        if devices.get("deviceName") == devicename:
            return devices
    
def searchById (deviceid):
    device = catalog.get("devicesList",[])
    for devices in device:
        if devices.get("deviceID") == deviceid:
            return devices
        
def searchByserice(servicename):
    result = []
    devices = catalog.get("devicesList",[])
    for device in devices:
        if servicename in device.get("availableServices",[]):
            result.append(device)
    
    return result



# Device_name = searchByname("VCNL4010")
# print(json.dumps(Device_name, indent=4))

# Device_id = searchById(1)
# print(json.dumps(Device_id, indent=4))

Device_service = searchByserice("MQTT")
print(json.dumps(Device_service, indent=4))
