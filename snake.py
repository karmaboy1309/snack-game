import curses
import random

def create_food(snake):
    """Generate food coordinates that do not overlap with the snake."""
    while True:
        food = [random.randint(1, 18), random.randint(1, 58)]
        if food not in snake:
            return food

def main(stdscr):
    # Initialize basic curses settings
    curses.curs_set(0)  # Hide the cursor
    
    # Get terminal dimensions
    sh, sw = stdscr.getmaxyx()

    # Ensure the terminal is large enough for the 20x60 game window
    if sh < 20 or sw < 60:
        stdscr.addstr(0, 0, "Terminal must be at least 20x60 to play. Press any key to exit.")
        stdscr.refresh()
        stdscr.getch()
        return

    # Calculate top-left coordinates to center the 20x60 window
    win_y = (sh // 2) - 10
    win_x = (sw // 2) - 30

    # Create the game window
    win = curses.newwin(20, 60, win_y, win_x)
    win.keypad(1)       # Enable keypad input (KEY_RIGHT, etc.)
    
    # Initial game speed (timeout in ms)
    timeout = 150
    win.timeout(timeout)

    # Draw the window border
    win.border(0)

    # Initialize the snake
    # Starting position at the center of the window
    snake_y = 10
    snake_x = 15
    snake = [
        [snake_y, snake_x],
        [snake_y, snake_x - 1],
        [snake_y, snake_x - 2]
    ]

    # Render initial snake
    for y, x in snake:
        win.addch(y, x, '#')

    # Initialize food
    food = create_food(snake)
    win.addch(food[0], food[1], '@')

    # Initial variables
    key = curses.KEY_RIGHT
    score = 0

    # Map opposite directions to prevent the snake from instantly reversing
    opposites = {
        curses.KEY_UP: curses.KEY_DOWN,
        curses.KEY_DOWN: curses.KEY_UP,
        curses.KEY_LEFT: curses.KEY_RIGHT,
        curses.KEY_RIGHT: curses.KEY_LEFT
    }

    while True:
        # Display the score at the top border
        win.addstr(0, 2, f' Score: {score} ')

        # Wait for next key input (blocks up to 'timeout' milliseconds)
        next_key = win.getch()

        # Update the direction if a valid arrow key was pressed
        if next_key in [curses.KEY_UP, curses.KEY_DOWN, curses.KEY_LEFT, curses.KEY_RIGHT]:
            # Prevent the snake from reversing into its own body
            if opposites.get(next_key) != key:
                key = next_key

        # Determine new head position based on current direction
        head_y, head_x = snake[0]

        if key == curses.KEY_UP:
            head_y -= 1
        elif key == curses.KEY_DOWN:
            head_y += 1
        elif key == curses.KEY_LEFT:
            head_x -= 1
        elif key == curses.KEY_RIGHT:
            head_x += 1

        new_head = [head_y, head_x]

        # Check for collisions
        # 1. Collision with window boundaries (0 or 19 for Y, 0 or 59 for X)
        # 2. Collision with self
        if (new_head[0] in [0, 19] or
            new_head[1] in [0, 59] or
            new_head in snake):
            break  # End the game loop

        # Move the snake by inserting the new head
        snake.insert(0, new_head)

        # Check if the snake has eaten the food
        if new_head == food:
            score += 1
            # Increase game speed (decrease timeout duration)
            timeout = max(30, timeout - 2)
            win.timeout(timeout)

            # Generate new food and display it
            food = create_food(snake)
            win.addch(food[0], food[1], '@')
        else:
            # If no food eaten, remove the tail segment to simulate movement
            tail = snake.pop()
            win.addch(tail[0], tail[1], ' ')

        # Draw the new snake head
        win.addch(new_head[0], new_head[1], '#')

    # Game Over Sequence
    win.addstr(8, 24, " GAME OVER ")
    win.addstr(10, 22, f" Final Score: {score} ")
    win.addstr(12, 17, " Press any key to exit... ")
    win.refresh()

    # Clear input buffer and wait for the user to press a key before exiting
    win.timeout(-1)
    curses.flushinp()
    win.getch()

if __name__ == "__main__":
    # curses.wrapper handles initialization and cleanup safely
    curses.wrapper(main)
