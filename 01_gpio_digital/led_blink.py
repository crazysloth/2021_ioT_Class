import RPi.GPIO as GPIO #GPIO 모듈 import
import time
LED_PIN = 23 # PIN 번호 설정
GPIO.setmode(GPIO.BCM) #핀 번호 방식 설정(GPIO.BOART or GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT) #PIN 모드 설정(GPIO.OUT or GPIO.IN)

for i in range(10):
    GPIO.output(LED_PIN, GPIO.HIGH) #True, 1
    print("Led on")
    time.sleep(1)
    GPIO.output(LED_PIN, GPIO.LOW) #false, 0
    print("Led off")
    time.sleep(1)

GPIO.cleanup() # GPiO 핀 상태 초기화