#Used to read the csv file
import pandas  as pd
#Used to relocate the csv file
import os
import shutil
from shutil import copy2
#Used to easliy get the averages of the data to then analysis it
from datafuncs import datafuncs as funcs
#Used to open the mircobit csv file website and download the data
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
'''from webdriver_manager.chrome import ChromeDriverManager'''

#This is the analysiing function. It uses the recommended temperature,sound level, light level and sleep cycle time to determine what the issue might be with your sleep
def Analysis(Time, Temp, Sound, Light):
    if Time % 120 == 0:
        TimeA = True
    else:
        TimeA = False
    
    if funcs.mean(Light) <= 50:
        LightA = True
    else:
        LightA = False
    
    if funcs.mean(Sound) <= 40:
        SoundA = True
    else:
        SoundA = False
    
    if funcs.mean(Temp) <= 19 and funcs.mean(Temp) >= 17:
        TempA = True
    else:
        TempA = False
        
    if not TempA:
        print("Temperature is not between 17 and 19 degrees. Fix this to improve sleep")
    
    if not SoundA:
        print("Room is too noisy to sleep in. Find a less noisy area.")
        
    if not LightA:
        print("Room is too bright. Maybe sleep with the lights fully off.")
    
    if not TimeA:
        print("You're not sleeping in full REM cycles. Fix this and you'll have a better sleep.")
    print(f"This is table grading sleep True means your sleep fine in this area while false means you need to fix it\nTime = {TimeA}\nLight = {LightA}\nSound = {TempA}\nTime = {TempA}")
"""
#THis code opens the Mircobit files when it connected to computer opens the file to download the csv file , downloads it then quits the webpage
NOT COMPATIBLE WITH OLDER VERSIONS OF MICROBIT
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("file:///D:MY_DATA.HTM")
sleep(1)
button=driver.find_element(By.XPATH,"/html/body/div/div/button[1]")
button.click()
sleep(10)
driver.quit()
"""
#Moves the file from downloads to the correct spot
source_file = r'C:\Users\User\Downloads\microbit (1).csv'
#The above line only works if the file directory is mapped to your pc exact directory please change it before running or else this code will not run
destination_dir = os.path.dirname(source_file)
destination_file = os.path.join(destination_dir, 'microbit (1).csv')
shutil.move(source_file, destination_file,copy_function=copy2)
# Read the CSV file
data = pd.read_csv(os.path.join(destination_dir, 'microbit (1).csv'))
#Saving all the colums as Variable arrays to make it easier to use the function
Temp = data['Temperature']
Time = data['Time']
Sound = data['Sound']
Light = data['Light']
Timer = data['Time'].iloc[-1]
#Perform analysis
Analysis(Timer, Temp, Sound, Light)


 