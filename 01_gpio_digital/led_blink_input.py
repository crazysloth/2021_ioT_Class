# Git test
import RPi.GPIO as GPIO

LED_PIN = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

try:  #finally로 연결됨
    while True:
        val = input("1 : on, 0 : off, 9 : exit >")
        if(val == '0') :
            GPIO.output(LED_PIN, GPIO.LOW) #GPIO.LOW를 0으로 써도됨
            print("led off")
        elif(val == "1"): 
            GPIO.output(LED_PIN, GPIO.HIGH) #GPIO.HIGH를 1로 써도됨
            print("led on")
        elif(val == "9"):
            break
finally:
    GPIO.cleanup()
    print("cleanup and exit")
