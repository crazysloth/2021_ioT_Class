#내부풀업저항, 내부풀다운저항 사용하기
import RPi.GPIO as GPIO
import time

SWITCH_PIN = 2
LED_PIN = 3
GPIO.setmode(GPIO.BCM)
#GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP) #내부풀업저항
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #내부풀다운저항]
GPIO.setup(LED_PIN, GPIO.OUT)

try:
    while True:
        val = GPIO.input(SWITCH_PIN)
        print(val)
        GPIO.output(LED_PIN, val)
finally:
    GPIO.cleanup()
    print("cleanup and exit")
