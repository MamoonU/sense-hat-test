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

# Slot grid x positions for columns
COL_X = [1, 3, 5]
ROW_Y = [0, 2, 4]
LINE_Y = [1, 3]

# Draw static white lines
def draw_lines():
    for y in LINE_Y:
        for x in range(8):
            sense.set_pixel(x, y, WHITE)

# Draw the slot machine
def draw_slots(slots):
    sense.clear()
    draw_lines()
    for col in range(3):
        for row in range(3):
            x = COL_X[col]
            y = ROW_Y[row]
            sense.set_pixel(x, y, slots[col][row])

# Spin animation
def spin(slots, spins=20):
    for _ in range(spins):
        for col in range(3):
            slots[col] = [random.choice(FRUITS) for _ in range(3)]
        draw_slots(slots)
        time.sleep(0.08)

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

    # Spin
    spin(slots)

    # Check middle row
    middle = [slots[col][1] for col in range(3)]
    if middle[0] == middle[1] == middle[2]:
        flash(GREEN)
    else:
        flash(RED)

sense.stick.direction_any = handle_joystick

# Keep program alive
try:
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    sense.clear()
    print("Slot machine stopped")