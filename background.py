import keyboard
import ctypes
import os

<<<<<<< HEAD


image_path = r"C:\Users\USER\Pictures\programtest\mary.png"



for files in os.path.join(r"C:\Users\USER\Pictures\programtest", ):
    keyboard.add_hotkey(". + ,")
    ctypes.windll.user32.SystemParametersInfoW(20, 0, files, 1 | 2)
=======
def change_wallpaper(image_path):
    # Constants for setting the wallpaper
    SPI_SETDESKWALLPAPER = 20  # Action to change wallpaper
    SPIF_UPDATEINIFILE = 0x01  # Update user profile
    SPIF_SENDWININICHANGE = 0x02  # Notify change to system
>>>>>>> a4ff5254f4a05c5508097535b2b2a1d7252b697d

    try:
        # Call Windows API to change wallpaper
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path,
                                                   SPIF_UPDATEINIFILE | SPIF_SENDWININICHANGE)
        return True
    except Exception as e:
        # Print error message if wallpaper change fails
        print(f"Error changing wallpaper: {e}")
        return False
    


names = []
for name in os.listdir(r"C:\Users\KSEQUEIRA\Documents\backgroundimages"):
    names.append(name) 
    
full_path = []
for name in names:
    full_pathtest = os.path.join(r"C:\Users\KSEQUEIRA\Documents\backgroundimages", name)
    full_path.append(full_pathtest)

def on_hotkey():
    for image in full_path:
        change_wallpaper(image)

keyboard.add_hotkey("shift + l", on_hotkey)

keyboard.wait()
