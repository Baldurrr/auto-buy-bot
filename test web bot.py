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

cookies=[
{
    "domain": ".amazon.fr",
    "expirationDate": 1638817744.848753,
    "hostOnly": false,
    "httpOnly": true,
    "name": "at-acbfr",
    "path": "/",
    "sameSite": "unspecified",
    "secure": true,
    "session": false,
    "storeId": "0",
    "value": "Atza|IwEBIPbTwMYVndMrGw_BCusgeeqH-UHPb9qF5D5HMSg9QfYK-9Vhd6Am-I5dmlp7iIVrIXvk7X4eJGLRdcU7yfFrJQkcFgCbhAfWkgr-3CspXoiPxSFKtoZQVv1by8mlJw7d6cIjfox9_gnJcZG1v6lAkMcRatqQUIZoqA0TpfYHXOUyJCZSTAWcA6VcPNV8Oaz8KvMn-xentnYTgcfQDHhiV7vV",
    "isProtected": true,
    "id": 1
},
{
    "domain": ".amazon.fr",
    "expirationDate": 1645377959.585501,
    "hostOnly": false,
    "httpOnly": false,
    "name": "i18n-prefs",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "EUR",
    "isProtected": true,
    "id": 2
},
{
    "domain": ".amazon.fr",
    "expirationDate": 2082787190.619688,
    "hostOnly": false,
    "httpOnly": false,
    "name": "lc-acbfr",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "fr_FR",
    "isProtected": true,
    "id": 3
},
{
    "domain": ".amazon.fr",
    "expirationDate": 1613843631,
    "hostOnly": false,
    "httpOnly": false,
    "name": "s_c27",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "548608",
    "id": 4
},
{
    "domain": ".amazon.fr",
    "hostOnly": false,
    "httpOnly": false,
    "name": "s_cc",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": true,
    "storeId": "0",
    "value": "true",
    "id": 5
},
{
    "domain": ".amazon.fr",
    "expirationDate": 1708449831,
    "hostOnly": false,
    "httpOnly": false,
    "name": "s_dslv",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "1613841831813",
    "isProtected": true,
    "id": 6
},
{
    "domain": ".amazon.fr",
    "expirationDate": 1613843631,
    "hostOnly": false,
    "httpOnly": false,
    "name": "s_dslv_s",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "Less%20than%207%20days",
    "id": 7
},
{
    "domain": ".amazon.fr",
    "expirationDate": 1613843631,
    "hostOnly": false,
    "httpOnly": false,
    "name": "s_invisit",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "true",
    "id": 8
},
{
    "domain": ".amazon.fr",
    "expirationDate": 2045841831,
    "hostOnly": false,
    "httpOnly": false,
    "name": "s_nr",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "1613841831812-Repeat",
    "isProtected": true,
    "id": 9
},
{
    "domain": ".amazon.fr",
    "hostOnly": false,
    "httpOnly": false,
    "name": "s_ppv",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": true,
    "storeId": "0",
    "value": "81",
    "id": 10
},
{
    "domain": ".amazon.fr",
    "hostOnly": false,
    "httpOnly": false,
    "name": "s_sq",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": true,
    "storeId": "0",
    "value": "%5B%5BB%5D%5D",
    "id": 11
},
{
    "domain": ".amazon.fr",
    "expirationDate": 2036998529,
    "hostOnly": false,
    "httpOnly": false,
    "name": "s_vnum",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "2036998529017%26vn%3D5",
    "isProtected": true,
    "id": 12
},
{
    "domain": ".amazon.fr",
    "expirationDate": 1638817744.848778,
    "hostOnly": false,
    "httpOnly": true,
    "name": "sess-at-acbfr",
    "path": "/",
    "sameSite": "unspecified",
    "secure": true,
    "session": false,
    "storeId": "0",
    "value": "\"BmrDAQneUvjg/bUdfQkb3dHTpHacdyNhYQL4kAgRmTo=\"",
    "isProtected": true,
    "id": 13
},
{
    "domain": ".amazon.fr",
    "expirationDate": 1645377959.585368,
    "hostOnly": false,
    "httpOnly": false,
    "name": "session-id",
    "path": "/",
    "sameSite": "unspecified",
    "secure": true,
    "session": false,
    "storeId": "0",
    "value": "258-4985876-2557963",
    "isProtected": true,
    "id": 14
},
{
    "domain": ".amazon.fr",
    "expirationDate": 1645377959.585412,
    "hostOnly": false,
    "httpOnly": false,
    "name": "session-id-time",
    "path": "/",
    "sameSite": "unspecified",
    "secure": true,
    "session": false,
    "storeId": "0",
    "value": "2082787201l",
    "isProtected": true,
    "id": 15
},
{
    "domain": ".amazon.fr",
    "expirationDate": 1645377959.585457,
    "hostOnly": false,
    "httpOnly": false,
    "name": "session-token",
    "path": "/",
    "sameSite": "unspecified",
    "secure": true,
    "session": false,
    "storeId": "0",
    "value": "\"4WXbZgxCDoYYkXgmBgw72F0c+T4KxZ6LyQTCOFlZKITty906qggEwT6smS+LFmKj1ph+VAhtudj7fYnZ+k7aV2RlmkwpXkbb0wR+mePFZnIS456od5MJ7kH1L7k3LEQQhE15M52eKyYPKcNCyPD+p8b4xOqTSinCmOsyFB4Q7LWNexzU82epEcNB7x7/WrZN2upDJJJa/Ef0+wotMNKL4Pb2n/4A4nVemY2SgzgkSD1EHe49SjiFMnUL7b2qHNyu+mouVwhtaPHcbcXSM4ZW/Q==\"",
    "isProtected": true,
    "id": 16
},
{
    "domain": ".amazon.fr",
    "expirationDate": 1638817744.8488,
    "hostOnly": false,
    "httpOnly": true,
    "name": "sst-acbfr",
    "path": "/",
    "sameSite": "unspecified",
    "secure": true,
    "session": false,
    "storeId": "0",
    "value": "Sst1|PQFbe0YyW9_VIl8kaSK8EWxxCZ8bvlJCbyv4k0Prnv8AKWChZGCLNTh0QDHOQWzvgoFX6bidZujgrErC9YMn_O74C4r0eKfEIem7VjbaOe7sfRQKlvxiZDnERmwvvpqEpeCH6FNDMtEn_j17m0ySHJrHZNopfb1gUOpEyYYvMGgkoWq5-X3nfh-M_roIrhkuA8oC82wbCAewlGfKz7uXnJ3mEOLFVXqc7Hg6lPmmgLffGPe2v3KJuzC2Fb2sUyJZaYwWlkPNY9AvOoQHjpdi1qlHdjm-mtvb2mwD-2ixJq2zmzA",
    "isProtected": true,
    "id": 17
},
{
    "domain": ".amazon.fr",
    "expirationDate": 1645377959.585435,
    "hostOnly": false,
    "httpOnly": false,
    "name": "ubid-acbfr",
    "path": "/",
    "sameSite": "unspecified",
    "secure": true,
    "session": false,
    "storeId": "0",
    "value": "262-4927989-7676469",
    "isProtected": true,
    "id": 18
},
{
    "domain": ".amazon.fr",
    "expirationDate": 1645377959.58548,
    "hostOnly": false,
    "httpOnly": false,
    "name": "x-acbfr",
    "path": "/",
    "sameSite": "unspecified",
    "secure": true,
    "session": false,
    "storeId": "0",
    "value": "\"bOq24XLF4dugKfFADZeRoBLEBwHKhxI8yfk0gIpHO9PbIGCfmcWqiICgBaX@M81k\"",
    "isProtected": true,
    "id": 19
},
{
    "domain": ".www.amazon.fr",
    "expirationDate": 1618430132,
    "hostOnly": false,
    "httpOnly": false,
    "name": "csd-key",
    "path": "/",
    "sameSite": "unspecified",
    "secure": true,
    "session": false,
    "storeId": "0",
    "value": "eyJ3YXNtVGVzdGVkIjp0cnVlLCJ3YXNtQ29tcGF0aWJsZSI6dHJ1ZSwid2ViQ3J5cHRvVGVzdGVkIjpmYWxzZSwidiI6MSwia2lkIjoiYTExMTQxIiwia2V5IjoiaTZyUEhua2NhUEV2c0ladkxzOFlmVGVDWiszcnd3V2E4aXVxNlZjWXJDV09wRjQ4aFdKOEgvLzN0TDBOZGxBN1lzQjd2a1JDS1V1TWI3enN4ZVFjK0pJZmh2c2ZHQURpZi81SWZmNndUNm1xbVBDeWtQdmNkUjh0a2hNVzZyUTB2VFVxaXpGOVMvQ0dWZzgvSVZJSUtyTnFuYldaQ0ZlUmJVMHZNQUFtVzZMWk5HN3RLeW1WeWFqT0Njc2M2dURPNi91OXNDVFBzYWpjM0dJZjNNOXhVb0c3MWI4ekdVZmlCWFNyYzBEM2xyRCsrZVlRT0ZxUmRSK3pkYjVZOE1KeklOaVJPdmlQdXRSSVJqUnNGRFZncFpYN3pUOFAyRUtIODM1VGh6RktrdlkzWjJQK1hNMlBIZFpxVG5qcXpCZStNSzJyVmFMQzl4WjZJMjBrbVAwNVZnPT0ifQ==",
    "isProtected": true,
    "id": 20
},
{
    "domain": "www.amazon.fr",
    "expirationDate": 1644081057,
    "hostOnly": true,
    "httpOnly": false,
    "name": "csm-hit",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "tb:s-V68NTXA74NWE8Z4Z4DM2|1613841056961&t:1613841057494&adb:adblk_yes",
    "isProtected": true,
    "id": 21
}
]