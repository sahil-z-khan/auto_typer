import time
import random
import pyautogui

# Safety: move mouse to top-left corner to abort typing
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0  # no extra pause between pyautogui calls

# 🔹 Put whatever text you want typed here.
TEXT_TO_TYPE = """
This is where you paste the text you want typed into Word.
You can include multiple lines, punctuation, etc.
The script will type it out as if a person is typing.
"""

def human_type(text, base_min=0.03, base_max=0.18):
    """
    Type text with random delays between keystrokes to mimic a human.
    base_min/base_max are the typical per-character delays in seconds.
    """
    for ch in text:
        # Actually press the key
        pyautogui.write(ch)

        # Space / punctuation can have slightly longer pauses
        if ch in {'.', ',', '!', '?', ';', ':'}:
            delay = random.uniform(base_min * 3, base_max * 4)
        elif ch == ' ':
            delay = random.uniform(base_min * 1.5, base_max * 2.5)
        elif ch == '\n':
            delay = random.uniform(base_min * 2, base_max * 3)
        else:
            delay = random.uniform(base_min, base_max)

        time.sleep(delay)

if __name__ == "__main__":
    print("You have 5 seconds to click into Word and put your cursor where you want to start typing...")
    time.sleep(5)

    print("Typing started. Move your mouse to the top-left corner of the screen to STOP.")
    human_type(TEXT_TO_TYPE)
    print("Done.")
