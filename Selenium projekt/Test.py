import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import re
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from datetime import date

# WebDriverWait(driver,30).until(
#     EC.visibility_of_element_located((By.XPATH, "//button[text()='Zamknij']"))

driver = webdriver.Chrome(executable_path="C:\DriverSelenium\chromedriver.exe")
driver.get("http://testautomationpractice.blogspot.com/")
driver.implicitly_wait(5)
driver.maximize_window()

sleep(3)

cookie_ok = driver.find_element(By.ID, value="cookieChoiceDismiss")
cookie_ok.click()
sleep(3)
# <input class="wikipedia-search-input" id="Wikipedia1_wikipedia-search-input" type="text">
sleep(3)
wiki_search = driver.find_element(By.ID, value="Wikipedia1_wikipedia-search-input")
wiki_search.send_keys("Test")
sleep(3)
wiki_buttom = driver.find_element(By.XPATH, value="//*[@id='Wikipedia1_wikipedia-search-form']/div/span[2]/span[2]/input")
wiki_buttom.click()

result = driver.find_element(By.XPATH, value="//*[@id='wikipedia-search-result-link']/a")
result.click()
sleep(3)

driver.switch_to.window(driver.window_handles[1])
driver.get("https://en.wikipedia.org/wiki/Test")
# sleep(5)

driver.close()
# sleep(5)

driver.switch_to.window(driver.window_handles[0])

click_me = driver.find_element(By.XPATH, value="//*[@id='HTML9']/div[1]/button")
click_me.click()

sleep(3)

WebDriverWait(driver, 5).until(EC.alert_is_present())
alert = Alert(driver)
alert.dismiss()
sleep(3)
today = date.today()
d1 = today.strftime("%d/%m/%Y")

date_piker = driver.find_element(By.ID, value="datepicker")
date_piker.send_keys(d1)
date_piker.send_keys(Keys.ENTER)
sleep(3)
speed = driver.find_element(By.ID, value="speed")
speed.click()
for i in range(4):
    speed.send_keys(Keys.DOWN)
speed.send_keys(Keys.ENTER)
sleep(3)

text_label = driver.find_element(By.XPATH, value="//*[@id='Text1']/div[1]/div[3]/span")
if text_label.text == "Message **** 1234":
     print("Tekst się zgadza")
else:
    print("Tu jest inny tekst")

sleep(3)
copy_buttom = driver.find_element(By.XPATH, value="//*[@id='HTML10']/div[1]/button")
action = ActionChains(driver)
# double click operation
action.double_click(copy_buttom).perform()
sleep(3)

action = ActionChains(driver)
target = driver.find_element(By.XPATH, value="//*[@id='draggable']/p")
drop_point = driver.find_element(By.XPATH, value="//*[@id='droppable']")
action.drag_and_drop(target, drop_point).perform()

action = ActionChains(driver)
image1 = driver.find_element(By.XPATH, value="//*[@id='gallery']/li[1]/img")
image2 = driver.find_element(By.XPATH, value="//*[@id='gallery']/li[2]/img")
trash = driver.find_element(By.XPATH, value="//*[@id='trash']")
action.drag_and_drop(image1, trash).perform()
sleep(5)
action.drag_and_drop(image2, trash).perform()
sleep(3)

recycle1 = driver.find_element(By.CSS_SELECTOR, value="#trash > ul > li:nth-child(1) > a")
recycle1.click()
sleep(3)
slider = driver.find_element(By.CSS_SELECTOR, value="#slider > span")
move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(333, 0).release().perform()
sleep(3)

action = ActionChains(driver)
slider2 = driver.find_element(By.CSS_SELECTOR, value="#resizable > div.ui-resizable-handle.ui-resizable-se.ui-icon.ui-icon-gripsmall-diagonal-se")
action.click_and_hold(slider2).move_by_offset(80, 80).release().perform()

sleep(3)
# WebDriverWait(driver,30).until(
#     EC.visibility_of_element_located((By.XPATH, "//button[text()='Zamknij']"))

# ActionChains(driver) \
#     .key_down(Keys.CONTROL) \
#     .send_keys("w") \
#     .key_up(Keys.CONTROL) \
#     .perform()


