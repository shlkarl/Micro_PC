import wiringpi
import time
from wiringpi import GPIO

wiringpi.wiringPiSetup()
wiringpi.pinMode(2, GPIO.INPUT)

def protect():
	while True:
		while wiringpi.digitalRead(2) == 0:
			time.sleep(0.5)
			count += 1
			print(0)
			if count == 8:
				return 0
		count = 0
		while wiringpi.digitalRead(2) == 1:
			time.sleep(0.5)
			count += 1
			print(1)
			if count == 8:
				return 1
		count = 0
		

ka = {'A': ['F', 'B'],
      'B': ['F', 'C'],
	  'C': ['F', 'D'],
      'D': ['F', 'E'],
      'E': ['F', 'E'],
      'F': ['G', 'B'],
      'G': ['H', 'B'],
      'H': ['I', 'B'],
      'I': ['I', 'B']}

state = 'A'	

while True:
	print(state)
	state = ka[state][protect()]
