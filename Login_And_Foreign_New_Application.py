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

file = open('foreign_apply.csv', encoding='utf-8')
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
time.sleep(5)
# Father's information
if driver.find_element(By.NAME, 'fatherDead').is_selected():
    print("CHECKED!")
    driver.find_element(By.XPATH, '//*[@id="form"]/div[3]/div/div[2]/div/div[1]/label').click()
driver.find_element(By.XPATH, '//*[@id="form"]/div[3]/div/div[2]/div/div[1]/label').click()
time.sleep(2)
driver.find_element(By.NAME, 'fatherNameBn').clear()
driver.find_element(By.NAME, 'fatherNameBn').send_keys(rows[0][8])

driver.find_element(By.NAME, 'fatherNameEn').clear()
driver.find_element(By.NAME, 'fatherNameEn').send_keys(rows[0][9])

driver.find_element(By.NAME, 'fatherNid').clear()
driver.find_element(By.NAME, 'fatherNid').send_keys(rows[0][46])

driver.find_element(By.NAME, 'fatherVoterNumber').clear()
driver.find_element(By.NAME, 'fatherVoterNumber').send_keys(rows[0][47])

driver.find_element(By.NAME, 'fatherDeathDate').clear()
driver.find_element(By.NAME, 'fatherDeathDate').send_keys(rows[0][48])
time.sleep(3)

# Mother's Information
if driver.find_element(By.NAME, 'motherDead').is_selected():
    print("CHECKED!")
    driver.find_element(By.XPATH, '//*[@id="form"]/div[3]/div/div[3]/div/div[1]/label').click()
driver.find_element(By.XPATH, '//*[@id="form"]/div[3]/div/div[3]/div/div[1]/label').click()

driver.find_element(By.NAME, 'motherNameBn').clear()
driver.find_element(By.NAME, 'motherNameBn').send_keys(rows[0][10])

driver.find_element(By.NAME, 'motherNameEn').clear()
driver.find_element(By.NAME, 'motherNameEn').send_keys(rows[0][11])

driver.find_element(By.NAME, 'motherNid').clear()
driver.find_element(By.NAME, 'motherNid').send_keys(rows[0][49])

driver.find_element(By.NAME, 'motherVoterNumber').clear()
driver.find_element(By.NAME, 'motherVoterNumber').send_keys(rows[0][50])

driver.find_element(By.NAME, 'motherDeathDate').clear()
driver.find_element(By.NAME, 'motherDeathDate').send_keys(rows[0][51])
time.sleep(3)

# Elder Brother/Sister's Information
driver.find_element(By.NAME, 'siblingName').clear()
driver.find_element(By.NAME, 'siblingName').send_keys(rows[0][52])

driver.find_element(By.NAME, 'siblingNid').clear()
driver.find_element(By.NAME, 'siblingNid').send_keys(rows[0][53])
time.sleep(2)

# Spouse's Information
Select(driver.find_element(By.NAME, 'maritalStatus')).select_by_visible_text(rows[0][12])

driver.find_element(By.NAME, 'spouseName1').clear()
driver.find_element(By.NAME, 'spouseName1').send_keys(rows[0][13])

driver.find_element(By.NAME, 'spouseNid1').clear()
driver.find_element(By.NAME, 'spouseNid1').send_keys(rows[0][54])

driver.find_element(By.NAME, 'spouseDeathDate1').clear()
driver.find_element(By.NAME, 'spouseDeathDate1').send_keys(rows[0][55])

driver.find_element(By.NAME, 'spouseName2').clear()
driver.find_element(By.NAME, 'spouseName2').send_keys(rows[0][56])

driver.find_element(By.NAME, 'spouseNid2').clear()
driver.find_element(By.NAME, 'spouseNid2').send_keys(rows[0][57])

driver.find_element(By.NAME, 'spouseDeathDate2').clear()
driver.find_element(By.NAME, 'spouseDeathDate2').send_keys(rows[0][58])

driver.find_element(By.NAME, 'spouseName3').clear()
driver.find_element(By.NAME, 'spouseName3').send_keys(rows[0][59])

driver.find_element(By.NAME, 'spouseNid3').clear()
driver.find_element(By.NAME, 'spouseNid3').send_keys(rows[0][60])

