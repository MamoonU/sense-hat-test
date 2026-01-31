from sense_hat import SenseHat
import time

sense = SenseHat()

# Expanded colors for a smoother rainbow (48 steps)
rainbow_colors = [
    [255, 0, 0], [255, 32, 0], [255, 64, 0], [255, 96, 0], [255, 128, 0], [255, 160, 0], [255, 192, 0], [255, 224, 0],
    [255, 255, 0], [224, 255, 0], [192, 255, 0], [160, 255, 0], [128, 255, 0], [96, 255, 0], [64, 255, 0], [32, 255, 0],
    [0, 255, 0], [0, 255, 32], [0, 255, 64], [0, 255, 96], [0, 255, 128], [0, 255, 160], [0, 255, 192], [0, 255, 224],
    [0, 255, 255], [0, 224, 255], [0, 192, 255], [0, 160, 255], [0, 128, 255], [0, 96, 255], [0, 64, 255], [0, 32, 255],
    [0, 0, 255], [32, 0, 255], [64, 0, 255], [96, 0, 255], [128, 0, 255], [160, 0, 255], [192, 0, 255], [224, 0, 255],
    [255, 0, 255], [255, 0, 224], [255, 0, 192], [255, 0, 160], [255, 0, 128], [255, 0, 96], [255, 0, 64], [255, 0, 32]
]

try:
    while True:
        pixels = []
        for row in range(8):
            for col in range(8):
                # Diagonal shift for flowing rainbow
                color_index = (row + col) % len(rainbow_colors)
                pixels.append(rainbow_colors[color_index])
        sense.set_pixels(pixels)

        # Shift colors to create movement
        rainbow_colors = rainbow_colors[1:] + [rainbow_colors[0]]

        # Slightly faster animation
        time.sleep(0.05)

except KeyboardInterrupt:
    sense.clear()
    print("Rainbow cycle stopped!")
