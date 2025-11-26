from selenium.webdriver.common.by import By



class MainLocators:

    button_order_header = [By.XPATH, ".//button[@class='Button_Button__ra12g']"]
    button_order_second = [By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"]

    logo_yandex = [By.CLASS_NAME, 'Header_LogoYandex__3TSOI']
    logo_scooter = [By.CLASS_NAME, 'Header_LogoScooter__3lsAR']


    @staticmethod
    def question(num):
        return By.ID, f"accordion__heading-{num}"
    
    @staticmethod
    def answer(num):
        return By.XPATH, f".//div[@id='accordion__panel-{num}']/p"
    

class OrderPageLocators:

    name_input = [By.XPATH, ".//input[@placeholder='* Имя']"]
    surname_input = [By.XPATH, ".//input[@placeholder='* Фамилия']"]
    adress_input = [By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']"]
    metro_input = [By.XPATH, ".//input[@placeholder='* Станция метро']"]
    metro_select = [By.CLASS_NAME, "select-search__select"] 
    number_input = [By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']"]
    button_next = [By.XPATH, ".//button[text()='Далее']"]

    date_rent = [By.XPATH, ".//input[@placeholder='* Когда привезти самокат']"]
    date_select = [By.XPATH, ".//div[@tabindex='0'][@role='button']"]
    rent_input = [By.XPATH, ".//div[text()='* Срок аренды']"]
    rent_day = [By.XPATH, ".//div[text()='сутки']"]
    black_scooter = [By.ID, "black"]
    button_order = [By.XPATH, ".//button[2][text()='Заказать']"]
    button_yes = [By.XPATH, ".//button[text()='Да']"]

    window_order = [By.XPATH, ".//div[text()='Заказ оформлен']"]

