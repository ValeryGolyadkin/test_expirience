from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Создаем экземпляр драйвера Edge
browser = webdriver.Edge()

# Открываем страницу OpenAI
browser.get('https://openai.com')

# Открываем новую вкладку и переходим на страницу GitHub
browser.execute_script("window.open('https://www.qa-practice.com/elements/button/simple')")
# Ждем, пока не появится вторая вкладка
WebDriverWait(browser, 10).until(EC.number_of_windows_to_be(2))

# Закрываем текущую вкладку
browser.close()
# Переключаемся на первую вкладку
browser.switch_to.window(browser.window_handles[0])
time.sleep(0.5)
button_id = browser.find_element(By.ID, 'submit-id-submit')
button_id.click()
time.sleep(0.5)
# Находим элемент с помощью CSS-селектора
#element = browser.find_element(By.CSS_SELECTOR, '.tab:nth-of-type(2)'работает)
element = browser.find_element(By.CSS_SELECTOR, 'li[class="tab"]' and ' .tab:nth-of-type(2)')
element.click()
time.sleep(0.5)
# Находим элемент с помощью класса
button_class = browser.find_element(By.CLASS_NAME, "a-button")
button_class.click()
time.sleep(0.5)
# Находим элемент по тексту
browser.find_element(By.LINK_TEXT, 'Inputs').click()
time.sleep(0.5)
# Находим элемент с помощью XPATH
email = browser.find_element(By.XPATH, '//li[@class="tab"][1]')
email.click()
time.sleep(0.5)
# Закрываем браузер
browser.quit()