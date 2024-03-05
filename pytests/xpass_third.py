from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Edge()
browser.get('https://www.qa-practice.com/elements/input/simple')
browser.find_element(By.LINK_TEXT, 'Checkbox').click()
time.sleep(0.5)
# Находим элемент с помощью XPATH перед название атрибута ВСЕГДА стоит @
# Для поиска по неточному значению используется элемент contains пример: //li[contains(@class, "tab")]
# Для поиска по тексту //*[contains(text(), "button")] or //*[text()="Simple button"] *-весь файл
elem = browser.find_element(By.XPATH, '//li[@class="tab"][1]')
elem.click()
time.sleep(0.5)
# поиск любого элемента после известного:
three = browser.find_element(By.XPATH, '//label[@class=" form-label"]/following::input[@value="three"]')
three.click()
time.sleep(0.5)
# /child:: - поиск внутри родительского тега
# /descendant:: - поиск детей по всем род. тегам главного тега
# /following-sibling - поиск на том же уровне, где известный тег
# /ancestor:: поиск родительских тегов через [x] можно повышать поколения по старшинству
# /parent:: поиск отца
# /preceding:: поиск любого элемента до известного
# /
browser.quit()
