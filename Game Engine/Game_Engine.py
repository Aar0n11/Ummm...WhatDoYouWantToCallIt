import time
import keyboard

a = 0

def move(key):
        print(key)
        time.sleep(0.1)

keyboard.add_hotkey("a", lambda: move("a"))
keyboard.add_hotkey("d", lambda: move("d"))
keyboard.add_hotkey("w", lambda: move("w"))
keyboard.add_hotkey("s", lambda: move("s"))