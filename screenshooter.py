import pyautogui
import keyboard
import os

# set the directory
save_directory = r"C:\Users\Adrian\Desktop\Screenshoter\screenshots"

# create the directory if doesn't exist
if not os.path.exists(save_directory):
    os.makedirs(save_directory)

counter = 1

def take_screenshot():
    global counter
    filename = os.path.join(save_directory, f'{counter:04d}.png')
    # take the screenshot
    screenshot = pyautogui.screenshot()
    # save the screenshot
    screenshot.save(filename)
    print(f"Screenshot saved as {filename} in {save_directory}")
    counter += 1

# screenshot hotkey
keyboard.add_hotkey('F9', take_screenshot)

print("Press F9 to take a screenshot. Press F4 to exit.")

# keep program running until F4
keyboard.wait('F4')