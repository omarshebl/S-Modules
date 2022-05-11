from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from os import system, name
from time import sleep
from sys import argv
import pandas as pd

options = Options()
options.page_load_strategy = 'eager'
driver = webdriver.Safari(options=options)

driver.get("http://web.whatsapp.com")

searchXPath = '//div[@contenteditable="true"][@data-tab="3"]'
messageXPath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]'

df = pd.read_excel("contacts.xls")
Number = df['Phone'].tolist()
Name = df['Sent Name'].tolist()
Gender = df['Gender'].tolist()
Religion = df['Religion'].tolist()
type1 = ""

for i in range(15, 0, -1):
    sleep(1)
    print(i)

print("Sending Now !")

def clearConsole():
    command = 'clear'
    if name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    system(command)

def sendMessage(inputM, inputN):
    search = WebDriverWait(driver,500).until(EC.presence_of_element_located((By.XPATH, searchXPath)))
    sleep(2)

    search.send_keys(inputN)
    sleep(1)
    search.send_keys(Keys.ENTER)
    sleep(2)

    message = driver.find_element(By.XPATH, messageXPath)
    message.click()

    sleep(2)

    message.send_keys(inputM)
    sleep(1)
    message.send_keys(Keys.ENTER)
    clearConsole()
    print('Sent to Number: ' + str(inputN))

def NewYear():
    for i, j, k in zip(Number, Name, Gender):
        if str(k) == "m":
            type1 = "انتا طيب يا " 
        elif str(k) == "f":
            type1 = "انتي طيبه يا "

        messageStr = "كل سنه و" + type1 + str(j) + "❤️ "
        sendMessage(messageStr,i)
        
def Ramadan():
    for i, j, k, r in zip(Number, Name, Gender, Religion):
        if (r != 'c'):
            messageStr = "رمضان كريم يا " + str(j) + "❤️ "
            sendMessage(messageStr,i)

def Eid(re):
    for i, j, k, r in zip(Number, Name, Gender, Religion):
        if (r == re):
            messageStr = "عيد سعيد يا " + str(j) + "❤️ "
            sendMessage(messageStr,i)

if(len(argv) > 1): 
    if(argv[1].lower() == "ramadan"): Ramadan()
    elif(argv[1].lower()== "newyear"): NewYear()
    elif(argv[1].lower()== "eid"): Eid(argv[2].lower())

Eid("m")

clearConsole()
print("Done !")
sleep(2)
driver.quit()

