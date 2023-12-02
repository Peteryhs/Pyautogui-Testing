import pyautogui
import time
import webbrowser
import pytesseract

# Set the path to the tesseract executable
# You will need to install Tesseract and set this path correctly
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Open Monkey Type website
webbrowser.open('https://monkeytype.com')

# Wait for the website to load
time.sleep(5)

# Define the top-left and bottom-right corners of the initial region
initial_top_left = (73, 504)
initial_bottom_right = (2471, 875)


# Calculate the width and height of the initial region
width = initial_bottom_right[0] - initial_top_left[0]
height = initial_bottom_right[1] - initial_top_left[1]

# Define the top-left corner of the new line region
new_line_top_left = (85, 703)  # You will need to adjust these coordinates

# Perform the OCR and typing process 4 times (1 initial + 3 additional)
for i in range(4):
    # Use the initial coordinates for the first iteration and the new line coordinates for the others
    top_left = initial_top_left if i == 0 else new_line_top_left

    # Take a screenshot at the current position
    screenshot = pyautogui.screenshot(region=(top_left[0], top_left[1], width, height))

    # Save the screenshot for debugging
    screenshot.save('C:/Users/peter/Documents/screenshot.png')

    # Use pytesseract to extract text from the image
    text = pytesseract.image_to_string(screenshot)

    # Split the text into lines
    lines = text.splitlines()

    # Remove the first line containing '@english'
    lines = lines[1:]

    # Join the remaining lines back into a single string
    text = ' '.join(lines)

    # Click on the text input area
    pyautogui.click(960, 540)  # You may need to adjust these coordinates

    # Type the extracted text twice as fast
    pyautogui.typewrite(text, interval=0.05)  # Adjust the interval as needed

    # Wait for the next line to appear (9 seconds for the first iteration, 1 second for the others)
    time.sleep(5 if i == 0 else 1)
