import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH="E:/BIDOUILLE/Script/ClickBot/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(PATH)

#driver.get("https://google.com")


driver.get("https://www.amazon.fr/Synology-Serveur-Baies-DS-420-Disque/dp/B088V71WGH/ref=sr_1_1?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=1XMR3Y31L5AH4&dchild=1&keywords=ds420%2B&qid=1613835475&sprefix=ds420%2B%2Caps%2C156&sr=8-1")

#Cookies settings
# cookie = {‘name’ : ‘foo’, ‘value’ : ‘bar’}
# driver.add_cookie(cookie)

# And now output all the available cookies for the current URL
driver.get_cookies()

#1) Ajout article => add-to-cart-button
search = driver.find_element_by_id("add-to-cart-button")
search.click()

time.sleep(3)

#2)skip annonce => siNoCoverage-announce
search = driver.find_element_by_id("siNoCoverage-announce")
search.click()

time.sleep(3)

#3)passer commande => hlb-ptc-btn-native
search = driver.find_element_by_id("hlb-ptc-btn-native")
search.click()

time.sleep(3)

#4) submitOrderButtonId
# search = driver.find_element_by_id("")
# search.click()

