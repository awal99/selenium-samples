from skpy import Skype
from getpass import getpass
import re
from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options
import time, os, sys, json, time, base64
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#loginto browser first

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-logging')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--window-size=1920,1080')
chrome_options.add_argument('--log-level=3')

driver = webdriver.Chrome('chromedriver', options=chrome_options)
driver.maximize_window()

driver.get("https://outlook.live.com/owa/?nlp=1")
time.sleep(5)
inputElement = driver.find_element(By.NAME,"loginfmt")
inputElement.send_keys("email")
nextButton = driver.find_element("id","idSIButton9")
nextButton.click()
time.sleep(3)
inputElement = driver.find_element(By.NAME,"passwd")
inputElement.send_keys("password")
nextButton = driver.find_element("id","idSIButton9")
nextButton.click()
time.sleep(5)
if(driver.title == "Did you request a security info change?"):
    with open("test.html", "w") as file:
        file.write(driver.page_source)
    
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "iLandingViewAction"))
    )
    # verify = driver.find_element("id","iLandingViewAction")
    element.click()
print(driver.title)
with open("test1.html", "w") as file:
        file.write(driver.page_source)
submit = driver.find_element("id","idSIButton9")
submit.click()
print(driver.title)



sk = Skype()
sk.conn.soapLogin("email", 'password')
#sk.getSkypeToken()
sk.conn

ch = sk.chats["4:+16507502035"]
message = ch.getMsgs()[0]
sms_html = message.content
links = re.findall('<body>(.*?)</body>', sms_html)
print(links)
#now we have the string message. lets parse for the code
code = re.findall('\d',links[0])
print(''.join(code))