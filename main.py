import keyboard

print('Press and release your desired shortcut: ')

shortcut = 'caps lock+s'
print('Shortcut selected:', shortcut)


def on_triggered():
    print("Triggered!")
    keyboard.press_and_release('left')


keyboard.block_key('caps lock')

keyboard.add_hotkey('caps lock+a', lambda: keyboard.press_and_release('left'), suppress=True)
keyboard.add_hotkey('caps lock+d', lambda: keyboard.press_and_release('right'), suppress=True)
keyboard.add_hotkey('caps lock+w', lambda: keyboard.press_and_release('up'), suppress=True)
keyboard.add_hotkey('caps lock+s', lambda: keyboard.press_and_release('down'), suppress=True)

# keyboard.add_hotkey('shift+caps lock+a', lambda: keyboard.press_and_release('shift+left'), suppress=True)
# keyboard.add_hotkey('shift+caps lock+d', lambda: keyboard.press_and_release('shift+right'), suppress=True)
# keyboard.add_hotkey('shift+caps lock+w', lambda: keyboard.press_and_release('shift+up'), suppress=True)
# keyboard.add_hotkey('shift+caps lock+s', lambda: keyboard.press_and_release('shift+down'), suppress=True)

keyboard.add_hotkey('caps lock+e', lambda: keyboard.press_and_release('end'), suppress=True)
keyboard.add_hotkey('caps lock+q', lambda: keyboard.press_and_release('home'), suppress=True)

keyboard.add_hotkey('caps lock+f', lambda: keyboard.press_and_release('enter'), suppress=True)

print("Press ESC to stop.")
keyboard.wait('esc')