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
time.sleep(2)

def read_serial_data():
    print("RAW DATA", ser.readline().decode().rstrip())
    data = int(ser.readline().decode().rstrip()) #read line of data, decode and convert to number
    data_inverted = abs(data - 100)  # invert data for better human interface handling
    print('SENSOR', data_inverted)
    ser.reset_input_buffer()
    return data_inverted
    # return data.decode().rstrip() # decode and strip r/n char

# def print_serial():
#     while(True): # read serial data on loop
#         time.sleep(2)
#         read_serial_data()

# print_serial()


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
