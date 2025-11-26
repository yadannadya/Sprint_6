from selenium import webdriver
from pages.base_page import BasePage
import allure
from locators.locators import MainLocators, OrderPageLocators
import pytest


class OrderPageScooter(BasePage):
        
    @allure.step('Клик на кнопку заказать')
    def click_button_order(self, locator):
        self.scroll_for_element(locator)
        self.click_on_element(locator)

    @allure.step('Заполнить поля личной информации о человеке')
    def set_info_people(self, person):
        self.send_keys_to_input(OrderPageLocators.name_input, person.name)
        self.send_keys_to_input(OrderPageLocators.surname_input, person.surname)
        self.send_keys_to_input(OrderPageLocators.adress_input, person.adress)
        self.send_keys_to_input(OrderPageLocators.metro_input, person.metro)
        self.click_on_element(OrderPageLocators.metro_select)
        self.send_keys_to_input(OrderPageLocators.number_input, person.number)
        self.click_on_element(OrderPageLocators.button_next)

    @allure.step('Заполнить поля информации о заказе')
    def set_info_order(self, person):
        self.send_keys_to_input(OrderPageLocators.date_rent, person.date)
        self.click_on_element(OrderPageLocators.date_select)
        self.click_on_element(OrderPageLocators.rent_input)
        self.click_on_element(OrderPageLocators.rent_day)
        self.click_on_element(OrderPageLocators.black_scooter)
        self.click_on_element(OrderPageLocators.button_order)

    @allure.step('Подтвердить заказ в всплывающем окне')
    def click_button_yes(self):
        self.click_on_element(OrderPageLocators.button_yes)

    @allure.step('Проверить появление окна об успешном заказе')
    def check_window_order(self):
        return self.wait_for_element(OrderPageLocators.window_order)
