import wiringpi
import time
from wiringpi import GPIO

wiringpi.wiringPiSetup()

wiringpi.pinMode(4, GPIO.INPUT)
wiringpi.pinMode(2, GPIO.INPUT)

def xor(a,b):
	return (a and not b) or (not a and b)
		

while True:
	if wiringpi.digitalRead(4) == 0:
		a = False
		print("\nLED1 IS OFF")
	if wiringpi.digitalRead(4) == 1:
		a = True
		print("\nLED1 IS ON")
	if wiringpi.digitalRead(2) == 0:
		b = False
		print("\nLED2 IS OFF")
	if wiringpi.digitalRead(2) == 1:
		b = True
		print("\nLED2 IS ON")
	print("\nin1")
	print(a)
	print("in2")
	print(b)
	print("\nXOR:")
	print(xor(a,b))
	time.sleep(1)