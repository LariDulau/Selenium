from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# selenium merge pe toate brwoser-urile
# initializam un browser - tot timpu se scrie la fel
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

# sau fara variabila
# chrome = webdriver.Chrome(serice = Service(ChromeDriverManager().install())

chrome.maximize_window()

chrome.get('http://www.seleniumframework.com/Practiceform/')
chrome.find_element(By.NAME, 'country').send_keys('Romania')
chrome.find_element(By.NAME, 'company').send_keys('IT factory')


sleep(20)


chrome.quit()

