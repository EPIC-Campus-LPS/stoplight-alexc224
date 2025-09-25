import RPi.GPIO as GPIO
import time
def LED_CYCLE():
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(18,GPIO.OUT)
	GPIO.setup(17,GPIO.OUT)
	GPIO.setup(16,GPIO.OUT)
	#Green LED on and off
	print ("Green LED on")
	GPIO.output(18,GPIO.HIGH)
	time.sleep(5)
	print ("Green LED off")
	GPIO.output(18,GPIO.LOW)

	#Yellow LED on and off)
	print ("Yellow LED on")
	GPIO.output(17,GPIO.HIGH)
	time.sleep(1)
	print ("Yellow LED off")
	GPIO.output(17,GPIO.LOW)

	#Red LED on and off
	print ("Red LED on")
	GPIO.output(16,GPIO.HIGH)
	time.sleep(4)
	print ("Red LED off")
	GPIO.output(16,GPIO.LOW)
def main():
	LED_CYCLE()
	print("Done")
	
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21, GPIO.IN)

while True:
	if GPIO.input(21) == 1:
		continue
	elif GPIO.input(21) == 0:
		break
print("Button Pressed")
time.sleep(0.5)
main()
