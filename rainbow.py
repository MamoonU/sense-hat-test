from sense_hat import SenseHat
import time

sense = SenseHat()

colors = [[255,0,0],[0,255,0],[0,0,255],[255,255,0],
          [255,0,255],[0,255,255],[255,255,255],[128,128,128]]

pixels = []
for row in range(8):
    for col in range(8):
        pixels.append(colors[(row*8 + col) % len(colors)])

try:
    sense.set_pixels(pixels)
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    sense.clear()
