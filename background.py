import keyboard
import ctypes
import os



image_path = r"C:\Users\USER\Pictures\programtest\mary.png"



for files in os.path.join(r"C:\Users\USER\Pictures\programtest", ):
    keyboard.add_hotkey(". + ,")
    ctypes.windll.user32.SystemParametersInfoW(20, 0, files, 1 | 2)

