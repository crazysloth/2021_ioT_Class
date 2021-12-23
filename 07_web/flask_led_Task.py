
from flask import Flask
import RPi.GPIO as GPIO

red_pin = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(red_pin, GPIO.OUT)

green_pin = 16
GPIO.setmode(GPIO.BCM)
GPIO.setup(green_pin, GPIO.OUT)

#Flask 객체 생성
#__name__은 파일명
app = Flask(__name__)

#라우팅을 위한 뷰 함수
@app.route("/")
def home():
    return """
        <p>Hello, Flask!</p>
        <a href="/led/red/on">RED LED ON</a>
        <a href="/led/red/off">RED LED OFF<br></a>
        <a href="/led/blue/on">BLUE LED ON</a>
        <a href="/led/blue/off">BLUE LED OFF</a>
    """

@app.route("/led/<op1>/<op2>")
def led_op(op1, op2):
    if op1 == "red" and op2 == "on":  
        GPIO.output(red_pin, 1)
        return """
            <p>RED LED ON</p>
            <a href="/">Go Home</a>
        """
    elif op1 == "red" and op2 == "off":
        GPIO.output(red_pin, 0)
        return """
            <p>RED LED OFF</p>
            <a href="/">Go Home</a>
        """

    elif op1 == "blue" and op2 == "on":
        GPIO.output(green_pin, 1)
        return """
            <p>BLUE LED ON</p>
            <a href="/">Go Home</a>
        """
    elif op1 == "blue" and op2 == "off":
        GPIO.output(green_pin, 0)
        return """
            <p>BLUE LED ON</p>
            <a href="/">Go Home</a>
        """
        


# 터미널에서 직접 실행시킨 경우
if __name__ =="__main__":
    try:
        app.run(host="0.0.0.0")
    finally:
        GPIO.cleanup()