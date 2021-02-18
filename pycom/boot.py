from network import WLAN
import machine
import pycom

pycom.heartbeat(True)

wlan = WLAN(mode=WLAN.STA)
#wlan.connect(ssid='IoT', auth=(WLAN.WPA2, 'KdGIoT92!'))
wlan.connect(ssid='telenet-18FDC', auth=(WLAN.WPA2, 'Amortje2016'))
while not wlan.isconnected():
    machine.idle()

print("WiFi connected succesfully")
print(wlan.ifconfig())
