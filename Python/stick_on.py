import serial
import time

ser = serial.Serial('/dev/ttyUSB0') # configure device name: '/dev/ttyUSBx' or 'COMx'

ser.rts = False # True: RTS = 0 (power off), False: RTS = 1 (power on)
ser.write(b'\xAA') # send arbitrary data to clock in the RTS state on the flip flop

time.sleep(0.1) # neccesarry on Unix, can be omitted on Windows

ser.close()