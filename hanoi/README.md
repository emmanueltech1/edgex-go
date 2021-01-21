# EdgeX Foundry Services - Software Defined Radio Devices

This device will be created using python scripts to showcase how to use the EdgeX Foundry REST APIs.
The SDR sensor cluster, which will be generating I and Q data, will be created with the following steps:

● Create value descriptors
Value descriptors are what they sound like. They describe a value. They tell EdgeX what
format the data comes in and what to label the data with. In this case value descriptors
are created for temperature and humidity values respectively.

● Upload the device profile
The device profile describes a type of device within the EdgeX system. Each device managed by a device service has an association with a device profile, which defines that device type in terms of the operations which it supports.

● Create the device
Now EdgeX is finally ready to receive the device creation command in python script as
follows:
Two items are particularly important in this JSON body:
 - The device service “edgex-device-rest” is used since this is a REST device.
 - The profile name “SDR-Sensor-HackRF” must match the name in the device profile yaml
file uploaded in the previous step.

## Get Started
 - Create virtual environment (name: “venv”)
```sh
python3 -m venv venv
```
- Enter virtual environment
```sh
. ./venv/bin/activate
```
- Install Python modules
```sh
pip install -r requirements.txt
```
- Create EdgeX Services
```sh
docker-compose up -d
```
- Run python script to add device(sensor) to EdgeX Registry
```sh
python3 ./createSDRRESTDevice.py -ip 127.0.0.1 -devip 127.0.0.1
```
- Run python script to send data to EdgeX internal Database (Redis)
```sh
python3 ./genSDRData.py 
```
To view the readings beening sent from the edge device use the following REST API call:

http://localhost:48080/api/v1/reading
