from selenium import webdriver
import time
from pages.logo_page import LogoPage
import allure

@allure.title('Проверка клика на логотип Яндекса')
@allure.description('Кликаем на логотип Яндекса и проверяем, что открывается окно Яндекса')
def test_dzen_page(driver):
   driver.get('https://qa-scooter.praktikum-services.ru/')
   home_page = LogoPage(driver)
   home_page.dzen_logotip()
   time.sleep(3)
   home_page.page_switch()
   assert "dzen.ru" or "yandex.ru" in driver.current_url

@allure.title('Проверка клика на логотип Самоката')
@allure.description('Кликаем на логотип Самоката и проверяем возвращаемся на главную стрницу')
def test_samokat_page(driver):
   driver.get('https://qa-scooter.praktikum-services.ru/')
   home_page = LogoPage(driver)
   home_page.click_order_button()
   home_page.wait_visibility_order_page()
   home_page.click_samokat_logo()
   time.sleep(3)
   assert driver.current_url == "https://qa-scooter.praktikum-services.ru/"








