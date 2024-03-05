import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Edge()
browser.get('https://www.qa-practice.com/elements/button/simple')
# CSS_SELECTOR работает с тэгами страницы div p li (если мы ищем именно стиль css работает через .tab)
# Так же он может управлять их атрибутами по названию: class, id, type ="...."
# Группировка элементов происходит через смешение тегов и атрибутов
element = browser.find_element(By.CSS_SELECTOR, 'li[class="tab"]' and ' .tab:nth-of-type(2)')
element.click()
time.sleep(0.5)
browser.find_element(By.LINK_TEXT, 'Inputs').click()
time.sleep(0.5)
# *= поиск элемента со схожим названием пример : [type*="idde"] от hidden.
# ^= поиск элемента со схожим началом пример : [type*="hidde"] от hidden.
# $= поиск элемента со схожим концом пример : [type*="idden"] от hidden.
# |= поиск элемента по первому слову атрибута : [type|="hidden"] от hidden-resolve.
# ~= поиск элемента по  слову атрибута : [type~="resolve"] от hidden resolve.
element = browser.find_element(By.CSS_SELECTOR, '[class~="requiredField"]')
element.click()
time.sleep(0.5)
# поиск элементов через родителя
# поиск родительского тэга -> тэг сына пример:form [method="post"] label
# поиск родительского тэга -> тэг сына только следующего уровня пример: form [method="post"]>input
# поиск смежного тэга  -> тэг следующий  пример: form [method="post"]~a
# если их несколько и нам нужен только следующий пример: form [method="post"]+a
element = browser.find_element(By.CSS_SELECTOR, 'form[method="post"] label ')
element.click()
time.sleep(0.5)
browser.quit()
