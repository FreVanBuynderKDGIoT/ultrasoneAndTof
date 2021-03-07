from machine import UART
import machine
import pycom
import time

data = [0, 0, 0, 0]
uart = UART(1, 9600)
header = b'\xff'

def setuart():
    uart.init(9600, bits=8, parity=None, stop=1, timeout_chars=100, pins=('P3', 'P4'))

def checkHeader():
    header_read = uart.read(1)
    while (header_read != header):
        header_read = uart.read(1)

def readData():
    checkHeader()
    dataH = int(uart.read(1)[0])
    dataL = int(uart.read(1)[0])
    checksum = int(uart.read(1)[0])
    if (checkChecksum(dataH, dataL, checksum)):
        distance = getDistance(dataH, dataL)
        print("distance: " + "{:5.1f}".format(distance) +  " cm")
        return distance
    else:
        return False

def checkChecksum(dataH, dataL, checksum):
    sum = (dataH + dataL - 1)
    if (sum == checksum):
        return True
    else:
        return False

def getDistance(dataH, dataL):
    distance = ((dataH * 256) + dataL)
    distance_centimeters = distance/10
    return distance_centimeters
