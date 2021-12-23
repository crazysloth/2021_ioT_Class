# Imports the necessary libraries...
#가변저항 돌리는 곳이 내쪽으로기준 왼쪽에 3.3v가 있다면 왼쪽으로 돌릴수록 voltage 커짐, 가변저항이 오른쪽에 있을 경우 오른쪽ㅇ로 돌릴 수록 voltage 커짐
import board
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

# Setting some variables for our reset pin etc.
RESET_PIN = digitalio.DigitalInOut(board.D4)

# Very important... This lets py-gaugette 'know' what pins to use in order to reset the display
i2c = board.I2C()
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3c, reset=RESET_PIN)

# Clear display.
oled.fill(0)
oled.show()

# Create blank image for drawing.
image = Image.new("1", (oled.width, oled.height))
draw = ImageDraw.Draw(image)

# Load a font in 2 different sizes.
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 28)
font2 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)

# Draw the text
draw.text((0, 0), "1606", font=font, fill=255)
draw.text((0, 30), "Kim Seong Hun!", font=font2, fill=255)
draw.text((0, 46), "ing", font=font2, fill=255)

# Display image
oled.image(image)
oled.show()