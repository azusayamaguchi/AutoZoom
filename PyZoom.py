import subprocess
import importlib
import sys
Required_Modules=['selenium','chromedriver_autoinstaller','pyscreeze','time','datetime','pyautogui','opencv-python','Pillow']
for module in Required_Modules:
    try:
        importlib.import_module(module)
    except ImportError as e:
        print(f'install {module}')
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', module])

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

import chromedriver_autoinstaller
import pyscreeze
from pyscreeze import ImageNotFoundException
pyscreeze.USE_IMAGE_NOT_FOUND_EXCEPTION = True
import time
import datetime
import pyautogui as pa
from sys import exit
#from pathlib import Path
chromedriver_autoinstaller.install()
pa.useImageNotFoundException()

def StartZOOM(MeetingID,url):
    #url = 'https://zoom.us/join'
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")  # Open browser in maximized mode
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # Disable automation control detection
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

    #driver = webdriver.Chrome()
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    wait = WebDriverWait(driver,60)
    time.sleep(3)
    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//button[@id="onetrust-accept-btn-handler"]'))).click()
        print("accepted cookies")
    except Exception as e:
        print('no cookie button')

    target = driver.find_element(By.ID,"join-confno")
    target.send_keys(MeetingID)
    btn = driver.find_element(By.ID,"btnSubmit").click()
    return driver

def FindLoc(pngfile):
    while True:
        try:
            p= pa.locateCenterOnScreen(pngfile,grayscale=False,confidence=0.7)
            if(p is not None):
                print('location:',p)
                break
        except pa.ImageNotFoundException:
            print(f"{pngfile} image not found, will exit")
            sc = pa.screenshot()
            name = 'screenshot%s.png' % (datetime.datetime.now().strftime('%Y-%m%d_%H-%M-%S-%f'))
            sc.save(name)
            exit()
    return p

def MeetingMinute(MeetingDuration):
    minutes =0
    second = 0
    if MeetingDuration[-1]=='h' :
        minutes=60*float(MeetingDuration[:-1])
    elif MeetingDuration[-1]=='m':
        minutes= float(MeetingDuration[:-1])
    return 60*minutes

def AutoZoom(MeetingID,MeetingDuration,url='http://zoom.us/join',Passcode=None):

    #url = 'https://zoom.us/join'
    driver=StartZOOM(MeetingID,url)
    #driver.maximize_window()
    time.sleep(3)
    p_zu=FindLoc('zoom_us.png')
    pa.moveTo(p_zu.x/2,p_zu.y/2)
    pa.click(p_zu.x/2, p_zu.y/2,clicks=2, interval=1)
    time.sleep(3)

    if Passcode =='None': Passcode=None
    if Passcode is not None:
        time.sleep(5)
        p_pc=FindLoc('zoom_pc.png')
        pa.moveTo(p_pc.x/2,p_pc.y/2)
        pa.write(Passcode)
        pa.press('enter')
    else: 
        time.sleep(10)
        p_join=FindLoc('zoom_join.png')
        pa.moveTo(p_join.x/2,p_join.y/2)
        pa.click(p_join.x/2, p_join.y/2,clicks=2, interval=1)
    
    time.sleep(10)
    # mic is muted
    pa.hotkey('command','shift','A')
    time.sleep(3)
    pa.hotkey('enter')

    time.sleep(MeetingMinute(MeetingDuration))

    #Leaving prompt
    pa.hotkey('command','q')
    time.sleep(3)
    pa.hotkey('enter')
    driver.close()

    return
