Here's a README file tailored for your script:

---

# Fallout 76 Event Alert Script

This Python script helps players detect in-game events in Fallout 76 by watching for a specific event image on the screen. When the specified image appears, the script will play an alert sound, letting you know that an event is available—even if you're away from the keyboard.

## Features

- **Automatic Event Detection:** The script continually scans the screen for the specified event image.
- **Sound Alert:** Plays an alert sound when the event image appears, notifying you instantly.
- **Script Restart:** Automatically restarts the scan after detecting an event, so you'll be alerted for each occurrence.

## Requirements

- **Python**: Make sure Python is installed on your system (3.7 or later recommended).
- **Python Libraries**: This script uses the `pyautogui`, `time`, `winsound`, `os`, and `sys` libraries.

### Install dependencies
Install the required Python libraries using:
```cmd
pip install -r requirements.txt
```

> **Note:** The `winsound` library is Windows-only. For non-Windows systems, use a cross-platform alternative like `playsound`.

## Setup

1. **Add the Target Image**: Capture an image of the Fallout 76 event notification (`event.png`) and save it in the script's directory.
2. **Add an Alert Sound**: Add a `.wav` file for the alert sound (`alert.wav`) and save it in the script's directory.

## Usage

1. **Run the Script**:
   ```cmd
   python fallout76_event_alert.py
   ```
2. **Minimize Fallout 76** or leave it running in windowed mode. The script will scan for the event image and alert you with a sound when it appears on screen.

3. **Adjusting Confidence Level**:
   If the script fails to detect the event reliably, adjust the `confidence` parameter in the `find_image_on_screen` function.

## Script Details

- **`find_image_on_screen(image_path)`**: Scans the screen for the specified image with a customizable confidence level.
- **`main()`**: Continuously monitors for the image and triggers a sound alert when detected. Restarts after a brief delay to re-enable detection for future events.

## Disclaimer

This script is intended for personal use only and may not be compatible with other applications.

---

Feel free to customize this as needed!
