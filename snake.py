
import curses
import random
import os

HIGHSCORE_FILE = "highscore.txt"

def get_highscore():
    if not os.path.exists(HIGHSCORE_FILE):
        return 0
    with open(HIGHSCORE_FILE, "r") as f:
        return int(f.read() or 0)

def save_highscore(score):
    with open(HIGHSCORE_FILE, "w") as f:
        f.write(str(score))

def create_food(snake):
    while True:
        food = [random.randint(1, 18), random.randint(1, 58)]
        if food not in snake:
            return food

def run_game(stdscr):
    curses.curs_set(0)
    sh, sw = stdscr.getmaxyx()

    if sh < 20 or sw < 60:
        stdscr.addstr(0, 0, "Terminal must be at least 20x60.")
        stdscr.getch()
        return False

    highscore = get_highscore()

    win_y = (sh // 2) - 10
    win_x = (sw // 2) - 30

    win = curses.newwin(20, 60, win_y, win_x)
    win.keypad(1)

    timeout = 150
    win.timeout(timeout)
    win.border(0)

    snake = [[10, 15], [10, 14], [10, 13]]

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

    paused = False

    while True:
        # 🔥 Show Score + High Score
        win.addstr(0, 2, f' Score: {score} ')
        win.addstr(0, 20, f' High: {highscore} ')

        if paused:
            win.addstr(9, 22, " PAUSED ")
            win.addstr(10, 18, " Press 'P' to Resume ")
            win.refresh()

            while True:
                k = win.getch()
                if k in [ord('p'), ord('P')]:
                    paused = False
                    win.clear()
                    win.border(0)

                    for y, x in snake:
                        win.addch(y, x, '#')

                    win.addch(food[0], food[1], '@')
                    break
            continue

        next_key = win.getch()

        if next_key in [ord('p'), ord('P')]:
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

        if (new_head[0] in [0, 19] or
            new_head[1] in [0, 59] or
            new_head in snake):
            break

        snake.insert(0, new_head)

        if new_head == food:
            score += 1

            # 🔥 Update high score live
            if score > highscore:
                highscore = score

            timeout = max(30, timeout - 2)
            win.timeout(timeout)

            food = create_food(snake)
            win.addch(food[0], food[1], '@')
        else:
            tail = snake.pop()
            win.addch(tail[0], tail[1], ' ')

        win.addch(new_head[0], new_head[1], '#')

    # 🔥 Save High Score
    save_highscore(highscore)

    # Game Over Screen
    win.clear()
    win.border(0)
    win.addstr(8, 22, " GAME OVER ")
    win.addstr(10, 20, f" Final Score: {score} ")
    win.addstr(11, 20, f" High Score: {highscore} ")
    win.addstr(13, 15, " Press 'R' to Restart ")
    win.addstr(14, 15, " Press any other key to Exit ")
    win.refresh()

    win.timeout(-1)
    key = win.getch()

    if key in [ord('r'), ord('R')]:
        return True
    return False


def main(stdscr):
    while True:
        restart = run_game(stdscr)
        if not restart:
            break

if __name__ == "__main__":
    curses.wrapper(main)
