import os
import keyboard
import ctypes

folder = r"C:\Users\USER\Pictures\league"
names = [f for f in os.listdir(folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
current_index = 0

def on_hotkey():
    global current_index
    full_path = os.path.join(folder, names[current_index])
    
    # Change the wallpaper
    ctypes.windll.user32.SystemParametersInfoW(20, 0, full_path, 1 | 2)
    print(f"Wallpaper changed to: {full_path}")
    
    # Move to the next image
    current_index = (current_index + 1) % len(names)

def on_reversehotkey():
    global current_index
    full_path = os.path.join(folder, names[current_index])
    
    # Change the wallpaper
    ctypes.windll.user32.SystemParametersInfoW(20, 0, full_path, 1 | 2)
    print(f"Wallpaper changed to: {full_path}")
    
    # Move to the next image
    current_index = (current_index + 1) % (len(names))   - 1
# Assign the hotkey
keyboard.add_hotkey("right arrow", on_hotkey)
keyboard.add_hotkey("left arrow", on_reversehotkey)

print("Press SHIFT + L to change wallpaper. Press ESC to quit.")
keyboard.wait('esc')
