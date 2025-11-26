import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ожидание загрузки')
    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step('Скролл до элемента')
    def scroll_for_element(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Клик по элементу')
    def click_on_element(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        element.click()

    @allure.step('Ввод текста')
    def send_keys_to_input(self, locator, key, timeout=10):
        element = self.wait_for_element(locator, timeout)
        element.clear()
        element.send_keys(key)

    @allure.step('Получить текст элемента')
    def get_text_on_element(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        return element.text
            
    @allure.step('Получить ссылку страницы')
    def get_url_page(self):
        return self.driver.current_url
    
       
    @allure.step('Сменить вкладку')
    def get_window_page(self, url):
        self.driver.switch_to.window(self.driver.window_handles[-1])
        return WebDriverWait(self.driver, 10).until(EC.url_contains(url))

