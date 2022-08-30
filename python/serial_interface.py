# Interface setup adapted from https://problemsolvingwithpython.com/

# Slack overflow Mac port commands
# You can find your Arduino via Terminal with

#     ls /dev/tty.*

# then you can read that serial port using the screen command, like this

#     screen /dev/tty.[yourSerialPortName] [yourBaudRate]

# for example:

#     screen /dev/tty.usbserial-A6004byf 9600


# serialInterface.py

import serial
import time

ser = serial.Serial('/dev/cu.usbserial-FTDK64TL', 9600)
time.sleep(2)
b = ser.readline() #readline() returns one line from a file
b
#b'409\r\n'
type(b)
#<class 'bytes'>
str_rn = b.decode()
str_rn
#'409\r\n'
str = str_rn.rstrip()
str
#'409'
type(str)
#<class 'str'>
f = float(str)
#409.0
type(f)
#<class 'float'>
print(f)
#ser.close()
#exit()