driver.find_element(By.NAME, 'spouseDeathDate3').clear()
driver.find_element(By.NAME, 'spouseDeathDate3').send_keys(rows[0][61])

driver.find_element(By.NAME, 'spouseName4').clear()
driver.find_element(By.NAME, 'spouseName4').send_keys(rows[0][62])

driver.find_element(By.NAME, 'spouseNid4').clear()
driver.find_element(By.NAME, 'spouseNid4').send_keys(rows[0][63])

driver.find_element(By.NAME, 'spouseDeathDate4').clear()
driver.find_element(By.NAME, 'spouseDeathDate4').send_keys(rows[0][64])
time.sleep(3)

driver.implicitly_wait(5)

# Now give value for identification information
Select(driver.find_element(By.XPATH, '/html/body/div/div[1]/div[5]/div[2]/select')).select_by_visible_text(rows[0][14])

driver.find_element(By.NAME, 'education').clear()
driver.find_element(By.NAME, 'education').send_keys(rows[0][15])

driver.find_element(By.NAME, 'occupation').clear()
driver.find_element(By.NAME, 'occupation').send_keys(rows[0][16])

Select(driver.find_element(By.NAME, 'disability')).select_by_visible_text(rows[0][65])

driver.find_element(By.NAME, 'identificationMark').clear()
driver.find_element(By.NAME, 'identificationMark').send_keys(rows[0][66])

driver.find_element(By.NAME, 'tin').clear()
driver.find_element(By.NAME, 'tin').send_keys(rows[0][67])

driver.find_element(By.NAME, 'dl').clear()
driver.find_element(By.NAME, 'dl').send_keys(rows[0][68])

driver.find_element(By.NAME, 'passport').clear()
driver.find_element(By.NAME, 'passport').send_keys(rows[0][69])

driver.find_element(By.NAME, 'telephone').clear()
driver.find_element(By.NAME, 'telephone').send_keys(rows[0][70])

driver.find_element(By.NAME, 'religion').send_keys(rows[0][17])

time.sleep(2)
driver.implicitly_wait(15)

# Now give value for address information
Select(driver.find_element(By.XPATH, '/html/body/div/div[1]/div[5]/div[2]/select')).select_by_visible_text(rows[0][18])
try:
    driver.find_element(By.NAME, 'foreignCountry').clear()
except:
    pass
time.sleep(2)
Select(driver.find_element(By.NAME, 'countryOfResidence')).select_by_visible_text('Singapore')
Select(driver.find_element(By.NAME, 'countryOfResidence')).select_by_visible_text(rows[0][19])
time.sleep(2)
# Give foreign address info
driver.find_element(By.NAME, 'foreignProvince').clear()
driver.find_element(By.NAME, 'foreignProvince').send_keys(rows[0][39])
driver.find_element(By.NAME, 'foreignCity').clear()
driver.find_element(By.NAME, 'foreignCity').send_keys(rows[0][40])
driver.find_element(By.NAME, 'foreignHouse').clear()
driver.find_element(By.NAME, 'foreignHouse').send_keys(rows[0][41])
driver.find_element(By.NAME, 'foreignRoad').clear()
driver.find_element(By.NAME, 'foreignRoad').send_keys(rows[0][42])
driver.find_element(By.NAME, 'foreignZip').clear()
driver.find_element(By.NAME, 'foreignZip').send_keys(rows[0][43])
driver.find_element(By.NAME, 'foreignMobile').clear()
driver.find_element(By.NAME, 'foreignMobile').send_keys(rows[0][44])
driver.find_element(By.NAME, 'foreignEmail').clear()
driver.find_element(By.NAME, 'foreignEmail').send_keys(rows[0][45])
time.sleep(5)

# Select voter AT
if driver.find_element(By.NAME, 'voterAt').is_selected():
    print("CHECKED!")
    driver.find_element(By.XPATH, '//*[@id="form"]/div[5]/div/div[3]/div/div[2]/div[1]/label').click()
driver.find_element(By.XPATH, '//*[@id="form"]/div[5]/div/div[3]/div/div[2]/div[1]/label').click()
Select(driver.find_element(By.NAME, 'division')).select_by_visible_text(rows[0][20])
Select(driver.find_element(By.NAME, 'district')).select_by_visible_text(rows[0][21])
driver.implicitly_wait(25)

