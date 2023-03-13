from bs4 import BeautifulSoup
import requests
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

url_doc = 'https://docs.google.com/forms/d/e/1FAIpQLSdS1ua1e644MAKx7QKAEna1tmv1iYtRsATxirDWevWiFPx_Ug/viewform?usp=sf_link'
url_zillow = 'https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.61529005957031%2C%22east%22%3A-122.25136794042969%2C%22south%22%3A37.6552491296774%2C%22north%22%3A37.89513918006007%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D'
cookies_goo = {
    "NID": "511=ktkACo_ZFBfZiD_DvYTKQFmYYX7R3Esh1ZtJ6A3F87KG_YzkbqlHc0NmQsGPyc78KIOXyCtVuYE9QmX-ixl-HzpbE9N9K67sGQCTZ2CFZ1oZAhe-iSFKtCcsUCsY8CHmbDu9YtxaEs7prgZqRID19DI6bqN2lxQZjog8HY6ur_M",
    "1P_JAR": "2021-11-05-13",
    "CONSENT": "YES+cb.20211102-08-p0.it+FX+548"
}

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36",
    "Accept-Language": "it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7"
}

CHROME_DRIVER_PATH = "C:\DriverSelenium\chromedriver.exe"

response = requests.get(url_zillow, headers=header, cookies=cookies_goo)
soup = BeautifulSoup(response.content, "lxml")
text = soup.prettify()
picture = soup.find_all(name="img", class_="Image-c11n-8-73-8__sc-1rtmhsc-0 emzIcX")
source_price = soup.find_all(name="div", class_="StyledPropertyCardDataArea-c11n-8-73-8__sc-yipmu-0 hRqIYX")
source_addresses = soup.find_all(name="a", class_="StyledPropertyCardDataArea-c11n-8-73-8__sc-yipmu-0 lhIXlm property-card-link")

links = []
prices = []
addresses = []
for i in picture:
    x = i.get("src")
    links.append(x)
for j in source_price:
    y = re.search('price">(.+?)</span>', str(source_price)).group(1)
    prices.append(y)
for k in source_addresses:
    z = re.search('"property-card-addr">(.+?)</address>', str(source_addresses)).group(1)
    addresses.append(z)


driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
driver.get(url_doc)
driver.implicitly_wait(5)
driver.maximize_window()
sleep(2)

for i in range(len(links)):
    input_address = driver.find_element(By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
    input_address.send_keys(addresses[i])
    sleep(2)
    input_price = driver.find_element(By.XPATH, value='/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    input_price.send_keys(prices[i])
    sleep(2)
    input_links = driver.find_element(By.XPATH, value='/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    input_links.send_keys(links[i])
    sleep(2)
    send_bottom = driver.find_element(By.XPATH, value='/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    send_bottom.click()
    sleep(2)
    send_another_answer = driver.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    send_another_answer.click()
    sleep(2)






