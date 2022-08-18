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

chrome.get('https://formy-project.herokuapp.com')

# selector By linktext
# chrome.find_element(By.LINK_TEXT, 'Autocomplete').click()

# selector By partial.linktext
chrome.find_element(By.PARTIAL_LINK_TEXT, 'Enabled').click()


sleep(20)


chrome.quit()

