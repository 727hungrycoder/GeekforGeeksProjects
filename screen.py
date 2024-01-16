# importing the required packages
import pyautogui
import cv2
import numpy as np

# Specify resolution
resolution = (1920, 1080)

# Specify video codec
codec = cv2.VideoWriter_fourcc(*"mp4v")

# Specify name of Output file
filename = "Recording.mp4v"

# Specify frames rate. We can choose any
# value and experiment with it
fps = 60.0


# Creating a VideoWriter object
out = cv2.VideoWriter(filename, codec, fps, resolution)

# Create an Empty window
cv2.namedWindow("Live", cv2.WINDOW_NORMAL)

# Resize this window
cv2.resizeWindow("Live", 480, 270)

while True:
    SCREEN_SIZE = resolution
    # Take screenshot using PyAutoGUI
    img = pyautogui.screenshot(region=(0, 0, SCREEN_SIZE[0], SCREEN_SIZE[1]))

    # Convert the screenshot to a numpy array
    frame = np.array(img)

    # Convert it from BGR(Blue, Green, Red) to
    # RGB(Red, Green, Blue)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Write it to the output file
    out.write(frame)

    # Optional: Display the recording screen
    cv2.imshow('Live', frame)

    # Stop recording when we press 'q'
    if cv2.waitKey(1) == ord('q'):
        break

# Release the Video writer
out.release()

# Destroy all windows
cv2.destroyAllWindows()


"""Importing Packages:

pyautogui: For taking screenshots.
cv2 (OpenCV): For video processing.
numpy: For array manipulation.
Setting Up Video Parameters:

resolution: The resolution of the video (width, height).
codec: Video codec used for writing the video (XVID in this case).
filename: Name of the output video file.
fps: Frames per second for the video.
Creating VideoWriter Object:

cv2.VideoWriter: An object that will write the video file.
Recording Loop:

The script enters a loop where it continuously takes screenshots using PyAutoGUI.
Converts the screenshot to a NumPy array and then from BGR to RGB format.
Writes each frame to the video file.
Optionally displays the recording screen in a window.
Exit Condition:

The loop continues until the user presses 'q'.
Release Resources:

After the loop, it releases the video writer and destroys all windows.
To run the script, you may need to install the required packages using:

bash
Copy code
pip install pyautogui opencv-python numpy
If the AVI file is not opening correctly after running the script, it could be due to various reasons. Here are some common troubleshooting steps you can take:

Check if Video Codec is Installed:

Ensure that the video codec specified in cv2.VideoWriter_fourcc(*"XVID") is installed on your system. XVID is a common codec, but you can try other codecs like MJPG or DIVX.
Try Different File Formats:

Instead of using AVI, try saving the video in a different format such as MP4 (use cv2.VideoWriter_fourcc(*"mp4v")).
Update OpenCV:

Make sure you have the latest version of OpenCV installed. You can update it using:
bash
Copy code
pip install --upgrade opencv-python
Check File Path:

Verify that the specified file path (filename = "Recording.avi") is correct and the script has permission to write to that location.
Install Appropriate Video Player:

Make sure you have a video player installed on your system that supports the AVI format. VLC Media Player is a good choice.
Use Different Video Players:

Try opening the file with different video players to see if the issue persists. Sometimes, the default player may not support certain codecs.
Check for Errors:

Run the script in a terminal and check for any error messages. This might provide insights into what could be going wrong.
Test with Different Resolutions and Frame Rates:

Experiment with different resolutions and frame rates to see if that makes a difference.
Try Without Displaying Live Window:

Comment out the lines related to displaying the live window (cv2.namedWindow, cv2.resizeWindow, cv2.imshow). Sometimes, displaying a live window can interfere with video writing.
Use Full Path for File Name:

Instead of just "Recording.avi," try using the full path to the file (e.g., "C:/path/to/Recording.avi").
If you try these steps and still face issues, you may want to provide additional details about any error messages or behaviors you observe.




User
It seems that there is a NameError because the variable SCREEN_SIZE is not defined in your code. You need to define SCREEN_SIZE before using it in the pyautogui.screenshot function.

Here's an example of how you can define SCREEN_SIZE using the resolution variable from your code:

python
Copy code
# Specify resolution
resolution = (1920, 1080)

# Specify video codec
codec = cv2.VideoWriter_fourcc(*"XVID")

# Specify name of Output file
filename = "Recording.avi"

# Specify frames rate. We can choose any 
# value and experiment with it
fps = 60.0

# Specify SCREEN_SIZE based on the resolution
SCREEN_SIZE = resolution

# Creating a VideoWriter object
out = cv2.VideoWriter(filename, codec, fps, resolution)

# ... rest of your code ...
Make sure to place this definition before the line where you use SCREEN_SIZE in the pyautogui.screenshot function. This should resolve the NameError. Adjust the SCREEN_SIZE variable according to your desired screen size or resolution."""