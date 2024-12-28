import wiringpi
import time
import Def
from wiringpi import GPIO

wiringpi.wiringPiSetup()
wiringpi.pinMode(2, GPIO.INPUT)

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
	
adr = {'0000': "0",'0001': "1", '0010': "2",'0011': "3",
'0100':"4",'0101':"5",'0110':"6",'0111':"7",
'1000':"8",'1001':"9",'1010':"a",'1011':"b",
'1100':"c",'1101':"d",'1110':"e",'1111':"f", '0':"_"}

mode = input("mode: ")

while mode == "0":
	date = input("example date input: 23112000 \ndate: ")
	for i in range(8):
		Def.ind(date[i])
		time.sleep(2)
		if i == 1 or i == 3:
			Def.ind(adr['0'])
		
		
while mode == "1":
	read = reading()
	Def.ind(adr[read])
	
while mode == "2":
	list_num = []
	num = int(input("example num input: 0123 \nnum: "))
	for i in range(4):
		list_num.append(int(num%10))
		num/=10
	list_num.reverse()
	print(list_num)
	print("type 1:")
	for i in range(4):
		Def.ind(str(list_num[i]))

	print("type 2:")
	for i in range(4):
		if list_num[i] == 0:
			continue
		Def.ind(str(list_num[i]))
