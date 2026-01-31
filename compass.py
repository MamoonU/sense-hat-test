from sense_hat import SenseHat
import time
import math

sense = SenseHat()
sense.clear()

# Colors
ARROW_COLOR = [255, 0, 0]   # Red arrow
BG = [0, 0, 0]

CENTER_X = 3.5
CENTER_Y = 3.5
RADIUS = 3.2

# Clear display
def clear():
    sense.set_pixels([BG] * 64)

# Draw a smooth arrow pointing at heading angle
def draw_arrow(angle_deg):
    clear()

    # Convert degrees to radians (Sense HAT compass: 0° = North)
    angle_rad = math.radians(angle_deg)

    # Calculate arrow tip
    tip_x = CENTER_X + RADIUS * math.sin(angle_rad)
    tip_y = CENTER_Y - RADIUS * math.cos(angle_rad)

    # Draw arrow shaft (interpolated points)
    steps = 6
    for i in range(steps + 1):
        t = i / steps
        x = CENTER_X + t * (tip_x - CENTER_X)
        y = CENTER_Y + t * (tip_y - CENTER_Y)
        px = int(round(x))
        py = int(round(y))
        if 0 <= px < 8 and 0 <= py < 8:
            sense.set_pixel(px, py, ARROW_COLOR)

try:
    while True:
        # Get compass heading
        heading = sense.get_compass()

        # Draw rotating arrow
        draw_arrow(heading)

        time.sleep(0.05)

except KeyboardInterrupt:
    sense.clear()
    print("Smooth compass stopped")