import serial

ser = serial.Serial('/dev/ttyS7')  

ser.close()
ser.open()
    

ser.break_condition = True
#ser.write(b'1')

ser.close()