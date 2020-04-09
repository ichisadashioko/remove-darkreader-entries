import time
import random
import threading

from pynput.keyboard import Key, Controller, Listener

keyboard = Controller()
GB_STOP = False
GB_IS_CONTINUE = False

def on_press(key):
    global GB_IS_CONTINUE

    print(f'{key} pressed.')
    if key == Key.f9:
        GB_IS_CONTINUE = not GB_IS_CONTINUE

def on_release(key):
    global GB_STOP

    print(f'{key} release.')
    if key == Key.esc:
        # stop listener
        GB_STOP = True
        return False

def auto_delete_darkreader_entries():
    while not GB_STOP:
        if GB_IS_CONTINUE:
            # press Ctrl+a, Backspace, and Enter
            with keyboard.pressed(Key.ctrl_r):
                keyboard.press('a')
                keyboard.release('a')
            time.sleep(0.2)

            keyboard.press(Key.backspace)
            keyboard.release(Key.backspace)
            time.sleep(0.2)

            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
            time.sleep(0.2)
        else:
            time.sleep(0.5)

    print('Auto pressing thread is done.')

if __name__ == '__main__':
    # time.sleep(3)
    # Collect events until released
    listener = Listener(on_press=on_press, on_release=on_release)

    auto_pressing_thread = threading.Thread(target=auto_delete_darkreader_entries)

    listener.start()
    auto_pressing_thread.start()

    listener.join()
    auto_pressing_thread.join()