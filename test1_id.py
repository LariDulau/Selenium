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
# sleep(20) # nu e folosesc, nu se recomanda (implicit wait, explicit wait - asteapta dupa anumite elemente)

# setam implicit wait in secunde
# selenium va cauta toate elementele, timp de x secunde inainte sa dea eroare
chrome.implicitly_wait(3)

# asa deschidem o pagina
chrome.get('https://formy-project.herokuapp.com/form')
first_name = chrome.find_element(By.ID, 'first-name')
first_name.send_keys('Lari')
first_name.clear()
first_name.send_keys('Andreea')
last_name = chrome.find_element(By.ID, 'last-name')
last_name.send_keys('Dulau')


sleep(20)

# asa se inchide driver-ul, trebuie sa punem tot timpu la finalu testelor - se recomanda
chrome.quit()
# daca punem chrome.close() - inchide tab-ul


