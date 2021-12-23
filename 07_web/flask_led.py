from typing import final
from flask import Flask
import RPi.GPIO as GPIO

led_pin = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

#Flask 객체 생성
#__name__은 파일명
app = Flask(__name__)

#라우팅을 위한 뷰 함수
@app.route("/")
def hello_world():
    return """
        <p>Hello, Flask!</p>
        <a href="/led/on">LED ON</a>
        <a href="/led/off">LED OFF</a>
    """

@app.route("/led/<op>")
def led_op(op):
    print(op)
    if op == "on":
        GPIO.output(led_pin, 1)
        return """
        <p>LED ON</p>
        <a href="/">Go Home</a>
        """
    elif op == "off":
        GPIO.output(led_pin, 0)
        return """
        <p>LED OFF</p>
        <a href="/">Go Home</a>
        """


# 터미널에서 직접 실행시킨 경우
if __name__ =="__main__":
    try:
        app.run(host="0.0.0.0")
    finally:
        GPIO.cleanup()