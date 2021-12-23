import RPi.GPIO as GPIO #GPIO 모듈 import
import time
LED_PIN_1 = 4
LED_PIN_2 = 5 # PIN 번호 설정
LED_PIN_3 = 6
GPIO.setmode(GPIO.BCM) #핀 번호 방식 설정(GPIO.BOART or GPIO.BCM)  
GPIO.setup(LED_PIN_1, GPIO.OUT) #PIN 모드 설정(GPIO.OUT or GPIO.IN)
GPIO.setup(LED_PIN_2, GPIO.OUT) #PIN 모드 설정(GPIO.OUT or GPIO.IN)
GPIO.setup(LED_PIN_3, GPIO.OUT) #PIN 모드 설정(GPIO.OUT or GPIO.IN)

for i in range(4,7):
    GPIO.output(i, GPIO.HIGH)
    time.sleep()
    GPIO.output(i, GPIO.LOW)


GPIO.cleanup() # GPiO 핀 상태 초기화