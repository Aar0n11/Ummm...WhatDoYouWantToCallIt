import keyboard

def moveleft():
    print("a")

def moveright():
    print("d")

def moveup():
    print("w")

def movedown():
    print("s")

keyboard.add_hotkey("a", lambda: moveleft())
keyboard.add_hotkey("d", lambda: moveright())
keyboard.add_hotkey("w", lambda: moveup())
keyboard.add_hotkey("s", lambda: movedown())