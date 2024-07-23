#!/usr/bin/env python3

def avr_lookup(signature):
    if str(hex(signature) == "0x1E9483"):
         return ("AT90PWM[23]16")
    if str(hex(signature) == "0x1E9383"):
         return ("AT90PWM[23]B")
    if str(hex(signature) == "0x1E9388"):
         return ("AT90PWM81")
    if str(hex(signature) == "0x1E96C1"):
         return ("AT90SCR100")
    if str(hex(signature) == "0x1E9382"):
         return ("ATA6289")
    if str(hex(signature) == "0x1E9781"):
         return ("CAN128")
    if str(hex(signature) == "0x1E9581"):
         return ("CAN32")
    if str(hex(signature) == "0x1E9681"):
         return ("CAN64")
    if str(hex(signature) == "0x1E9703"):
         return ("ATmega1280")
    if str(hex(signature) == "0x1E9704"):
         return ("ATmega1281")
    if str(hex(signature) == "0x1E9705"):
         return ("ATmega1284P")
    if str(hex(signature) == "0x1EA701"):
         return ("ATmega128RFA1")
    if str(hex(signature) == "0x1E9401"):
         return ("ATmega161")
    if str(hex(signature) == "0x1E9404"):
         return ("ATmega162")
    if str(hex(signature) == "0x1E9402"):
         return ("ATmega163")
    if str(hex(signature) == "0x1E940F"):
         return ("ATmega164")
    if str(hex(signature) == "0x1E9407"):
         return ("ATmega165[P]")
    if str(hex(signature) == "0x1E940B"):
         return ("ATmega168P")
    if str(hex(signature) == "0x1E9405"):
         return ("ATmega169[P][A]")
    if str(hex(signature) == "0x1E9403"):
         return ("ATmega16[A]")
    if str(hex(signature) == "0x1E940C"):
         return ("ATmega16HVA")
    if str(hex(signature) == "0x1E940E"):
         return ("ATmega16HVA2")
    if str(hex(signature) == "0x1E940D"):
         return ("ATmega16HVB")
    if str(hex(signature) == "0x1E9484"):
         return ("ATmega16M1")
    if str(hex(signature) == "0x1E9489"):
         return ("ATmega16U2")
    if str(hex(signature) == "0x1E9488"):
         return ("ATmega16U4")
    if str(hex(signature) == "0x1E9801"):
         return ("ATmega2560")
    if str(hex(signature) == "0x1E9802"):
         return ("ATmega2561")
    if str(hex(signature) == "0x1E9502"):
         return ("ATmega32")
    if str(hex(signature) == "0x1E9501"):
         return ("ATmega323")
    if str(hex(signature) == "0x1E9511"):
         return ("ATmega324PA")
    if str(hex(signature) == "0x1E9505"):
         return ("ATmega325")
    if str(hex(signature) == "0x1E9506"):
         return ("ATmega3250")
    if str(hex(signature) == "0x1E950F"):
         return ("ATmega328P")
    if str(hex(signature) == "0x1E9503"):
         return ("ATmega329")
    if str(hex(signature) == "0x1E9504"):
         return ("ATmega3290")
    if str(hex(signature) == "0x1E9586"):
         return ("ATmega32C1")
    if str(hex(signature) == "0x1E9510"):
         return ("ATmega32HVB")
    if str(hex(signature) == "0x1E9584"):
         return ("ATmega32M1")
    if str(hex(signature) == "0x1E958A"):
         return ("ATmega32U2")
    if str(hex(signature) == "0x1E9587"):
         return ("ATmega32U4")
    if str(hex(signature) == "0x1E9588"):
         return ("ATmega32U6")
    if str(hex(signature) == "0x1E9507"):
         return ("ATmega406")
    if str(hex(signature) == "0x1E920A"):
         return ("ATmega48P")
    if str(hex(signature) == "0x1E9608"):
         return ("ATmega640")
    if str(hex(signature) == "0x1E9609"):
         return ("ATmega644")
    if str(hex(signature) == "0x1E960A"):
         return ("ATmega644P[A]")
    if str(hex(signature) == "0x1E9605"):
         return ("ATmega645")
    if str(hex(signature) == "0x1E9606"):
         return ("ATmega6450")
    if str(hex(signature) == "0x1E9603"):
         return ("ATmega649")
    if str(hex(signature) == "0x1E9604"):
         return ("ATmega6490")
    if str(hex(signature) == "0x1E960B"):
         return ("ATmega649")
    if str(hex(signature) == "0x1E9686"):
         return ("ATmega64C1")
    if str(hex(signature) == "0x1E9610"):
         return ("ATmega64HVE")
    if str(hex(signature) == "0x1E9684"):
         return ("ATmega64M1")
    if str(hex(signature) == "0x1E9307"):
         return ("ATmega8")
    if str(hex(signature) == "0x1E9306"):
         return ("ATmega8515")
    if str(hex(signature) == "0x1E9308"):
         return ("ATmega8535")
    if str(hex(signature) == "0x1E930F"):
         return ("ATmega88P[A]")
    if str(hex(signature) == "0x1E9389"):
         return ("ATmega8U2")
    if str(hex(signature) == "0x1E9003"):
         return ("ATtiny10")
    if str(hex(signature) == "0x1E9007"):
         return ("ATtiny13")
    if str(hex(signature) == "0x1E9487"):
         return ("ATtiny167")
    if str(hex(signature) == "0x1E910F"):
         return ("ATtiny20")
    if str(hex(signature) == "0x1E910A"):
         return ("ATtiny2313[A]")
    if str(hex(signature) == "0x1E910B"):
         return ("ATtiny24[A]")
    if str(hex(signature) == "0x1E9108"):
         return ("ATtiny25")
    if str(hex(signature) == "0x1E910C"):
         return ("ATtiny261[A]")
    if str(hex(signature) == "0x1E900A"):
         return ("ATtiny4")
    if str(hex(signature) == "0x1E920E"):
         return ("ATtiny40")
    if str(hex(signature) == "0x1E920D"):
         return ("ATtiny4313")
    if str(hex(signature) == "0x1E920C"):
         return ("ATtiny43U")
    if str(hex(signature) == "0x1E9207"):
         return ("ATtiny44[A]")
    if str(hex(signature) == "0x1E9206"):
         return ("ATtiny45")
    if str(hex(signature) == "0x1E9208"):
         return ("ATtiny461[A]")
    if str(hex(signature) == "0x1E9209"):
         return ("ATtiny48")
    if str(hex(signature) == "0x1E9009"):
         return ("ATtiny5")
    if str(hex(signature) == "0x1E930C"):
         return ("ATtiny84[A]")
    if str(hex(signature) == "0x1E930B"):
         return ("ATtiny85")
    if str(hex(signature) == "0x1E930D"):
         return ("ATtiny861[A]")
    if str(hex(signature) == "0x1E9387"):
         return ("ATtiny87")
    if str(hex(signature) == "0x1E9311"):
         return ("ATtiny88")
    if str(hex(signature) == "0x1E9008"):
         return ("ATtiny9")
    if str(hex(signature) == "0x1E9782"):
         return ("AT90USB128[67]")
    if str(hex(signature) == "0x1E9482"):
         return ("AT90USB162")
    if str(hex(signature) == "0x1E9682"):
         return ("AT90USB64[67]")
    if str(hex(signature) == "0x1E974C"):
         return ("ATxmega128A1")
    if str(hex(signature) == "0x1E9742"):
         return ("ATxmega128A3")
    if str(hex(signature) == "0x1E9748"):
         return ("ATxmega128D3")
    if str(hex(signature) == "0x1E9441"):
         return ("ATxmega16A4")
    if str(hex(signature) == "0x1E9442"):
         return ("ATxmega16D4")
    if str(hex(signature) == "0x1E9744"):
         return ("ATxmega192A3")
    if str(hex(signature) == "0x1E9749"):
         return ("ATxmega192D3")
    if str(hex(signature) == "0x1E9842"):
         return ("ATxmega256A3")
    if str(hex(signature) == "0x1E9843"):
         return ("ATxmega256A3B")
    if str(hex(signature) == "0x1E9844"):
         return ("ATxmega256D3")
    if str(hex(signature) == "0x1E9541"):
         return ("ATxmega32A4")
    if str(hex(signature) == "0x1E9542"):
         return ("ATxmega32D4")
    if str(hex(signature) == "0x1E964E"):
         return ("ATxmega64A1")
    if str(hex(signature) == "0x1E9642"):
         return ("ATxmega64A3")
    if str(hex(signature) == "0x1E964A"):
         return ("ATxmega64D3")
