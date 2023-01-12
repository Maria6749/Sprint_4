from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class OrderPage:
    order_top_of_the_page_button = [By.CLASS_NAME, "Button_Button__ra12g"]
    loading_page_form=[By.CLASS_NAME, "Order_Form__17u6u"]
    name_field = [By.XPATH, ".//input[@placeholder='* Имя']"]
    surname_field = [By.XPATH, ".//input[@placeholder='* Фамилия']"]
    address_field = [By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']"]
    metro = [By.XPATH, ".//input[@placeholder='* Станция метро']"]
    metro_station_1 = [By.XPATH, "//div[text()='Преображенская площадь']"]
    metro_station_2 = [By.XPATH, "//div[text()='Сокольники']"]
    wait_drop_down = [By.CLASS_NAME, "select-search__select"]
    phone_field = [By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']"]
    further_button = [By.XPATH, ".//button[text()='Далее']"]
    loading_second_pade = [By.XPATH, ".//div[text()='Про аренду']"]
    calendar = [By.XPATH, ".//input[@placeholder='* Когда привезти самокат']"]
    data = [By.XPATH, ".//div[@aria-label='Choose пятница, 27-е января 2023 г.']"]
    data_2 = [By.XPATH, ".//div[@aria-label='Choose пятница, 13-е января 2023 г.']"]
    rental_period_button = [By.XPATH, ".//div[text()='* Срок аренды']"]
    rental_period = [By.XPATH, ".//div[text()='четверо суток']"]
    rental_period_2 = [By.XPATH, ".//div[text()='сутки']"]
    colour =[By.ID, "black"]
    colour_2 = [By.ID, "grey"]
    comment = [By.CLASS_NAME, "Input_Input__1iN_Z Input_Responsible__1jDKN"]
    second_order_button = [By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"]
    loading_confirmation = [By.XPATH, ".//div[@class='Order_ModalHeader__3FDaJ']"]
    button_confirmation = [By.XPATH, ".//button[text()='Да']"]
    order_assert = By.CLASS_NAME, "Order_ModalHeader__3FDaJ"
    page_loading = By.CLASS_NAME, "Order_Content__bmtHS"

    def __init__(self, driver):
        self.driver = driver

    def click_order_button(self):
        self.driver.find_element(*self.order_top_of_the_page_button).click()

    def wait_loading_page_form(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((self.loading_page_form)))

    def click_name_field(self, name):
        self.driver.find_element(*self.name_field).send_keys(name)

    def click_surname_field(self, surname):
        self.driver.find_element(*self.surname_field).send_keys(surname)

    def click_address_field(self, address):
        self.driver.find_element(*self.address_field).send_keys(address)

    def click_metro_field(self):
        self.driver.find_element(*self.metro).click()

    def wait_metro_drop_down(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((self.wait_drop_down)))

    def select_metro_station_1(self):
        self.driver.find_element(*self.metro_station_1).click()

    def select_metro_station_2(self):
        self.driver.find_element(*self.metro_station_2).click()

    def filling_phone_field(self, phone):
        self.driver.find_element(*self.phone_field).send_keys(phone)

    def samokat_order_login(self, name, surname, address, phone ):
        self.click_name_field(name)
        self.click_surname_field(surname)
        self.click_address_field(address)
        self.filling_phone_field(phone)

    def click_further_button(self):
        self.driver.find_element(*self.further_button).click()

    def wait_loading_second_pade(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((self.loading_second_pade)))

    def click_on_calendar(self):
        self.driver.find_element(*self.calendar).click()

    def select_data(self):
        self.driver.find_element(*self.data).click()

    def select_data_2(self):
        self.driver.find_element(*self.data_2).click()

    def click_rental_period_button(self):
        self.driver.find_element(*self.rental_period_button).click()

    def select_rental_period(self):
        self.driver.find_element(*self.rental_period).click()

    def select_rental_period_2(self):
        self.driver.find_element(*self.rental_period_2).click()

    def select_colour(self):
        self.driver.find_element(*self.colour).click()

    def select_colour_2(self):
        self.driver.find_element(*self.colour_2).click()

    def click_second_order_button(self):
        self.driver.find_element(*self.second_order_button).click()

    def wait_loading_confirmation(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((self.loading_confirmation)))

    def click_button_confirmation(self):
        self.driver.find_element(*self.button_confirmation).click()

    def for_order_assert(self):
        return self.driver.find_element(*self.order_assert).text

    def for_second_page_1(self):
        self.click_on_calendar()
        self.select_data()
        self.click_rental_period_button()
        self.select_rental_period()
        self.select_colour()
        self.click_second_order_button()
        self.wait_loading_confirmation()
        self.click_button_confirmation()

    def for_second_page_2(self):
        self.click_on_calendar()
        self.select_data_2()
        self.click_rental_period_button()
        self.select_rental_period_2()
        self.select_colour_2()
        self.click_second_order_button()
        self.wait_loading_confirmation()
        self.click_button_confirmation()

    def scroll(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*self.second_order_button))

    def click_order_button_bottom_of_the_page(self):
        self.driver.find_element(*self.second_order_button).click()
