from sense_hat import SenseHat
import time

sense = SenseHat()

# Ultra-smooth rainbow (96 steps)
rainbow_colors = []
for r in range(0, 256, 16):
    rainbow_colors.append([255, r, 0])
for g in range(0, 256, 16):
    rainbow_colors.append([255 - g, 255, 0])
for b in range(0, 256, 16):
    rainbow_colors.append([0, 255, b])
for g in range(255, -1, -16):
    rainbow_colors.append([0, g, 255])
for r in range(0, 256, 16):
    rainbow_colors.append([r, 0, 255])
for b in range(255, -1, -16):
    rainbow_colors.append([255, 0, b])

try:
    while True:
        pixels = []
        for row in range(8):
            for col in range(8):
                color_index = (row + col) % len(rainbow_colors)
                pixels.append(rainbow_colors[color_index])
        sense.set_pixels(pixels)

        # Shift colors for animation
        rainbow_colors = rainbow_colors[1:] + [rainbow_colors[0]]

        # Faster animation
        time.sleep(0.02)

except KeyboardInterrupt:
    sense.clear()
    print("Rainbow cycle stopped!")
