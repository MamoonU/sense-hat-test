from sense_hat import SenseHat
import time
import math

sense = SenseHat()
sense.clear()

# Colors
NORTH_COLOR = [255, 0, 0]   # Red arrow
BG = [0, 0, 0]

# 8 directions (N, NE, E, SE, S, SW, W, NW)
directions = [
    (0, -1),   # N
    (1, -1),   # NE
    (1, 0),    # E
    (1, 1),    # SE
    (0, 1),    # S
    (-1, 1),   # SW
    (-1, 0),   # W
    (-1, -1)   # NW
]

center = (3, 3)

def draw_arrow(dx, dy):
    sense.clear()
    x, y = center
    sense.set_pixel(x, y, NORTH_COLOR)
    sense.set_pixel(x + dx, y + dy, NORTH_COLOR)

try:
    while True:
        heading = sense.get_compass()  # 0–360 degrees

        # Convert heading to one of 8 directions
        index = int((heading + 22.5) // 45) % 8
        dx, dy = directions[index]

        draw_arrow(dx, dy)
        time.sleep(0.1)

except KeyboardInterrupt:
    sense.clear()
    print("Compass stopped")
