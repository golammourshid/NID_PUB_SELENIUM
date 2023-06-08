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
driver.implicitly_wait(5)
# driver.maximize_window()

file = open('bd_apply.csv', encoding='utf-8')
csvreader = csv.reader(file)

next(csvreader)
rows = []
for row in csvreader:
    rows.append(row)

time.sleep(2)

# Right menu
driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/div[3]/div[2]/i").click()
# time.sleep(2)

driver.implicitly_wait(5)

# English Language
driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[2]/div[1]/span").click()
# time.sleep(2)

driver.implicitly_wait(5)

# Login
driver.find_element(By.NAME, 'username').send_keys(rows[0][0])
driver.find_element(By.NAME, 'password').send_keys(rows[0][1])
# time.sleep(10)
driver.find_element(By.NAME, 'captcha').send_keys(rows[0][2])
time.sleep(2)
driver.find_element(By.LINK_TEXT, 'Login').click()
time.sleep(1)
driver.implicitly_wait(5)


# Edit Profile
driver.find_element(By.LINK_TEXT, 'Profile').click()
time.sleep(1)
driver.find_element(By.ID, 'edit').click()

time.sleep(1)
driver.implicitly_wait(5)

driver.find_element(By.NAME, 'nameBn').clear()
driver.find_element(By.NAME, 'nameBn').send_keys(rows[0][3])

Select(driver.find_element(By.NAME, 'gender')).select_by_visible_text(rows[0][4])

Select(driver.find_element(By.NAME, 'bloodGroup')).select_by_visible_text(rows[0][5])

driver.find_element(By.NAME, 'birthReg').clear()
driver.find_element(By.NAME, 'birthReg').send_keys(rows[0][6])

Select(driver.find_element(By.NAME, 'birthPlace')).select_by_visible_text(rows[0][7])

driver.find_element(By.NAME, 'fatherNameBn').clear()
driver.find_element(By.NAME, 'fatherNameBn').send_keys(rows[0][8])

driver.find_element(By.NAME, 'fatherNameEn').clear()
driver.find_element(By.NAME, 'fatherNameEn').send_keys(rows[0][9])

driver.find_element(By.NAME, 'motherNameBn').clear()
driver.find_element(By.NAME, 'motherNameBn').send_keys(rows[0][10])

driver.find_element(By.NAME, 'motherNameEn').clear()
driver.find_element(By.NAME, 'motherNameEn').send_keys(rows[0][11])

Select(driver.find_element(By.NAME, 'maritalStatus')).select_by_visible_text(rows[0][12])

driver.find_element(By.NAME, 'spouseName1').clear()
driver.find_element(By.NAME, 'spouseName1').send_keys(rows[0][13])

time.sleep(2)
driver.implicitly_wait(5)

# Now give value for identification information
Select(driver.find_element(By.XPATH, '/html/body/div/div[1]/div[5]/div[2]/select')).select_by_visible_text(rows[0][14])

driver.find_element(By.NAME, 'education').clear()
driver.find_element(By.NAME, 'education').send_keys(rows[0][15])

driver.find_element(By.NAME, 'occupation').clear()
driver.find_element(By.NAME, 'occupation').send_keys(rows[0][16])

driver.find_element(By.NAME, 'religion').send_keys(rows[0][17])

time.sleep(5)
driver.implicitly_wait(15)

# Now give value for address information
Select(driver.find_element(By.XPATH, '/html/body/div/div[1]/div[5]/div[2]/select')).select_by_visible_text(rows[0][18])

Select(driver.find_element(By.NAME, 'countryOfResidence')).select_by_visible_text(rows[0][19])

driver.find_element(By.ID, 'voter-area-present').click()
Select(driver.find_element(By.NAME, 'division')).select_by_visible_text(rows[0][20])
Select(driver.find_element(By.NAME, 'district')).select_by_visible_text(rows[0][21])
driver.implicitly_wait(25)

Select(driver.find_element(By.NAME, 'upozila')).select_by_visible_text(rows[0][22])
driver.implicitly_wait(25)

Select(driver.find_element(By.NAME, 'rmo')).select_by_visible_text(rows[0][23])
driver.implicitly_wait(25)
time.sleep(2)
Select(driver.find_element(By.NAME, 'union')).select_by_visible_text(rows[0][24])
driver.implicitly_wait(25)

Select(driver.find_element(By.NAME, 'area')).select_by_visible_text(rows[0][25])
Select(driver.find_element(By.NAME, 'village')).select_by_visible_text(rows[0][26])
driver.find_element(By.NAME, 'house').send_keys(rows[0][27])
Select(driver.find_element(By.NAME, 'voterArea')).select_by_visible_text(rows[0][28])
time.sleep(2)
driver.implicitly_wait(5)

Select(driver.find_element(By.NAME, 'perDivision')).select_by_visible_text(rows[0][29])
Select(driver.find_element(By.NAME, 'perDistrict')).select_by_visible_text(rows[0][30])
Select(driver.find_element(By.NAME, 'perUpozila')).select_by_visible_text(rows[0][31])
Select(driver.find_element(By.NAME, 'perRmo')).select_by_visible_text(rows[0][32])
Select(driver.find_element(By.NAME, 'perUnion')).select_by_visible_text(rows[0][33])
Select(driver.find_element(By.NAME, 'perArea')).select_by_visible_text(rows[0][34])
driver.find_element(By.NAME, 'perAreaOther').send_keys(rows[0][35])
Select(driver.find_element(By.NAME, 'perVillage')).select_by_visible_text(rows[0][36])
driver.find_element(By.NAME, 'perVillageOther').send_keys(rows[0][37])
driver.find_element(By.NAME, 'perHouse').send_keys(rows[0][38])
time.sleep(5)
driver.implicitly_wait(5)


# Scroll up for finding next button
element = driver.find_element(By.ID, 'next-document')
driver.execute_script("arguments[0].scrollIntoView();", element)
driver.execute_script("arguments[0].click();", element)
# driver.find_element(By.XPATH, '/html/body/div/div[1]/div[4]/div/div[2]/a[2]/div').click()
time.sleep(1)
driver.find_element(By.ID, 'next-confirm').click()
time.sleep(1)
driver.find_element(By.ID, 'update').click()

time.sleep(2000)
