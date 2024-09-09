import curses
#import color

def draw_string(
    window:curses.window,
    text:str,
    cords:tuple[int,int],
    color:int
    ) -> None:
  window.addstr(cords[1], cords[0], text, curses.color_pair(color))

def draw_char(
    window:curses.window,
    char:str,
    cords:tuple[int,int],
    color:int
    ) -> None:
  window.addch(cords[1], cords[0], char, curses.color_pair(color))

def draw_rect(
    window:curses.window,
    char:str,
    start:tuple[int,int],
    size:tuple[int,int],
    color:int
    ) -> None:
  for x in range(start[0], start[0]+size[0]):
    draw_char(window, char, (x,start[1]), color)
    draw_char(window, char, (x,start[1]+size[1]-1), color)
  
  for y in range(start[1], start[1]+size[1]):
    draw_char(window, char, (start[0], y), color)
    draw_char(window, char, (start[0]+size[0]-1, y), color)

def draw_line(
    window:curses.window,
    char:str,
    start:tuple[int,int],
    end:tuple[int,int],
    color:int
    ) -> None:
  dx = end[0] - start[0]
  dy = end[1] - start[1]
  step = max(abs(dx), abs(dy))
  if step == 0:
    raise ValueError
  stepX = dx/step
  stepY = dy/step
  for i in range(step+1):
    draw_char(window, char, (round(start[0] + i*stepX), round(start[1] + i*stepY)), color)