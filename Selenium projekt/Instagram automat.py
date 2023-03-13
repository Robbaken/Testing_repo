from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

CHROME_DRIVER_PATH = "C:\DriverSelenium\chromedriver.exe"
LOGIN = "kamil_r_mlody"
PASSWORD = "ziomak6"

driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
driver.get("https://www.instagram.com/chefsteps/")
driver.implicitly_wait(5)
driver.maximize_window()

sleep(3)

cookie = driver.find_element(By.XPATH, value='/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]')
cookie.click()
enter_login = driver.find_element(By.NAME, value='username')
enter_login.send_keys(LOGIN)
enter_password = driver.find_element(By.NAME, value='password')
enter_password.send_keys(PASSWORD)
login_bottom = driver.find_element(By.CSS_SELECTOR, value='#loginForm > div > div:nth-child(3) > button > div')
sleep(5)
login_bottom.click()
sleep(5)
not_now_tag = driver.find_element(By.CLASS_NAME, value='_ac8f')
not_now_tag.click()
sleep(3)
followers = driver.find_element(By.XPATH, value='/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/ul/li[2]/a')
followers.click()
sleep(2)
action = ActionChains(driver)
# action.double_click(copy_buttom).perform()
# scroll_origin = driver.find_element(By.TAG_NAME, value='')
# action.scroll_from_origin(scroll_origin, 0, 200).perform()