"""Test Interia"""
# driver.get("https://www.interia.pl/")
# driver.implicitly_wait(5)
#
#
# driver.maximize_window()
#
# rodo_buttom = driver.find_element(By.XPATH, value="//button[text()='Przejdź do serwisu']")
# rodo_buttom.click()
#
# mail_enter = driver.find_element(By.XPATH, value='//*[@title="Poczta"]')
# mail_enter.click()
#
# email_input = driver. find_element(By.ID, value="email")
# email_input.send_keys("kamil.robak93@interia.pl")
#
# password_input = driver. find_element(By.ID, value="password")
# password_input.send_keys("ziomak6")
#
# checkbox_label = driver.find_element(By.CLASS_NAME, value="checkbox-label")
# checkbox_label.click()
#
# login_battom = driver.find_element(By.XPATH, value="//button[text()='Zaloguj się']")
# login_battom.click()
#
# new_mail = driver.find_element(By.XPATH, value="//span[@class='icon icon-new-message']")
# new_mail.click()
#
# sender_input_mail = driver.find_element(By.CSS_SELECTOR, value="input[ng-model='inputEmail']")
# sender_input_mail.send_keys("weglarzsylwia97@gmail.com")
#
# sleep(5)
#
# topic = driver.find_element(By.XPATH, value="//*[@id='subject']")
# topic.send_keys("Dla kochanej Sylwiuni Testy Automatyczne")
#
# driver.switch_to.frame(driver.find_element(By.ID, value="uiTinymce0_ifr"))
# ## Insert text via xpath ##
# elem = driver.find_element(By.XPATH, value="//*[@id='tinymce']")
# elem.send_keys("Tutaj CV")
# ## Switch back to the "default content" (that is, out of the iframes) ##
# driver.switch_to.default_content()
#
#
# upload_doc = driver.find_element(By.XPATH, value="//div[@id='wrapper']/div[3]/div/div/div/div[2]/div/div[2]/div[5]/input")
# upload_doc.send_keys("C:\\Users\\LENOVO\\Desktop\\CV_Kamil_Robak.pdf")
#
# sleep(5)
#
# driver.close()
#
# # send_buttom = driver.find_element(By.XPATH, value="//*[@id='wrapper']/div[3]/div/div/div/div[2]/div/div[2]/div[8]/button")
# # send_buttom.click()
# # send_buttom.click()

"""Testowanie strony twittera"""

# def hashtags(text):
#     pattern = "#(\w+)"
#     return re.findall(pattern, text)
#
# driver.get("https://twitter.com/hashtag/python")
#
# post_loaded = expected_conditions.presence_of_element_located((By.TAG_NAME, 'article'))
# WebDriverWait(driver, 15).until(post_loaded)
#
# list_hashtags = []
# for post in driver.find_elements_by_tag_name('article'):
#     try:
#         list_hashtags += hashtags(
#               post.find_element_by_css_selector('[lang="pl"]').text
#             )
#     except NoSuchElementException:
#         continue
#
# counter = {}
# for i in list_hashtags:
#     if i not in counter:
#         counter[i] = 0
#
#     counter[i] += 1
#
# print(counter)
# driver.close()

"""DO strony Anime zone rejestracja"""
# driver.get("https://www.animezone.pl/user/register")

# driver.implicitly_wait(5)
#
# login_input = driver.find_element_by_id("inputLogin")
# email_input = driver.find_element_by_id("inputEmail")
#
# login_input.send_keys("Kamil")
# sleep(5)
#
# email_input.send_keys("mmm@ggg.pl")
# sleep(5)
#
# birth_date = driver.find_element_by_name("user[birthdate]")
# birth_date.send_keys("19.02.1993")
#
# sleep(5)
# combo_gender = driver.find_element_by_name("user[gender]")
# combo_gender.click()
# combo_gender.send_keys(Keys.DOWN)
# combo_gender.send_keys(Keys.ENTER)
#
# sleep(5)
#
# combo_theme = driver.find_element_by_name("user[theme]")
# combo_theme.click()
# combo_theme.send_keys(Keys.DOWN)
# combo_theme.send_keys(Keys.ENTER)
#
# sleep(5)
# driver.implicitly_wait(5)
#
# checkbox_reg = driver.find_element_by_name("terms")
# checkbox_reg.click()
#
# WebDriverWait(driver,30).until(
#     EC.visibility_of_element_located((By.XPATH, "//button[text()='Zamknij']"))
# )
#
# send_buttom = driver.find_element_by_xpath("//button[@type='submit']")
# send_buttom.click()



