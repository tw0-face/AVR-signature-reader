import serial
from time import sleep
import sys
import sig_table


ser = serial.Serial(str(sys.argv[1]))  
ser.close()
ser.open()

def mosi(x):
    ser.dtr = x

def miso():
    return ser.dsr

def sck(x):
    ser.rts = x

def resetpulse():
    ser.write(b'0')

def resetoff():
    ser.break_condition = True

def reseton():
    ser.break_condition = False



def xfr(b): 
    r = 0
    for i in range(8):
        if(b&(128>>i)):
            mosi(1)
        else:
            mosi(0)
        sleep(0.001)#idelay
        sck(1)
        sleep(0.001)#idelay
        v = miso()
        sck(0)
        if v:
            r |= (128>>i)
    return r

def xfrxpct(b, r):
    rb = xfr(b)
    if rb!= r:
        print("Error")
        return 1
    else:
        return 0    




def readsignature():
    signature = 0
    for i in range(3):
        if(xfrxpct(0x30,0x00)) :
            return(1);
        if(xfrxpct(0x00,0x30)):
            return(1);
        if(xfrxpct(i,0x00)):
            return(1);
        signature<<=8;
        b=xfr(0x00);
        signature|=b;
    avr_type = sig_table.avr_lookup(signature=signature)
    print("part :" + avr_type )

def programinit():
    sck(0)
    reseton()
    for i in range(5):
        sleep(0.2)
        resetpulse()
        sleep(0.05)
        xfr(0xAC);
        xfr(0x53);
        if xfrxpct(0x00,0x53):
            print('could not initialize')
            break
        xfr(0x00)
    readsignature()

    
programinit()
ser.close()