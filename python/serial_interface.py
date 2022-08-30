#Find Arduino via Terminal with # ls /dev/tty.*

import serial
import time

ser = serial.Serial('/dev/cu.usbserial-FTDK64TL', 9600) #port name, baud rate

def read_serial_data():
    data = ser.readline() #read line of data
    print(data.decode().rstrip()) # decode and strip r/n char
    return data.decode().rstrip()

# ser.close()
# exit()