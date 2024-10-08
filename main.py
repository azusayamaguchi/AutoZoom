
def DateToCron(MeetingDateTime):
    import datetime
    MeetingDT = datetime.datetime.strptime(MeetingDateTime, '%d/%m/%y %H:%M')
    sunday_as_zero = (MeetingDT.weekday() + 1) % 7
    return f'{MeetingDT.minute} {MeetingDT.hour} {MeetingDT.day} {MeetingDT.month} {sunday_as_zero} '


if __name__ == '__main__':

    import argparse
    import pyautogui as pa
    import os
    import time
    import subprocess
    import PyZoom as PZ
    from pathlib import Path

    parser = argparse.ArgumentParser(description="Pass meeting details as arguments.")
    # Adding arguments
    parser.add_argument("--MeetingID", required=True, help="Meeting ID")
    parser.add_argument("--Passcode", default=None, help="Passcode for the meeting")
    parser.add_argument("--MeetingTime", required=True, help="Time of the meeting")
    parser.add_argument("--MeetingSchedule", required=True, help="Date and time of the meeting")
    args = parser.parse_args()
    strArgs=f"--MeetingID='{args.MeetingID}' --MeetingTime='{args.MeetingTime}' --Passcode='{args.Passcode}'"

    # Parse the arguments

    strCron=DateToCron(args.MeetingSchedule)
    home_directory = Path.home()
    strCron=strCron+f'source {home_directory}/.zshrc; cd {home_directory}/Zoom/AutoZOOM; python {home_directory}/Zoom/AutoZOOM/main_zoom.py  {strArgs} >> /tmp/test.txt 2>&1'

    subprocess.run(["open", "-a", "Terminal"])
    pa.write('crontab -e')
    pa.press('enter')  

    time.sleep(2)
    pa.press('i')
    pa.write('PATH=/usr/sbin:/usr/bin:/bin:/usr/local/bin \nSHELL=/bin/zsh \n')
    pa.write(strCron)

    pa.press('esc')            # Confirm save (if asked)
    pa.write(':wq')   # Exit nano
    pa.press('enter')  

