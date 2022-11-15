
from selenium import webdriver
from selenium.webdriver.chrome.options import Options #Setting up special options in order to not quit automatically
from selenium.webdriver.common.by import By #Importing by in order to work in brackets
import time #Importing time for pause
chrome_options = Options() #special options
chrome_options.add_experimental_option("detach", True) #special options

driver = webdriver.Chrome(options=chrome_options)

driver.get('edupage url') #Opening edupage

Searchloginname = driver.find_element(By.ID, "home_Login_1e1") #Finding element for login input
Searchloginname.send_keys("Username") #Login 

Searchloginpassword = driver.find_element(By.ID, "home_Login_1e2")# Finding element for password
Searchloginpassword.send_keys("Password")# Password

loginbutton = driver.find_element(By.CLASS_NAME,"skgdFormSubmit").click()# Finding element for login button and clicking
time.sleep(5)
obedbutton = driver.find_element(By.CLASS_NAME,"strava").click()#Finding element for lunch menu and clicking
time.sleep(5)
daslityzdenbutton = driver.find_element(By.CSS_SELECTOR,"#mainContainer > div:nth-child(1) > div > div:nth-child(2) > div > div > div:nth-child(3) > span").click()# Finding element for next week lunch menu and clicking
time.sleep(5)
Pondelok = driver.find_element(By.CSS_SELECTOR,"#mainContainer > div:nth-child(3) > div > table > tbody > tr:nth-child(1) > td:nth-child(3) > div > div > button").click()# Finding element for registering monday and clicking
time.sleep(5)
Utorok = driver.find_element(By.CSS_SELECTOR,"#mainContainer > div:nth-child(3) > div > table > tbody > tr:nth-child(2) > td:nth-child(3) > div > div > button").click()# Finding element for registering tuesday and clicking
time.sleep(5)
Streda = driver.find_element(By.CSS_SELECTOR,"#mainContainer > div:nth-child(3) > div > table > tbody > tr:nth-child(3) > td:nth-child(3) > div > div > button").click()# Finding element for registering wednesday and clicking
time.sleep(5)
Stvrtok = driver.find_element(By.CSS_SELECTOR,"#mainContainer > div:nth-child(3) > div > table > tbody > tr:nth-child(4) > td:nth-child(3) > div > div > button").click()# Finding element for registering thursady and clicking
time.sleep(5)
Piatok = driver.find_element(By.CSS_SELECTOR,"#mainContainer > div:nth-child(3) > div > table > tbody > tr:nth-child(5) > td:nth-child(3) > div > div > button").click()# Finding element for registering friday and clicking

