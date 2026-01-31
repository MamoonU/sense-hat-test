from sense_hat import SenseHat
import time

sense = SenseHat()
sense.clear()

# Colors
BALL_COLOR = [255, 255, 0]  # Yellow ball
EMPTY_COLOR = [0, 0, 0]     # Empty

# Initial position
x, y = 3, 3  # Start near center

# Game loop
try:
    while True:
        # Read tilt from accelerometer
        orientation = sense.get_accelerometer_raw()
        ax = orientation['x']
        ay = orientation['y']

        # Move ball based on tilt
        if ax < -0.2 and x < 7:
            x += 1
        elif ax > 0.2 and x > 0:
            x -= 1

        if ay < -0.2 and y < 7:
            y += 1
        elif ay > 0.2 and y > 0:
            y -= 1

        # Draw ball
        pixels = [EMPTY_COLOR for _ in range(64)]
        pixels[y * 8 + x] = BALL_COLOR
        sense.set_pixels(pixels)

        time.sleep(0.05)

except KeyboardInterrupt:
    sense.clear()
    print("Teeter game stopped!")
