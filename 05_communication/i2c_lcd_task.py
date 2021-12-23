from lcd import drivers
import time
import datetime
import Adafruit_DHT
sensor = Adafruit_DHT.DHT11
PIN = 26
display = drivers.Lcd()
try:
    while True:
        now = datetime.datetime.now()
        display.lcd_display_string(now.strftime("%x%X"), 1)
        h, t = Adafruit_DHT.read_retry(sensor, PIN)
        display.lcd_display_string("%.1f*C, %.1f%%" % (t, h), 2)

finally:
    print("Cleaning up!")
    display.lcd_clear()