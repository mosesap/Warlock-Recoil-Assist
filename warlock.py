import time
import json
import win32api
import win32con
from playsound import playsound
 
LMB = 0x01 
RMB = 0x02
end = 0x2E
enable = 0x2D
rel = 0x52
loadout = 0x48
swap1 = 0x31
swap2 = 0x32

def is_mb_pressed():
    return win32api.GetKeyState(LMB) < 0 and win32api.GetKeyState(RMB) < 0

def is_end_pressed():
    return win32api.GetKeyState(end) < 0

def is_reload_pressed():
    return win32api.GetKeyState(rel) < 0

def is_loadout_pressed():
    return win32api.GetKeyState(loadout) < 0

def is_swap_pressed():
    if win32api.GetKeyState(swap1) < 0 or win32api.GetKeyState(swap2) < 0:
        time.sleep(.05)
        return True
    return False
 
def mouse_move_relative(dx, dy):
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int(dx), int(dy), 0, 0)

def repeat_sound(x, sound):
    while x > 0:
        playsound(sound)
        time.sleep(.1)
        x -= 1

def load_guns_json():
    with open('guns.json') as f:
        return json.load(f)

def get_loadout(loadout):
    if loadout:
        return True
    start_time = time.time()
    while is_loadout_pressed():
        if time.time() - start_time > 1:
            repeat_sound(2, 'hitmarker.wav')
            return True
    return False

def load_gun(armed, guns):
    if win32api.GetKeyState(0x31) < 0:
        repeat_sound(2, 'hitmarker.wav')
        return guns['ONE']
    elif win32api.GetKeyState(0x32) < 0:
        repeat_sound(2, 'hitmarker.wav')
        return guns['TWO']
    elif win32api.GetKeyState(0x33) < 0:
        repeat_sound(2, 'hitmarker.wav')
        return guns['THREE']
    elif win32api.GetKeyState(0x34) < 0:
        repeat_sound(2, 'hitmarker.wav')
        return guns['FOUR']
    elif win32api.GetKeyState(0x35) < 0:
        repeat_sound(2, 'hitmarker.wav')
        return guns['FIVE']
    elif win32api.GetKeyState(0x36) < 0:
        repeat_sound(2, 'hitmarker.wav')
        return guns['SIX']
    elif win32api.GetKeyState(0x37) < 0:
        repeat_sound(2, 'hitmarker.wav')
        return guns['SEVEN']
    elif win32api.GetKeyState(0x38) < 0:
        repeat_sound(2, 'hitmarker.wav')
        return guns['EIGHT']
    elif win32api.GetKeyState(0x39) < 0:
        repeat_sound(2, 'hitmarker.wav')
        return guns['NINE']
    elif win32api.GetKeyState(0x30) < 0:
        repeat_sound(2, 'hitmarker.wav')
        return guns['TEN']
    else: 
        time.sleep(.05)
        return armed

def is_enabled(enabled)->bool:
    if win32api.GetKeyState(enable) < 0:
        time.sleep(.05)
        enabled = not enabled
        if enabled: playsound('hitmarker.wav')
    return enabled
            
def main():
    enabled = False
    armed = []
    index = 0
    guns = load_guns_json()
    loadout = False
    while True:
        start = time.time()
        enabled = is_enabled(enabled)
        loadout = get_loadout(loadout)
        if loadout:
            armed = []
            armed = load_gun(armed, guns)
            if armed: loadout = False
            continue
        if enabled and armed:
            if is_mb_pressed() and index < len(armed["RECOIL"]):
                mouse_move_relative(armed['RECOIL'][index][0], armed["RECOIL"][index][1])
                index += 1
                time.sleep((60/armed["RPM"]) - (time.time() - start))
                continue
        if is_reload_pressed():
            index = 0
        if is_swap_pressed():
            enabled = not enabled
            index = 0
        if is_end_pressed():
            repeat_sound(4, 'hitmarker.wav')
            break 

if __name__ == "__main__":
    main()