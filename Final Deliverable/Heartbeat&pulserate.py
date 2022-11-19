import time
import sys
import ibmiotf.application
import ibmiotf.device
import random


#Provide your IBM Watson Device Credentials
organization = "7vszt8"
deviceType = "Monitor"
deviceId = "1234"
authMethod = "token"
authToken = "12345678"

        


try:
	deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
	deviceCli = ibmiotf.device.Client(deviceOptions)
	#..............................................
	
except Exception as e:
	print("Caught exception connecting device: %s" % str(e))
	sys.exit()

# Connect and send a datapoint "hello" with value "world" into the cloud as an event of type "greeting" 10 times
deviceCli.connect()

# Initialize GPIO


def myCommandCallback(cmd):
    print("Command received: %s" % cmd.data['command'])
    status=cmd.data['command']
    if status=="pulse_rate":
        print ("pulse_rate monitored")
    else :
        print (" Heart_beat monitored")
   
    #print(cmd)
    
while True:
        #Get Sensor Data from ECG Sensor
        
        pulse_rate=random.randint(60,100)
        Heart_beat=random.randint(60,100)
        
        data = { 'pulse_rate' :pulse_rate, 'Heart_beat': Heart_beat }
        #print data
        def myOnPublishCallback():
             print ("Published  pulse_rate = %s bpm" % pulse_rate, "Heart_beat = %s bpm" % Heart_beat, "to IBM Watson")


        success = deviceCli.publishEvent("IoTSensor", "json", data, qos=0, on_publish=myOnPublishCallback)
        if not success:
            print("Not connected to IoTF")
        time.sleep(20)
        
        deviceCli.commandCallback = myCommandCallback

# Disconnect the device and application from the cloud
deviceCli.disconnect()
