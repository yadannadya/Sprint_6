from selenium import webdriver
from pages.base_page import BasePage
import allure
from locators.locators import MainLocators


class MainPageScooter(BasePage):
    
    @allure.step('Клик на логотип Яндекс')
    def click_logo_yandex(self):
        self.click_on_element(MainLocators.logo_yandex)
    
    @allure.step('Клик на логотип Самокат')
    def click_logo_scooter(self):
        self.click_on_element(MainLocators.logo_scooter)  

    @allure.step('Открыть вопрос')
    def click_on_question(self, question):
        question_locator = MainLocators.question(question)
        self.scroll_for_element(question_locator)
        self.click_on_element(question_locator)

   
    @allure.step("Сравнить текст ответа")
    def check_text(self, answer, text):
        answer_locator = MainLocators.answer(answer)
        actual_text = self.get_text_on_element(answer_locator)
        return actual_text == text



