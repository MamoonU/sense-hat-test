from sense_hat import SenseHat
import time
import random

sense = SenseHat()
sense.clear()

# Colors
RED = [255, 0, 0]
YELLOW = [255, 255, 0]
BLUE = [0, 0, 180]
PINK = [255, 0, 255]
GREEN = [0, 255, 0]
WHITE = [255, 255, 255]
BLACK = [0, 0, 0]

FRUITS = [RED, YELLOW, BLUE, PINK, GREEN]

# Column x ranges (2 pixels wide per column)
COL_X = [0, 3, 6]
# Row y ranges (2 pixels tall per row)
ROW_Y = [0, 3, 6]
# Horizontal divider rows
LINE_Y = [2, 5]
# Vertical divider columns
LINE_X = [2, 5]

# Draw static white grid lines
def draw_lines():
    for y in LINE_Y:
        for x in range(8):
            sense.set_pixel(x, y, WHITE)
    for x in LINE_X:
        for y in range(8):
            sense.set_pixel(x, y, WHITE)

# Draw the slot machine
def draw_slots(slots):
    sense.clear()
    draw_lines()
    for col in range(3):
        for row in range(3):
            color = slots[col][row]
            base_x = COL_X[col]
            base_y = ROW_Y[row]
            # Draw 2x2 fruit block
            for dx in range(2):
                for dy in range(2):
                    sense.set_pixel(base_x + dx, base_y + dy, color)

# Spin animation (columns scroll downward, slower & longer)
def spin(slots):
    # Different spin lengths for each column (more realistic & longer)
    spin_counts = [45, 60, 75]

    max_spins = max(spin_counts)

    for step in range(max_spins):
        for col in range(3):
            if step < spin_counts[col]:
                # Scroll column downward
                slots[col] = [slots[col][2], slots[col][0], slots[col][1]]
                # New random fruit enters at the top
                slots[col][0] = random.choice(FRUITS)
        draw_slots(slots)
        time.sleep(0.18)  # Slower spin, more visible movement

# Flash result
def flash(color):
    for _ in range(3):
        sense.clear(color)
        time.sleep(0.2)
        draw_slots(slots)
        time.sleep(0.2)

# Initial slots
slots = [[random.choice(FRUITS) for _ in range(3)] for _ in range(3)]
draw_slots(slots)

# Joystick handler
def handle_joystick(event):
    global slots
    if event.action != 'pressed':
        return

    spin(slots)

    # Check middle row
    middle = [slots[col][1] for col in range(3)]
    if middle[0] == middle[1] == middle[2]:
        flash(GREEN)
    else:
        flash(RED)

    # Hold final result on screen longer
    time.sleep(1.5)

sense.stick.direction_any = handle_joystick

try:
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    sense.clear()
    print("Slot machine stopped")
