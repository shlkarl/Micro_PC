import wiringpi
import time
import Def
from wiringpi import GPIO

wiringpi.wiringPiSetup()
wiringpi.pinMode(2, GPIO.INPUT)


def reading():
	count = 0
	signal = ""
	while count < 3:
		if wiringpi.digitalRead(2) == 0:
			signal += "0"
		if wiringpi.digitalRead(2) == 1:
			signal += "1"
		print(signal)
		time.sleep(2)
		count += 1
	return signal

adr = {'000': "+",'001': "-", '010': "--",'011': "*",
'100':"/",'101':"//",'110':"%",'111':"%%"}

while True:
	A = int(input("input A: "))
	B = int(input("input B: "))

	read = reading()
	print("result: ")
	Def.calc(adr[read], A, B)
