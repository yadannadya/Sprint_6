import allure
import pytest
import data
from pages.main_page import MainPageScooter



class TestMainQuestion:

    @allure.title('Ответ соответствует вопросу в разделе Вопросы')   
    @pytest.mark.parametrize('question, answer, text', data.text)
    def test_check_answer_to_question(self, driver, question, answer, text): 
                
        main = MainPageScooter(driver)
        main.click_on_question(question)
        assert main.check_text(answer, text)



