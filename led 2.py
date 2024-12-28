import wiringpi
import time
from wiringpi import GPIO

wiringpi.wiringPiSetup()
wiringpi.pinMode(2, GPIO.INPUT)
wiringpi.pinMode(4, GPIO.OUTPUT)
wiringpi.pinMode(3, GPIO.OUTPUT)

def reading():
	count = 0
	signal = ""
	while count < 4:
		if wiringpi.digitalRead(2) == 0:
			signal += "0"
		if wiringpi.digitalRead(2) == 1:
			signal += "1"
		print(signal)
		time.sleep(2)
		count += 1
	return signal
	
Y1 = {'0000':1,'0001':0,'0010':1,'0011':1,
'0100':0,'0101':1,'0110':1,'0111':0,
'1000':1,'1001':1,'1010':1,'1011':1,
'1100':0,'1101':1,'1110':0,'1111':1}

Y0 = {'0000':1,'0001':0,'0010':0,'0011':0,
'0100':1,'0101':1,'0110':0,'0111':0,
'1000':0,'1001':1,'1010':1,'1011':0,
'1100':0,'1101':0,'1110':1,'1111':0}	



while True:
	read = reading()
	if Y0[read] == 0:
		print("\nLED1 IS OFF")
		wiringpi.digitalWrite(4,0)
	elif Y0[read] == 1:
		print("\nLED1 IS ON")
		wiringpi.digitalWrite(4,1)
	if Y1[read] == 0:
		print("\nLED2 IS OFF")
		wiringpi.digitalWrite(3,0)
	elif Y1[read] == 1:
		print("\nLED2 IS ON")
		wiringpi.digitalWrite(3,1)
