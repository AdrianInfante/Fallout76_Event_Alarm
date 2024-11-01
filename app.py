import pyautogui
import time
import winsound
import os
import sys


target_image_path = "./event.png"
alert_sound_path = "./alert.wav"  

def find_image_on_screen(image_path):
    try:
        # Attempt to locate the image on the screen with a lower confidence level
        location = pyautogui.locateOnScreen(image_path, confidence=0.8)
        if location:
            print("Image found on screen!")
            winsound.PlaySound(alert_sound_path, winsound.SND_FILENAME) 
            return True
        else:
            return False
    except pyautogui.ImageNotFoundException:
        print("Image could not be processed or found.")
        return False


def main():
    while True:
        found = find_image_on_screen(target_image_path)
        
        if found:
            print("Restarting script...")
            time.sleep(2)  
            # Restart the script
            os.execv(sys.executable, ['python'] + sys.argv)

        time.sleep(2)  
    


if __name__ == "__main__":
    main()
