#'도'음 출력하기
import RPi.GPIO as GPIO
import time

BUZZER_PIN = 4
GPIO.setmod(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

# 주파수 (262Hz)
pwm = GPIO.PWM(BUZZER_PIN, 262)
pwm.start(50) # duty cycle(0 ~ 100)

time.sleep(2)
pwm.ChangeDutyCycle(0) # 부저음 끄기

pwm.stop()
GPIO.cleanup()

