import curses
import sys

WHITE:int = curses.COLOR_WHITE
BLACK:int = curses.COLOR_BLACK
RED:int = curses.COLOR_RED
GREEN:int = curses.COLOR_GREEN
BLUE:int = curses.COLOR_BLUE
YELLOW:int = curses.COLOR_YELLOW
CYAN:int = curses.COLOR_CYAN
MAGENTA:int = curses.COLOR_MAGENTA

def color(f:int, b:int) -> int:
  return (f*10)+b+1

def init_color() -> None:

  curses.start_color()
  if not curses.has_colors:
    print("ERROR:<Terminal does not suport color>")
    input()

  for fcolor in range(8):
    for bcolor in range(8):
      print(fcolor, bcolor)
      curses.init_pair((fcolor*10)+bcolor+1, fcolor, bcolor)