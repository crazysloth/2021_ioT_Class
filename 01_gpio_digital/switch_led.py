# 스위치로 LED 제어하기
import RPi.GPIO as GPIO

LED_PIN_1 = 10 #red
LED_PIN_2 = 9 #yellow
LED_PIN_3 = 8 #green
SWITCH_PIN_1 = 13 #red
SWITCH_PIN_2 = 12 #yellow
SWITCH_PIN_3 = 11 #green

GPIO.setmode(GPIO.BCM)
# LED_PIN 셋업
GPIO.setup(LED_PIN_1, GPIO.OUT)
GPIO.setup(LED_PIN_2, GPIO.OUT)
GPIO.setup(LED_PIN_3, GPIO.OUT)

GPIO.setup(SWITCH_PIN_1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SWITCH_PIN_2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SWITCH_PIN_3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)#GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    while True:
        red = GPIO.input(SWITCH_PIN_1) #누르지 않았을 때 0, 눌렀을 때 1
        GPIO.output(LED_PIN_1, red)

        yellow = GPIO.input(SWITCH_PIN_2)
        GPIO.output(LED_PIN_2, yellow) #LOW = 0 , HIGH = 1

        green = GPIO.input(SWITCH_PIN_3)
        GPIO.output(LED_PIN_3, green)
finally:
    GPIO.cleanup()
    print("clenaup and exit")