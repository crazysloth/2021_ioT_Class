#servo_motor.py
import RPi.GPIO as GPIO
import time

SERVO_PIN = 4

GPIO.setmode(GPIO.IN)
GPIO.setup(SERVO_PIN, GPIO.OUT)

# 주파수 : 50Hz
pwm = GPIO.PWN(SERVO_PIN, 50)
pwm.start(7.5) # 0도 # 시작

try:
    while True:
        val = input("1: 0도, 2: -90도, 3: +90도, 9: Exit>")
        if val == '1':
            pwm.ChangeDutyCycle(7.5) # 0도
        elif val == '2':
            #pwm.ChangeDutyCycle(5) # -45도
            pwm.ChangeDutyCycle(2.5) # -90도
        elif val == '3':
            #pwm.ChangeDutyCycle(10) # +45도
            pwm.ChangeDutyCycle(12.5) # +90도
        elif val == '9':
            break
finally:
    pwm.stop() # 종료
    GPIO.cleanup()
