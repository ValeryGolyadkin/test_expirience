from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

browser = webdriver.Edge()
browser.implicitly_wait(10)
browser.get('https://magento.softwaretestingboard.com/women/tops-women/tees-women.html')

first_girl = browser.find_element(By.XPATH, "/html/body/div[2]/main/div[3]/div[1]/div[4]/ol/li[1]/div/div/strong/a")
print(first_girl.id)
print(first_girl.text)
print(first_girl.get_attribute('href'))
sorter = browser.find_element(By.ID, 'sorter')
select = Select(sorter)
select.select_by_value('price')
sleep(5)
first_girl = browser.find_element(By.XPATH, "/html/body/div[2]/main/div[3]/div[1]/div[4]/ol/li[1]/div/div/strong/a")
print(first_girl.text)
print(first_girl.get_attribute('href'))
