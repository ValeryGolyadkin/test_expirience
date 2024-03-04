from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep  # использовать только в крайнем случае

browser = webdriver.Edge()
# implicitly_wait - неявное ожидание
# implicitly_wait будет пытаться пропихнуть тест все время пока ждет
browser.implicitly_wait(10)
browser.get('https://magento.softwaretestingboard.com/women/tops-women/tees-women.html')
# WebDriverWait - явное ожидание
# WebDriverWait ждет пока прогрузится строка, если не прогрузится он все дропнет
WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element(
    (By.CLASS_NAME, 'not-logged-in'), 'Click “Write for us” link in the footer to submit a guest post'))

girls = browser.find_elements(By.XPATH, "//a[@class='product-item-link']")  # сократил XPATH
first_girl = girls[0]
print(first_girl.id)
print(first_girl.text)
print(first_girl.get_attribute('href'))
sorter = browser.find_element(By.ID, 'sorter')
select = Select(sorter)
select.select_by_value('price')
# пока не пропадет first_girl
WebDriverWait(browser, 10).until(EC.staleness_of(first_girl))
girls = browser.find_elements(By.XPATH, "//a[@class='product-item-link']")
first_girl = girls[0]
sleep(0.5)
print(first_girl.text)
print(first_girl.get_attribute('href'))