Select(driver.find_element(By.NAME, 'upozila')).select_by_visible_text(rows[0][22])
driver.implicitly_wait(25)
time.sleep(1)
Select(driver.find_element(By.NAME, 'rmo')).select_by_visible_text(rows[0][23])
driver.implicitly_wait(25)
time.sleep(1)
Select(driver.find_element(By.NAME, 'rmo')).select_by_visible_text("শহর")
time.sleep(1)
Select(driver.find_element(By.NAME, 'rmo')).select_by_visible_text(rows[0][23])
time.sleep(2)
Select(driver.find_element(By.NAME, 'union')).select_by_visible_text(rows[0][24])
driver.implicitly_wait(25)

Select(driver.find_element(By.NAME, 'area')).select_by_visible_text(rows[0][25])
driver.find_element(By.NAME, 'ward').clear()
driver.find_element(By.NAME, 'ward').send_keys('1')
Select(driver.find_element(By.NAME, 'village')).select_by_visible_text(rows[0][26])
driver.find_element(By.NAME, 'house').clear()
driver.find_element(By.NAME, 'house').send_keys(rows[0][27])
time.sleep(1)
driver.find_element(By.NAME, 'postOffice').clear()
driver.find_element(By.NAME, 'postOffice').send_keys(rows[0][71])
Select(driver.find_element(By.NAME, 'voterArea')).select_by_visible_text(rows[0][28])
time.sleep(5)
driver.implicitly_wait(5)

Select(driver.find_element(By.NAME, 'perDivision')).select_by_visible_text(rows[0][29])
Select(driver.find_element(By.NAME, 'perDistrict')).select_by_visible_text(rows[0][30])
Select(driver.find_element(By.NAME, 'perUpozila')).select_by_visible_text(rows[0][31])
driver.implicitly_wait(25)
time.sleep(1)
Select(driver.find_element(By.NAME, 'perRmo')).select_by_visible_text(rows[0][32])
time.sleep(1)
Select(driver.find_element(By.NAME, 'perRmo')).select_by_visible_text("শহর")
time.sleep(1)
Select(driver.find_element(By.NAME, 'perRmo')).select_by_visible_text(rows[0][32])
time.sleep(1)
Select(driver.find_element(By.NAME, 'perCity')).select_by_visible_text('ঢাকা উত্তর সিটি কর্পোরেশন')
time.sleep(2)
Select(driver.find_element(By.NAME, 'perUnion')).select_by_visible_text(rows[0][33])
time.sleep(1)
Select(driver.find_element(By.NAME, 'perArea')).select_by_visible_text(rows[0][34])
driver.find_element(By.NAME, 'perAreaOther').send_keys(rows[0][35])
driver.find_element(By.NAME, 'perWard').clear()
driver.find_element(By.NAME, 'perWard').send_keys('5')
Select(driver.find_element(By.NAME, 'perVillage')).select_by_visible_text(rows[0][36])
driver.find_element(By.NAME, 'perVillageOther').clear()
driver.find_element(By.NAME, 'perVillageOther').send_keys(rows[0][37])
driver.find_element(By.NAME, 'perHouse').clear()
driver.find_element(By.NAME, 'perHouse').send_keys(rows[0][38])

time.sleep(1)
driver.find_element(By.NAME, 'perPostOffice').clear()
driver.find_element(By.NAME, 'perPostOffice').send_keys('উত্তরা মডেল টাউন')
time.sleep(10)
driver.implicitly_wait(5)

# Scroll up for finding next button
element = driver.find_element(By.ID, 'next-document')
driver.execute_script("arguments[0].scrollIntoView();", element)
driver.execute_script("arguments[0].click();", element)
# driver.find_element(By.XPATH, '/html/body/div/div[1]/div[4]/div/div[2]/a[2]/div').click()
time.sleep(10)
driver.find_element(By.ID, 'next-confirm').click()
time.sleep(1)
driver.find_element(By.ID, 'update').click()
time.sleep(1)

# Download this form
driver.find_element(By.ID, 'download').click()

time.sleep(10)
