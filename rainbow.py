from sense_hat import SenseHat
import time

sense = SenseHat()

# More colors for a smoother rainbow
rainbow_colors = [
    [255, 0, 0],    # Red
    [255, 64, 0],
    [255, 128, 0],
    [255, 191, 0],
    [255, 255, 0],  # Yellow
    [191, 255, 0],
    [128, 255, 0],
    [64, 255, 0],
    [0, 255, 0],    # Green
    [0, 255, 64],
    [0, 255, 128],
    [0, 255, 191],
    [0, 255, 255],  # Cyan
    [0, 191, 255],
    [0, 128, 255],
    [0, 64, 255],
    [0, 0, 255],    # Blue
    [64, 0, 255],
    [128, 0, 255],
    [191, 0, 255],
    [255, 0, 255],  # Magenta
    [255, 0, 191],
    [255, 0, 128],
    [255, 0, 64]
]

try:
    while True:
        pixels = []
        for row in range(8):
            for col in range(8):
                # Use a diagonal shift for a flowing rainbow
                color_index = (row + col) % len(rainbow_colors)
                pixels.append(rainbow_colors[color_index])
        sense.set_pixels(pixels)

        # Shift the colors to create movement
        rainbow_colors = rainbow_colors[1:] + [rainbow_colors[0]]

        # Faster tick (smaller sleep = faster animation)
        time.sleep(0.1)

except KeyboardInterrupt:
    sense.clear()
    print("Rainbow cycle stopped!")
