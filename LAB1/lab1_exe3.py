# import json
# import datetime as dt

# with open("catalog.json", "r") as f:
#     catalog = json.load(f)
# # a = catalog["devicesList"][*]["availableServices"]
# # print(json.dumps(a, indent=4))

# # get the value of the key devicesList
# def searchByname (devicename):
#     device = catalog.get("devicesList",[])
#     for devices in device:
#         if devices.get("deviceName") == devicename:
#             return devices
    
# def searchById (deviceid):
#     device = catalog.get("devicesList",[])
#     for devices in device:
#         if devices.get("deviceID") == deviceid:
#             return devices
        
# def searchByserice(servicename):
#     result = []
#     devices = catalog.get("devicesList",[])
#     for device in devices:
#         if servicename in device.get("availableServices",[]):
#             result.append(device)
    
#     return result


# def searchByMeasurement(measure_Type):
#     result = []
#     devices = catalog.get("devicesList",[])
#     for device in devices:
#         if measure_Type in device.get("measureType",[]):
#             result.append(device)
    
#     return result


# def insertDevice(newDevice):
#     devices = catalog.get("devicesList",[])
#     existin_device = None
#     for device in devices:
#         if device.get("deviceID") == newDevice.get("deviceID"):
#             existin_device = device
#             break
   
#     if existin_device:
#         update = input(f"Device with ID {newDevice.get('deviceID')} already exists. Do you want to update it? (y/n)")
#         if update == "y":
#             existin_device.update(newDevice)
#             existin_device["lastUpdate"] = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#             print(f"Device with ID {newDevice.get('deviceID')} has been updated")
#     else:
#         newDevice["lastUpdate"] = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         devices.append(newDevice)
#         print(f"Device with ID {newDevice.get('deviceID')} has been added")

#     with open("catalog.json", "w") as f:
#         json.dump(catalog, f, indent=4)
#     print("Catalog has been updated")

    

    

# # Device_name = searchByname("VCNL4010")
# # print(json.dumps(Device_name, indent=4))

# # Device_id = searchById(1)
# # print(json.dumps(Device_id, indent=4))

# # Device_service = searchByserice("MQTT")
# # print(json.dumps(Device_service, indent=4))

# # Measure_Service = searchByMeasurement("Proximity")
# # print(json.dumps(Measure_Service, indent=4))

# new_device = {
#     "deviceID": 4,
#     "deviceName": "DHT1123",
#     "measureType": ["Pressure", "Temperature", "Humidity"],
#     "availableServices": ["MQTT", "REST"],
#     "servicesDetails": [
#         {
#             "serviceType": "MQTT",
#             "topic": ["MySmartThingy/4/pressure"]
#         },
#         {
#             "serviceType": "REST",
#             "serviceIP": "newdevice.org:8080"
#         }
#     ]
# }

# insertDevice(new_device)