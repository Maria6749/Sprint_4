from pages.drop_down_menu_page import FAQLocators
from helps import FAQExpectedAnswers
import pytest
import allure
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


FAQ_DATA = [(FAQLocators.QUESTION_1, FAQExpectedAnswers.QUESTION_TEXT_1, FAQLocators.ANSWER_1, FAQExpectedAnswers.EXPECTED_ANSWER_1), (FAQLocators.QUESTION_2, FAQExpectedAnswers.QUESTION_TEXT_2, FAQLocators.ANSWER_2, FAQExpectedAnswers.EXPECTED_ANSWER_2),
            (FAQLocators.QUESTION_3, FAQExpectedAnswers.QUESTION_TEXT_3, FAQLocators.ANSWER_3, FAQExpectedAnswers.EXPECTED_ANSWER_3), (FAQLocators.QUESTION_4, FAQExpectedAnswers.QUESTION_TEXT_4, FAQLocators.ANSWER_4, FAQExpectedAnswers.EXPECTED_ANSWER_4),
            (FAQLocators.QUESTION_5, FAQExpectedAnswers.QUESTION_TEXT_5, FAQLocators.ANSWER_5, FAQExpectedAnswers.EXPECTED_ANSWER_5), (FAQLocators.QUESTION_6, FAQExpectedAnswers.QUESTION_TEXT_6, FAQLocators.ANSWER_6, FAQExpectedAnswers.EXPECTED_ANSWER_6),
            (FAQLocators.QUESTION_7, FAQExpectedAnswers.QUESTION_TEXT_7, FAQLocators.ANSWER_7, FAQExpectedAnswers.EXPECTED_ANSWER_7), (FAQLocators.QUESTION_8, FAQExpectedAnswers.QUESTION_TEXT_8, FAQLocators.ANSWER_8, FAQExpectedAnswers.EXPECTED_ANSWER_8)]

@pytest.mark.parametrize('question, question_text, answer, expected_answer', FAQ_DATA)
@allure.title('Проверка текста в вопросе о важном: {question_text}')
@allure.description('Проверяем соттвествует ли текст вопроса тексту ответа')
def test_faq(driver, question, question_text, answer, expected_answer):
    driver.get('https://qa-scooter.praktikum-services.ru/')
    home_page = FAQLocators(driver)
    home_page.accept_cookie()
    home_page.driver.execute_script("arguments[0].scrollIntoView();", home_page.driver.find_element(*question))
    time.sleep(5)
    home_page.driver.find_element(*question).click()
    time.sleep(5)
    assert home_page.driver.find_element(*answer).text == expected_answer

