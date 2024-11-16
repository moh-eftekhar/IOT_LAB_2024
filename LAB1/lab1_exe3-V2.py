import json
import datetime as dt

class DeviceCatalog:
    def __init__(self, catalog_file):
        self.catalog_file = catalog_file
        with open(catalog_file, "r") as f:
            self.catalog = json.load(f)

    def search_by_name(self, devicename):
        devices = self.catalog.get("devicesList", [])
        for device in devices:
            if device.get("deviceName") == devicename:
                return device
        return None

    def search_by_id(self, deviceid):
        devices = self.catalog.get("devicesList", [])
        for device in devices:
            if device.get("deviceID") == deviceid:
                return device
        return None

    def search_by_service(self, servicename):
        result = []
        devices = self.catalog.get("devicesList", [])
        for device in devices:
            if servicename in device.get("availableServices", []):
                result.append(device)
        return result

    def search_by_measurement(self, measure_type):
        result = []
        devices = self.catalog.get("devicesList", [])
        for device in devices:
            if measure_type in device.get("measureType", []):
                result.append(device)
        return result

    def insert_device(self, new_device):
        devices = self.catalog.get("devicesList", [])
        existing_device = None
        for device in devices:
            if device.get("deviceID") == new_device.get("deviceID"):
                existing_device = device
                break

        if existing_device:
            update = input(f"Device with ID {new_device.get('deviceID')} already exists. Do you want to update it? (y/n) ")
            if update.lower() == "y":
                existing_device.update(new_device)
                existing_device["lastUpdate"] = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"Device with ID {new_device.get('deviceID')} has been updated")
        else:
            new_device["lastUpdate"] = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            devices.append(new_device)
            print(f"Device with ID {new_device.get('deviceID')} has been added")

        with open(self.catalog_file, "w") as f:
            json.dump(self.catalog, f, indent=4)
        print("Catalog has been updated")

# Example usage
if __name__ == "__main__":
    catalog = DeviceCatalog("catalog.json")

    # Example searches
    device_name = catalog.search_by_name("VCNL4010")
    print(json.dumps(device_name, indent=4))

    device_id = catalog.search_by_id(1)
    print(json.dumps(device_id, indent=4))

    device_service = catalog.search_by_service("MQTT")
    print(json.dumps(device_service, indent=4))

    measure_service = catalog.search_by_measurement("Proximity")
    print(json.dumps(measure_service, indent=4))

    # Example insertion
    new_device = {
        "deviceID": 4,
        "deviceName": "DHT1123",
        "measureType": ["Pressure", "Temperature", "Humidity"],
        "availableServices": ["MQTT", "REST"],
        "servicesDetails": [
            {
                "serviceType": "MQTT",
                "topic": ["MySmartThingy/4/pressure"]
            },
            {
                "serviceType": "REST",
                "serviceIP": "newdevice.org:8080"
            }
        ]
    }

    catalog.insert_device(new_device)