from sense_hat import SenseHat
import time

sense = SenseHat()
sense.clear()

# Colors
BALL_COLOR = [255, 255, 0]  # Yellow ball
EMPTY_COLOR = [0, 0, 0]     # Empty

# Position stored as floats for smooth movement
x, y = 3.5, 3.5

# Tuning constants
SENSITIVITY = 0.4   # How strongly tilt affects movement
FRICTION = 0.90     # Slows the ball gradually

vx, vy = 0.0, 0.0   # Velocity

try:
    while True:
        # Read tilt from accelerometer
        accel = sense.get_accelerometer_raw()
        ax = accel['x']
        ay = accel['y']

        # Corrected directions (natural tilt)
        vx += ax * SENSITIVITY
        vy += ay * SENSITIVITY

        # Apply friction
        vx *= FRICTION
        vy *= FRICTION

        # Update position
        x += vx
        y += vy

        # Clamp to screen bounds
        x = max(0, min(7, x))
        y = max(0, min(7, y))

        # Convert to LED coordinates
        px = int(round(x))
        py = int(round(y))

        # Draw
        pixels = [EMPTY_COLOR for _ in range(64)]
        pixels[py * 8 + px] = BALL_COLOR
        sense.set_pixels(pixels)

        time.sleep(0.03)

except KeyboardInterrupt:
    sense.clear()
    print("Teeter game stopped!")