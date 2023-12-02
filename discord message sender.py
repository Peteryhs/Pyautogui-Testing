import pyautogui
import time
import random

# Open the start menu
pyautogui.press('win')

# Wait for the start menu to open
time.sleep(1)

# Type 'discord' to search for Discord
pyautogui.typewrite('discord')

# Wait for the search results to appear
time.sleep(1)

# Press enter to open Discord
pyautogui.press('enter')

# Wait for Discord to open
time.sleep(5)  # Adjust this based on your computer speed

# Click on a specific user
# Replace (x, y) with the coordinates of the user
pyautogui.click(840, 1048)


# List of messages
messages = ["Hello", "How are you?", "I'm good, thanks!"]

# Number of times to send a message
num_messages = 10

# Time delay between messages (in seconds)
delay = 1

for _ in range(num_messages):
    # Select a random message
    message = random.choice(messages)

    # Type the message
    pyautogui.typewrite(message)

    # Press enter to send the message
    pyautogui.press('enter')

    # Wait for the specified delay
    time.sleep(delay)
