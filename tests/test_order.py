import allure
import pytest
import data
from pages.order_page import OrderPageScooter
from locators.locators import MainLocators

class TestPageOrder:

  
    @allure.title('Успешный заказ самоката')
    @pytest.mark.parametrize('locator',  [MainLocators.button_order_header, MainLocators.button_order_second])
    def test_check_order(self, driver, locator): 
                
        order = OrderPageScooter(driver)
        order.click_button_order(locator)
        order.set_info_people(data.person)
        order.set_info_order(data.person)
        order.click_button_yes()
        assert order.check_window_order()


