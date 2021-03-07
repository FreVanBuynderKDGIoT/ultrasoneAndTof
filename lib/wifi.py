from network import WLAN
import machine
import time
import requests as requests

wlan = WLAN(mode=WLAN.STA)
ssid1 = 'IoT'
passwd1 = 'KdGIoT92!'

ssid2 = 'telenet-18FDC'
passwd2 = 'Amortje2016'

counter = 0
connected = None

def connectWifi():
    global counter
    global connected
    wlan.connect(ssid=ssid1, auth=(WLAN.WPA2, passwd1))
    while (not wlan.isconnected() and (counter <= 5)):
        print("not yet connected with wifi 1")
        time.sleep(2)
        counter += 1
    counter = 0
    if not wlan.isconnected():
        wlan.connect(ssid=ssid2, auth=(WLAN.WPA2, passwd2))
        while (not wlan.isconnected() and counter <= 5):
            print("not yet connected with wifi 2")
            time.sleep(2)
            counter += 1
    if wlan.isconnected():
        print('wifi connected')
        print(wlan.ifconfig())
        connected = True
    else:
        connected = False

    return connected
