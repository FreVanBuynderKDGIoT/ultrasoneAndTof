import ultrasone
import wifi
import adafruitiowifi
import lora
import time

data = False

if(lora.joinLora()):
    print('there is a connection with LoRa')
    while True:
        ultrasone.setuart()
        data = ultrasone.readData()
        if (data != False):
            lora.sendBytes(data)
elif(wifi.connectWifi()):
    print('there is a connection with wifi')
    while True:
        ultrasone.setuart()
        data = ultrasone.readData()
        if(data != False):
            adafruitiowifi.sendDataWifi(data)

else:
    print("there is no connection with adafruit io")
