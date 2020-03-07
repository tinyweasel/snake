import curses, time


def main(screen):
    curses.curs_set(0) # hide cursor
    screen.nodelay(True) # don't block I/O

    snake = [(0, i) for i in reversed(range(20))]
    
    directions = {
        curses.KEY_UP: (-1, 0),
        curses.KEY_DOWN: (1, 0),
        curses.KEY_LEFT: (0, -1),
        curses.KEY_RIGHT: (0, 1),
    }

    direction = directions[curses.KEY_RIGHT]

    while True:
        screen.erase()
            
        # draw snake
        screen.addstr(*snake[0], '@')
        for segment in snake[1:]:
            screen.addstr(*segment, '*')
        
        # move snake
        snake.pop()
        snake.insert(0, tuple(map(sum, zip(snake[0], direction))))

        # change direction
        direction = directions.get(screen.getch(), direction)

        screen.refresh()
        time.sleep(0.1)

if __name__ == '__main__':
    curses.wrapper(main)
