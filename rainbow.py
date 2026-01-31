from sense_hat import SenseHat
import time

sense = SenseHat()

# Define 8 rainbow colors
rainbow_colors = [
    [255, 0, 0],      # Red
    [255, 127, 0],    # Orange
    [255, 255, 0],    # Yellow
    [0, 255, 0],      # Green
    [0, 0, 255],      # Blue
    [75, 0, 130],     # Indigo
    [148, 0, 211],    # Violet
    [255, 255, 255]   # White (optional, can remove)
]

# Repeat forever until Ctrl+C
try:
    while True:
        # Build 8x8 matrix
        pixels = []
        for row in range(8):
            for col in range(8):
                # Shift colors to create moving rainbow
                color_index = (col + row) % len(rainbow_colors)
                pixels.append(rainbow_colors[color_index])

        sense.set_pixels(pixels)
        time.sleep(0.2)  # adjust speed (seconds)
        
        # Rotate the rainbow for next frame
        rainbow_colors = rainbow_colors[1:] + [rainbow_colors[0]]

except KeyboardInterrupt:
    sense.clear()
    print("Rainbow cycle stopped!")
