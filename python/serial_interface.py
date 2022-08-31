#For arduino address in Terminal type 'ls /dev/tty.*'

import serial
import time
import os
import pty

# primary, secondary = pty.openpty()
# if '/dev/cu.usbserial-FTDK64TL' == True:
#     PORT = '/dev/cu.usbserial-FTDK64TL' # arduino usb port
# else: 
#     PORT = os.ttyname(secondary) #virtual test port

PORT = '/dev/cu.usbserial-FTDK64TL'
# print('🟡', PORT)

ser = serial.Serial(PORT, 9600) #port name, baud rate
time.sleep(1)

def read_serial_data():
    data = ser.readline() #read line of data
    print(data.decode().rstrip()) 
    return data.decode().rstrip() # decode and strip r/n char

# ser.close()
# exit()


# import serial
# import time



# BELOW CODE WORKS WHEN ARDUINO IS HOOKED UP!!

# PORT = '/dev/cu.usbserial-FTDK64TL' # arduino usb port
# ser = serial.Serial(PORT, 9600) #port name, baud rate
# time.sleep(1)

# def read_serial_data():
#     data = ser.readline() #read line of data
#     print(data.decode().rstrip()) 
#     return data.decode().rstrip() # decode and strip r/n char
