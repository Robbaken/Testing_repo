from selenium import webdriver

url_doc = 'https://docs.google.com/forms/d/e/1FAIpQLSdS1ua1e644MAKx7QKAEna1tmv1iYtRsATxirDWevWiFPx_Ug/viewform?usp=sf_link'
CHROME_DRIVER_PATH = "C:\DriverSelenium\chromedriver.exe"

driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
driver.get(url_doc)
driver.implicitly_wait(5)
driver.maximize_window()