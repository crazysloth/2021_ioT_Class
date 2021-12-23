from lcd import drivers
import time
import datetime
import Adafruit_DHT
sensor = Adafruit_DHT.DHT11
PIN = 12
now = datetime.datetime.now()
display = drivers.Lcd()

try:
    display.lcd_display_string(now.strftime("%x %X")), 1)
    while True:
        display.lcd_display_string("** WELCOME **", 2)
        time.sleep(2)
        display.lcd_display_string("   WELCOME   ", 2)
        time.sleep(2) 
finally:
    print("Cleaning up!")
    display.lcd_clear()