from selenium import webdriver
from re import search
import time

PATH="E:/BIDOUILLE/Script/ClickBot/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(PATH)
# driver.maximize_window()
driver.get("https://store.obeygiant.com/collections/prints")
time.sleep(0.5)

# identify elements with tagname <a>
lnks=driver.find_elements_by_tag_name("a")

keyword="american-rage"

for lnk in lnks:
    # get_attribute() to get all href
    item=lnk.get_attribute('href')
    print(item)
    if search(keyword, item):
        print("link found")
        time.sleep(0.5)
        driver.get(item)
        item.click()
