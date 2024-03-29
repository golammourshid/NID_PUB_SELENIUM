import time
from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import csv
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
ser = Service('C://Program Files//Google//Chrome//Application//chromedriver.exe')
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)


driver.get("https://prportal.nidw.gov.bd/nid-pub/")
driver.maximize_window()
driver.implicitly_wait(25)
# driver.maximize_window()

# file = open('get_started.csv', encoding='utf-8')
# csvreader = csv.reader(file)

# header = []
# header = next(csvreader)
# next(csvreader)
# rows = []
# for row in csvreader:
#     rows.append(row)
# print(rows[0][0])

time.sleep(2)

# Right menu for small window
# driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/div[3]/div[2]/i").click()
# time.sleep(2)

driver.implicitly_wait(5)

# English Language
driver.find_element(By.ID, 'language').click()
driver.find_element(By.XPATH, '//*[@id="language-option"]/div[1]').click()
# driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[2]/div[1]/span").click()
# time.sleep(2)

driver.implicitly_wait(5)

# Get Started
driver.find_element(By.LINK_TEXT, 'Get Started').click()
# time.sleep(2)

driver.implicitly_wait(5)

# Provide full name
driver.find_element(By.NAME, 'fullName').send_keys('Golam Mourshid Antorr')

# provide date of birth -> day
driver.find_element(By.NAME, 'day').send_keys('1')

# provide date of birth -> month
driver.find_element(By.NAME, 'month').send_keys('1')

# provide date of birth -> year
driver.find_element(By.NAME, 'year').send_keys('2000')


# Provide Captcha
driver.find_element(By.NAME, 'captcha').send_keys('123456')

time.sleep(2)

driver.implicitly_wait(5)

# Continue Button
driver.find_element(By.ID, 'start').click()

time.sleep(2)

# Select Country Code
Select(driver.find_element(By.ID, 'country-select')).select_by_visible_text('Italy (IT)+39')

# Give Mobile Number
driver.find_element(By.NAME, 'mobile').send_keys('3279739401')

time.sleep(2)
driver.implicitly_wait(5)

# Send SMS Button
driver.find_element(By.ID, 'send-sms').click()

driver.implicitly_wait(15)
time.sleep(2)
# Give Verification Code
driver.find_element(By.NAME, 'verificationCode').send_keys('123456')
driver.implicitly_wait(15)
time.sleep(2)

# Continue Button
driver.find_element(By.ID, 'verify-mobile-code').click()

time.sleep(2)
# Give Username
driver.find_element(By.NAME, 'username').send_keys('31antor')

# Give Password
driver.find_element(By.NAME, 'password').send_keys('123456')

# Give Retype Password
driver.find_element(By.NAME, 'retypePassword').send_keys('123456')

time.sleep(2)

# Continue Button
driver.find_element(By.ID, 'create-account').click()

time.sleep(10)
print("Account Created Successfully!\n")




