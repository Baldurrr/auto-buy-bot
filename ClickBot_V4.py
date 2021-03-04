# -*- coding: utf-8 -*-
import time
import json
import os
import time
from re import search
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

PATH="E:/BIDOUILLE/Script/ClickBot/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(PATH)

def keywords_researcher(keyword_list):

    href_list=[]
    print("Keywords researcher function")
    # lnks=driver.find_elements_by_tag_name("a")
    lnks=driver.find_elements_by_tag_name("a")

    for lnk in lnks:
        # print(lnk)
        item=lnk.get_attribute('href')
        print(item)
        word_counter=0

        for word in keyword_list:
            if search(word, item):
                print("+1")
                word_counter=word_counter+1

        if (word_counter > 0 and word_counter == len(keyword_list)) or (word_counter >= len(keyword_list)/2):
            print("link found")
            href_list.append(str(item))
            time.sleep(1)
            break
    print("href : "+href_list[0])
    time.sleep(0.5)
    return href_list

def cookies_extraction(cookies_file,url):

    driver.get(url) 
    time.sleep(0.5)
    with open(cookies_file) as mycookiesfile:
        for line in mycookiesfile:
            line=str(line)
            cookie_line=json.loads(line)
            driver.add_cookie(cookie_line)
    
    mycookiesfile.close()
    driver.refresh()
    print("LOGED IN")

# def Amazon_casual():
#     pass

def ObeyGiant_limited():
    time.sleep(0.5)
    #1) Ajout article 
    search = driver.find_element_by_id("AddToCartText")
    search.click()
    time.sleep(0.5)

    #2)passer commande 
    search = driver.find_element_by_name("checkout")
    search.click()
    time.sleep(0.5)

    # #3)Info paiment 
    # #Passage au infos personnels
    # search = driver.find_element_by_id("continue_button")
    # search.click()
    # time.sleep(0.5)

    # #Passage aux Méthodes paiments
    # search = driver.find_element_by_id("continue_button")
    # search.click()
    # time.sleep(0.5)

    #Complete order
    #search = driver.find_element_by_id("continue_button")
    #search.click()
    #FIN

if __name__ == '__main__':

    menu = str(input(
        """
        1- Obey Giant limited mode  'tapez 1'
        """))
        
    if menu == '1' :
        cookies_file="E:/BIDOUILLE/Script/ClickBot/MyCookies/cookies_obey2.txt"
        print("\nObey Giant limited mode selected")
        keyword=input("Set the most potential word to be retrieve: (separated by spaces) \n=>")
        # keyword="american rage"
        keyword_list=keyword.split(" ")
        print("Keywords list: ")
        print(keyword_list)

        MyInputTime=input("Set the programmation of the script: (ex: 12:00:00)")
        ItsNotTime= True
        while ItsNotTime:
            Now=datetime.now()
            timing = Now.strftime("%H:%M:%S")
            time.sleep(1)
            print(timing)
            if timing == MyInputTime:
                print("Its time to go")
                ItsNotTime=False

                url="https://store.obeygiant.com/"
                cookies_extraction(cookies_file,url)
                time.sleep(1)
                href_list=keywords_researcher(keyword_list)
                time.sleep(1)

        print("Lancement page item trouvé")
        time.sleep(0.5)
        print("je suis a la fin")
        driver.get(href_list[0])
        ObeyGiant_limited()

    if menu == '3' :
        print("\nAmazon mode selected")
        url="https://www.amazon.fr/"
        cookies_file="E:/BIDOUILLE/Script/ClickBot/MyCookies/cookies_amazon.txt"
        cookies_extraction(cookies_file,url)

    elif menu == '4' :
        print(" Bye Bye")