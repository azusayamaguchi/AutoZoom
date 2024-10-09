# AutoZoom
This Python project is designed specifically for MacOS and uses crontab to schedule Zoom meetings. It automates the process with selenium and pyautogui, which handle launching Zoom at the scheduled time, entering the Meeting ID, and joining the meeting with the microphone muted. Since the project involves controlling the system's GUI, you need to grant accessibility permissions to both Python and any automation tools (pyautogui and selenium) in MacOS System Preferences for the script to function properly.
# Overview
AutoZoom is a Python-based automation tool designed to simplify the process of joining Zoom meetings. It uses Selenium for browser control and PyAutoGUI for handling pop-up windows, allowing users to join meetings seamlessly.
# Code Environment
macOS: Sonoma 14.2.1
Python: 3.12.5
# Code Description
The types of pop-up windows that Selenium can control include:

Alert: A simple warning that requires an "OK" response.

Prompt: Requires user input for a user ID or password.

Confirmation: Requests approval for actions like closing a site.

Pop-up windows controlled by the operating system of the application being launched cannot be handled by Selenium. Therefore, the simplest method is to use PyAutoGUI's screen position detection and click functionality.

For the Zoom application:

Use the image of the "Open zoom.us?" pop-up button as zoom_us.png.

If the meeting requires a passcode, use the image of the passcode input field as zoom_pc.png.

In paid Zoom accounts, the host can either allow entry from the waiting room or require a passcode. In the free version, passcode entry is the default. Use the image of the waiting room entry button as zoom_join.png.

In the StartZoom function , Selenium launches a browser, navigates to zoom.us/join, and inputs the Meeting ID while accepting cookies. The FindLoc function retrieves the screen positions of the images zoom_us.png, zoom_pc.png, and zoom_join.png. The positions obtained using PyAutoGUI are divided by two, as macOS outputs the positions at twice the size.The file containing the above functions is named PyZoom.py.  It is imported as PZ, and in main_zoom.py, we call the AutoZoom function, specifying the Meeting ID, the presence of a Meeting Passcode, and the Meeting Duration. After entering the meeting, the microphone is muted, and when the meeting time expires, a prompt to exit is displayed.

# Scheduling with Crontab
macOS Setup

To use PyAutoGUI with crontab on macOS, the following steps are necessary:

Grant Access for Screen Capture

Open System Preferences.

Navigate to Privacy & Security > Screen & System Audio Recording.

Add python3 and Terminal to the list of allowed apps. To do this quickly, click the + button and then press Command + Shift + G to enter the path.

Allow Access for Python and Terminal

In System Preferences, go to Privacy & Security > Accessibility.

Similarly, add python3 and Terminal to the list of allowed apps.

Grant Full Disk Access to Terminal and Cron

Navigate to System Preferences > Privacy & Security > Full Disk Access.

Add cron and Terminal to the list of allowed apps.

To schedule tasks with crontab, we will use the subprocess module and PyAutoGUI for setting the time and writing the command.

Required Parameters:
Meeting ID, meeting time, meeting date, and, if needed, the passcode. These parameters will be passed to main.py.

Functionality of main.py:

The main.py script will convert the meeting schedule into a format suitable for crontab and write the execution command to crontab.

Launching Zoom:
The actual code to launch Zoom will be called in main_zoom.py, where the Meeting ID, meeting time, and Passcode were provided as arguments.

# Usage 
python main.py --MeetingID='XXX XXXX XXXX' --Passcode='XXXXXX' --MeetingTime='30m' --MeetingSchedule='date/month/year HH:mm'
