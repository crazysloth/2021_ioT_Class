#'도'음 출력하기
import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
BUZZER_PIN = 4
GPIO.setup(BUZZER_PIN, GPIO.OUT)

# 주파수 (262Hz)
pwm = GPIO.PWM(BUZZER_PIN, 262)
pwm.start(10) # duty cycle(0 ~ 100)

school = [392, 392, 440, 440, 392, 392, 330 ,392, 392, 330, 330 ,294, 392, 392, 440, 440, 392, 392, 330,392 ,330, 294, 330,262]
try:
    for i in school:
        pwm.ChangeFrequency(i)
        if i == 6 or 18:
            time.sleep(0.6)
        elif i == 11 or 23:
            time.sleep(2)
        else:
            time.sleep(0.3)
finally:
    pwm.stop()
    GPIO.cleanup()

#time.sleep(2)
#pwm.ChangeDutyCycle(0) # 부저음 끄기



