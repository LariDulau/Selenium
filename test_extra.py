from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

chrome.maximize_window()

# By.CSS_SELECTOR

chrome.get('https://www.sendspace.com/login.html')
# sleep(5) sa se incarce dar la mine merge

# tipul de element (a) si in [] atributul si valoarea
facebook = chrome.find_element(By.CSS_SELECTOR, 'a[title="log in with Facebook"]')
facebook.click()

# tipul de element a cu atributul title care contine* textul Facebook
facebook = chrome.find_element(By.CSS_SELECTOR, 'a[title*="Facebook"]')
facebook.click()

# tipul de element a cu atributul title care incepe^ textul Facebook
facebook = chrome.find_element(By.CSS_SELECTOR, 'a[title^="Facebook"]')
facebook.click()

# tipul de element a cu atributul title care se termina$ textul Facebook
facebook = chrome.find_element(By.CSS_SELECTOR, 'a[title$="Facebook"]')
facebook.click()

chrome.get('https://www.sendspace.com/login.html')
user = chrome.find_element(By.ID, 'loginusername')
# ID sub forma de CSS: # in fata, se rec ala simplu by id
# selector By CSS - ID
# user = chrome.find_element(By.CSS_SELECTOR, '#loginusername')
user.send_keys('trttt')


# selector By Xpath
user = chrome.find_element(By.XPATH, "//input[@id='loginusername']")
name = chrome.find_element(By.XPATH, "//input[@name='username']")
name = chrome.find_element(By.XPATH, "//*[@name='username']") # se pune * = orice tip de elem care atribut name=username
user = chrome.find_element(By.CSS_SELECTOR, "input[id='loginusername']")


# CLASS sub forma de CSS: . in fata si in spatiile libere sau scrii class
user = chrome.find_element(By. CLASS_NAME, 'fa fa-facebook')
# selector By CSS - Class
user = chrome.find_element(By. CSS_SELECTOR, '.fa.fa-facebook')
# selector By CSS - [atribut = valoare] [class = fafafacebook]
user = chrome.find_element(By. CSS_SELECTOR, "[class = 'fa fa-facebook']")


# copy - selector (titlu emag)

# CSS SELECTOR: #masthead > div > div > div.navbar-branding > a > img
# img[alt='eMAG'] asta nu e cu copy paste
# XPATH: //*[@id="masthead"]/div/div/div[1]/a/img

login_button = chrome.find_element(By.CSS_SELECTOR, "input[value='Log In']")
login_button.click()

# selector By CSS - css selector (unic si cat mai scurt)
login_button = chrome.find_element(By.CSS_SELECTOR, "div > div >  input")
login_button.click()

login_button = chrome.find_element(By.XPATH, "//div/div/input")
# // se pun la inceput si daca nu e parinte direct

# form[action="/login.html"] div.row > div > input
# "//input[@value='Log In']/parent::div/parent::div/following-sibling::div/preceding-sibling::div"

# By.XPATH

google_button = chrome.find_element(By.XPATH, 'div#openid_btns a:nth-child(3)')

sleep(10)
chrome.quit()