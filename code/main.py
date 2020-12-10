from machine import I2C
from bme280 import *
import utime
from network import LoRa
import binascii
import machine
import pycom
import socket
import ustruct

# setup i2c for BME280 sensor
i2c=I2C()
bme280 = BME280(i2c=i2c)

# disable LED heartbeat (so we can control the LED)
pycom.heartbeat(False)

# set LED to red
pycom.rgbled(0x7f0000)

lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.AS923)

# access info
app_eui = binascii.unhexlify('XXXXXXXXXXXXXXXX') #Insert you Application EUI here keeping ''
app_key = binascii.unhexlify('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX') #Insert you Application Key here keeping ''

# attempt join - continues attempts background
lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)

# wait for a connection
print('Waiting for LoRaWAN network connection...')
while not lora.has_joined():
	utime.sleep(1)
	# if no connection in a few seconds, then reboot
	if utime.time() > 30:
		print("possible timeout")
		machine.reset()
	pass

# we're online, set LED to green and notify via print
pycom.rgbled(0x004600)
print('Network joined!')

# setup the socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)
s.setblocking(False)
s.bind(1)

# Main code loop for reading and uploading weather data

while True:
    pycom.rgbled(0x00007d)
    print(bme280.values)
    values = bme280.read_compensated_data(result = None)
    temperature = values[0]
    pressure = values[1]
    humidity = values[2]

    packet = ustruct.pack('fff', temperature, pressure, humidity)
    s.send(packet)

    pycom.rgbled(0x004600)
    utime.sleep(120)
