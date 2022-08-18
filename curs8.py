from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)
chrome.maximize_window()

# By.CSS_SELECTOR

chrome.get('https://www.sendspace.com/login.html')
sleep(10)
login_button = chrome.find_element(By.XPATH, "//input[text()='Log In']")

actions = ActionChains(chrome)
actions.move_to_element(login_button).perform()
login_button.click()

sleep(10)
chrome.quit()


# sleep(), implicit.wait, explicit.wait
# sleep opreste executia codului pt un anumit timp de secunde
# il folosim doar cand nu merge altcumva, sau sa ne jucati local, dupa le stergem
# ingreuneaza rularea testelor

# implicit wait - stabileste in tot proiectul/testul cate secunde sa caute selenium ca sa gaseasca un element pe pagina
# la inceputul testului
chrome.implicitly_wait(3)

# explicit wait - cel mai recomandat sa se foloseasca
login_button = chrome.find_element(By.XPATH, "//input[text()='Log In']")
login_button = WebDriverWait(chrome,10).until(EC.presence_of_element_located(By.XPATH, "//input[text()='Log In']"))
# doar la testele care pica fara sens