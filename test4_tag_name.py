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

chrome.get('https://formy-project.herokuapp.com/form' )
# introduce la primul input ce ii zic eu
chrome.find_element(By.TAG_NAME, 'input').send_keys('Lari')

# pt a introduce in al 3-lea input
# imi returneaza o lista cu elem ce le gaseste cu valoarea ce o dau eu (input)
lista_elemente_input = chrome.find_elements(By.TAG_NAME, 'input')
lista_elemente_input[2].send_keys('QA')


sleep(20)


chrome.quit()

