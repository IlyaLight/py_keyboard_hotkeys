import keyboard
from pynput.keyboard import Key, Controller

TRIGGER = 'caps lock'

pynput_keyboard = Controller()

keyboard.block_key(TRIGGER)

keyboard.add_hotkey(f'{TRIGGER} + a', lambda: keyboard.press_and_release('left'), suppress=True)
keyboard.add_hotkey(f'{TRIGGER} + d', lambda: keyboard.press_and_release('right'), suppress=True)
keyboard.add_hotkey(f'{TRIGGER} + w', lambda: keyboard.press_and_release('up'), suppress=True)
keyboard.add_hotkey(f'{TRIGGER} + s', lambda: keyboard.press_and_release('down'), suppress=True)

keyboard.add_hotkey(f'{TRIGGER} + n', lambda: keyboard.press_and_release('0'), suppress=True)
keyboard.add_hotkey(f'{TRIGGER} + m', lambda: keyboard.press_and_release('1'), suppress=True)
keyboard.add_hotkey(f'{TRIGGER} + comma', lambda: keyboard.press_and_release('2'), suppress=True)
keyboard.add_hotkey(f'{TRIGGER} + dot', lambda: keyboard.press_and_release('3'), suppress=True)
keyboard.add_hotkey(f'{TRIGGER} + j', lambda: keyboard.press_and_release('4'), suppress=True)
keyboard.add_hotkey(f'{TRIGGER} + k', lambda: keyboard.press_and_release('5'), suppress=True)
keyboard.add_hotkey(f'{TRIGGER} + l', lambda: keyboard.press_and_release('6'), suppress=True)
keyboard.add_hotkey(f'{TRIGGER} + u', lambda: keyboard.press_and_release('7'), suppress=True)
keyboard.add_hotkey(f'{TRIGGER} + i', lambda: keyboard.press_and_release('8'), suppress=True)
keyboard.add_hotkey(f'{TRIGGER} + o', lambda: keyboard.press_and_release('9'), suppress=True)


def key_code_plus_key(key):
    pynput_keyboard.press(Key.shift)
    pynput_keyboard.press(key)
    pynput_keyboard.release(key)
    pynput_keyboard.release(Key.shift)


keyboard.add_hotkey('shift+caps lock + a', key_code_plus_key, (Key.left,), suppress=True)
keyboard.add_hotkey('shift+caps lock + d', key_code_plus_key, (Key.right,), suppress=True)
keyboard.add_hotkey('shift+caps lock + w', key_code_plus_key, (Key.up,), suppress=True)
keyboard.add_hotkey('shift+caps lock + s', key_code_plus_key, (Key.down,), suppress=True)

keyboard.add_hotkey(f'{TRIGGER} + e', lambda: keyboard.press_and_release('end'), suppress=True)
keyboard.add_hotkey(f'{TRIGGER} + q', lambda: keyboard.press_and_release('home'), suppress=True)
keyboard.add_hotkey(f'{TRIGGER} + f', lambda: keyboard.press_and_release('enter'), suppress=True)

print("Press ESC to stop.")
keyboard.wait('esc')


