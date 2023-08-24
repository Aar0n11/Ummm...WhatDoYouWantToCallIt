import subprocess
import keyboard

def move(key):


keyboard.add_hotkey("a", lambda: move("a"))
keyboard.add_hotkey("d", lambda: move("d"))
keyboard.add_hotkey("w", lambda: move("w"))
keyboard.add_hotkey("s", lambda: move("s"))