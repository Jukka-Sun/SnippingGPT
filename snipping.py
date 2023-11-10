import subprocess
from datetime import datetime
import os

# Function to capture a screenshot
def capture_screenshot():
    screenshots_dir = '/Users/jukson/Documents/GPT/SnippingGPT/screenshots'
    if not os.path.exists(screenshots_dir):
        os.makedirs(screenshots_dir)

    file_name = datetime.now().strftime('%Y-%m-%d_%H-%M-%S-screenshot.png')
    file_path = os.path.join(screenshots_dir, file_name)
    
    subprocess.run(['screencapture', '-i', file_path])
    print(f"Screenshot saved to {file_path}")
    return file_path
