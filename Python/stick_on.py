import serial
#ser = serial.Serial('/dev/ttyUSB0') # open serial port (UNIX)
ser = serial.Serial('COM5') # open serial port (Windows)

# True: RTS = 0, False: RTS = 1

ser.setRTS(False) # power on
#ser.setRTS(True) # power off

ser.write(b'\xAA') # send arbitrary data to clock in the RTS state on the flip flop

ser.close()
