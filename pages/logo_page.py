from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class LogoPage:
    dzen_logo = [By.CLASS_NAME, "Header_LogoYandex__3TSOI"]
    order_button = [By.CLASS_NAME, "Button_Button__ra12g"]
    samokat_order_header = [By.CLASS_NAME, "Order_Form__17u6u"]
    samokat_logo = [By.CLASS_NAME, "Header_LogoScooter__3lsAR"]
    cookies = [By.XPATH, ".//button[text()='да все привыкли']"]


    def __init__(self, driver):
        self.driver = driver

    def dzen_logotip(self):
        self.driver.find_element(*self.dzen_logo).click()

    def page_switch(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def click_order_button(self):
        self.driver.find_element(*self.order_button).click()

    def wait_visibility_order_page(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((self.samokat_order_header)))

    def click_samokat_logo(self):
        self.driver.find_element(*self.samokat_logo).click()