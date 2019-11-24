import time
import random
#import os #to execute relay script
#import RPI.GPIO as GPIO #to use GPIO pins for Sensor and actuators 
import urllib3#to use thingspeak URL to see Graphs

def read_from_sensor():
	temp = random.randint(25,45)
	hum = random.randint(50,60)
	air = random.randint(55,60)
	light= random.randint(100,180)
	return temp,hum,air,light

while(1):
	temp,hum,air,light = read_from_sensor()
	print("Temperature",temp, chr(176) + "C")
	print("Humidity",hum,"%rH")

	time.sleep(2.0)
	baseURL = "https://api.thingspeak.com/update?api_key=GIL5HB8CS8YU29ZK"

	g = urllib3.urlopen(baseURL + "&field1=%d, &field2=%d" % (temp,hum))

	time.sleep(0.01)
