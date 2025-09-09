from tkinter import *
import os
import keyboard
import ctypes

root = Tk()

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


def assign():
    keyboard.add_hotkey("right arrow", on_hotkey)



hentai_button = Button(root, text= "Hentai Background", command= assign)
hentai_button.pack()



root.mainloop()

