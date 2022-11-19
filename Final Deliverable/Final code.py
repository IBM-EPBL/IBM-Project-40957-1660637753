
import json
import wiotp.sdk.device
import time

myConfig = {
    "identity": {
        "orgId": "7vszt8",
        "typeId": "Monitor",
        "deviceId":"1234"
    },
    "auth": {
        "token": "12345678"
     }
}
client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
        name="locationtracker"
        #in area location

        #latitude=17.4225176
        #longitude=78.5458842

        #out area location
        latitude=17.4225176
        longitude=78.5458842
        myData={'name': name,'la':latitude,'lo':longitude}
        client.publishEvent(eventId="status",msgFormat="json", data=myData, qos=0, onPublish=None)
        print("Data published to IBM IoT plpatform: ",myData)
        time.sleep(5)

client.disconnect()7vs
