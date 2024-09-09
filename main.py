import curses
import sys
import os
#import json

from color import *
import draw

import screen

WIDTH:int = 120
HEIGHT:int = 30

def show_exception_and_exit(exc_type, exc_value, tb):
    import traceback
    traceback.print_exception(exc_type, exc_value, tb)
    input("Press key to exit.")
    sys.exit(-1)
sys.excepthook = show_exception_and_exit

def main(window:curses.window) -> None:
  os.system("@echo off")
  os.system("cls")
  os.system(f"mode con: cols={WIDTH} lines={HEIGHT}")

  init_color()
  
  curses.curs_set(0)
  curses.cbreak()
  
  window.keypad(True)
  window.nodelay(0)

  window.clear()
  draw.draw_string(window, "Press any key...", (WIDTH//2-8,HEIGHT-2), color(GREEN, BLACK))
  window.refresh()

  window.getch()
  window.getch()

  screen.main_menu(window)

  sys.exit(0)

if __name__ == "__main__":
  curses.wrapper(main)