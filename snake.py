from sense_hat import SenseHat
import time
import random

# Initialize
sense = SenseHat()
sense.clear()

# Colors
SNAKE_COLOR = [0, 255, 0]      # Green body
SNAKE_HEAD_COLOR = [0, 200, 0] # Darker green head
FOOD_COLOR = [255, 0, 0]       # Red

# Snake initial state
snake = [(4, 4), (3, 4), (2, 4)]
direction = "RIGHT"

# Food
def place_food():
    while True:
        f = (random.randint(0, 7), random.randint(0, 7))
        if f not in snake:
            return f

food = place_food()

# Move snake
def move_snake():
    global snake, food
    head_x, head_y = snake[0]
    if direction == 'UP':
        head_y -= 1
    elif direction == 'DOWN':
        head_y += 1
    elif direction == 'LEFT':
        head_x -= 1
    elif direction == 'RIGHT':
        head_x += 1

    new_head = (head_x, head_y)

    # Collision check
    if new_head in snake or not (0 <= head_x <= 7 and 0 <= head_y <= 7):
        return False

    snake.insert(0, new_head)

    if new_head == food:
        food = place_food()
    else:
        snake.pop()

    return True

# Draw function
def draw():
    sense.clear()
    for segment in snake[1:]:
        sense.set_pixel(segment[0], segment[1], SNAKE_COLOR)
    sense.set_pixel(snake[0][0], snake[0][1], SNAKE_HEAD_COLOR)
    sense.set_pixel(food[0], food[1], FOOD_COLOR)

# Main game loop
game_over = False
speed = 0.3  # movement delay

while not game_over:
    # Poll joystick events and update direction
    for event in sense.stick.get_events():
        if event.action == 'pressed':
            global direction  # <- crucial for updating global variable
            if event.direction == 'up' and direction != 'DOWN':
                direction = 'UP'
            elif event.direction == 'down' and direction != 'UP':
                direction = 'DOWN'
            elif event.direction == 'left' and direction != 'RIGHT':
                direction = 'LEFT'
            elif event.direction == 'right' and direction != 'LEFT':
                direction = 'RIGHT'

    game_over = not move_snake()
    draw()
    time.sleep(speed)

# Game over message
sense.show_message("GAME OVER", text_colour=[255, 0, 0], scroll_speed=0.05)
sense.clear()
