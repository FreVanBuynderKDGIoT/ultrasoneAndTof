from network import LoRa
import socket
import ubinascii
import time
import ustruct

lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)
app_eui = ubinascii.unhexlify('70B3D57ED003E4C1')
app_key = ubinascii.unhexlify('802522436B3C6A2EEC1748B7FDB295FB')

counter = 0
connected = None

def joinLora():
    global counter
    global connected
    lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)
    while (not lora.has_joined() and counter <= 5):
        time.sleep(2.5)
        print('Not yet joined with LoRa')
        counter = counter + 1


    if(lora.has_joined()):
        print('Joined')
        connected = True
    else:
        connected = False
    return connected

def setSocket():
    global s
    s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
    s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)
    s.setblocking(True)

def sendBytes(data):
    setSocket()
    packet = ustruct.pack('f', data)
    s.send(packet)
    time.sleep(10)

def receiveData():
    data = s.recv(64)
    print(data)
