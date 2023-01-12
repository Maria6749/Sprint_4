from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class FAQLocators:
    drop_menu_0 = [By.CLASS_NAME, "Home_FAQ__3uVm4"]
    loading_drop_down= [By.CLASS_NAME, "Home_FAQ__3uVm4"]
    drop_down_menu_question_0 = [By.ID, "accordion__heading-0"]
    drop_down_menu_answer_0 = [By.ID, "accordion__panel-0"]
    cookie_button = [By.CLASS_NAME,'App_CookieButton__3cvqF']

    QUESTION_1 = By.ID, "accordion__heading-0"
    QUESTION_2 = By.ID, "accordion__heading-1"
    QUESTION_3 = By.ID, "accordion__heading-2"
    QUESTION_4 = By.ID, "accordion__heading-3"
    QUESTION_5 = By.ID, "accordion__heading-4"
    QUESTION_6 = By.ID, "accordion__heading-5"
    QUESTION_7 = By.ID, "accordion__heading-6"
    QUESTION_8 = By.ID, "accordion__heading-7"

    ANSWER_1 = By.ID, "accordion__panel-0"
    ANSWER_2 = By.ID, "accordion__panel-1"
    ANSWER_3 = By.ID, "accordion__panel-2"
    ANSWER_4 = By.ID, "accordion__panel-3"
    ANSWER_5 = By.ID, "accordion__panel-4"
    ANSWER_6 = By.ID, "accordion__panel-5"
    ANSWER_7 = By.ID, "accordion__panel-6"
    ANSWER_8 = By.ID, "accordion__panel-7"


    def __init__(self, driver):
        self.driver = driver

    def scroll(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*self.QUESTION_8))

    def accept_cookie(self):
        self.driver.find_element(*self.cookie_button).click()

    def wait_loading_drop_down(self):
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((self.loading_drop_down)))

    def click_after_scroll(self):
        self.driver.find_element(*self.drop_down_menu_question_0).click()

    def wait_for_load_home_page(self):
        time.sleep(5)

    def text_dropdown_menu(self):
        return self.driver.find_element(*self.drop_down_menu_answer_0).text

