import json

# Load the JSON file
with open('catalog.json', 'r') as file:
    data = json.load(file)

# Function to search for devices by name
def searchByName(device_name):
    devices = data.get('devicesList', [])
    results = [device for device in devices if device.get('deviceName') == device_name]
    
    if results:
        for device in results:
            print(json.dumps(device, indent=4))
    else:
        print(f"No devices found with the name: {device_name}")

# Function to search for devices by ID
def searchByID(device_id):
    devices = data.get('devicesList', [])
    device = next((device for device in devices if device.get('deviceID') == device_id), None)
    
    if device:
        print(json.dumps(device, indent=4))
    else:
        print(f"No device found with ID: {device_id}")

# Example usage
# device_name = input("Enter the name of the device you want to search for: ")
# searchByName("device_name")
device_ID = int(input("Enter the ID of the device you want to search for: "))
searchByID(device_ID)
