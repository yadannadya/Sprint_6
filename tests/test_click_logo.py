import allure
import pytest
from pages.main_page import MainPageScooter
import curl




class TestHeader:

  
    @allure.title('Логотип Самокат открывает главную страницу')
    def test_check_transit_on_logo_scooter_for_main_page(self, driver): 

        main = MainPageScooter(driver)
        main.click_logo_scooter()
        assert main.get_url_page() == curl.main_page

    @allure.title('Логотип Яндекс открывает страницу Дзен')   
    def test_check_transit_on_logo_yandex_for_dzen(self, driver): 
        
        main = MainPageScooter(driver)
        main.click_logo_yandex()
        assert main.get_window_page(curl.dzen_url)

