import curses
import random

def create_food(snake):
    """Generate food coordinates that do not overlap with the snake."""
    while True:
        food = [random.randint(1, 18), random.randint(1, 58)]
        if food not in snake:
            return food

def main(stdscr):
    curses.curs_set(0)
    sh, sw = stdscr.getmaxyx()

    if sh < 20 or sw < 60:
        stdscr.addstr(0, 0, "Terminal must be at least 20x60. Press any key.")
        stdscr.getch()
        return

    win_y = (sh // 2) - 10
    win_x = (sw // 2) - 30

    win = curses.newwin(20, 60, win_y, win_x)
    win.keypad(1)

    timeout = 150
    win.timeout(timeout)

    win.border(0)

    snake = [
        [10, 15],
        [10, 14],
        [10, 13]
    ]

    for y, x in snake:
        win.addch(y, x, '#')

    food = create_food(snake)
    win.addch(food[0], food[1], '@')

    key = curses.KEY_RIGHT
    score = 0

    opposites = {
        curses.KEY_UP: curses.KEY_DOWN,
        curses.KEY_DOWN: curses.KEY_UP,
        curses.KEY_LEFT: curses.KEY_RIGHT,
        curses.KEY_RIGHT: curses.KEY_LEFT
    }

    paused = False  # 🔥 Pause state

    while True:
        win.addstr(0, 2, f' Score: {score} ')

        if paused:
            win.addstr(9, 22, " PAUSED ")
            win.addstr(10, 18, " Press 'P' to Resume ")
            win.refresh()

            while True:
                k = win.getch()
                if k == ord('p') or k == ord('P'):
                    paused = False
                    win.clear()
                    win.border(0)

                    # redraw snake
                    for y, x in snake:
                        win.addch(y, x, '#')

                    # redraw food
                    win.addch(food[0], food[1], '@')
                    break
            continue

        next_key = win.getch()

        # 🔥 Pause trigger
        if next_key == ord('p') or next_key == ord('P'):
            paused = True
            continue

        if next_key in [curses.KEY_UP, curses.KEY_DOWN, curses.KEY_LEFT, curses.KEY_RIGHT]:
            if opposites.get(next_key) != key:
                key = next_key

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

        # Collision
        if (new_head[0] in [0, 19] or
            new_head[1] in [0, 59] or
            new_head in snake):
            break

        snake.insert(0, new_head)

        if new_head == food:
            score += 1
            timeout = max(30, timeout - 2)
            win.timeout(timeout)

            food = create_food(snake)
            win.addch(food[0], food[1], '@')
        else:
            tail = snake.pop()
            win.addch(tail[0], tail[1], ' ')

        win.addch(new_head[0], new_head[1], '#')

    # Game Over
    win.addstr(8, 24, " GAME OVER ")
    win.addstr(10, 22, f" Final Score: {score} ")
    win.addstr(12, 17, " Press any key to exit ")
    win.timeout(-1)
    win.getch()

if __name__ == "__main__":
    curses.wrapper(main)
