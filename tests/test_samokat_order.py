from pages.order_page import OrderPage
import pytest
import allure

@pytest.mark.parametrize('name', ['Мария', 'Максим'])
@pytest.mark.parametrize('surname', ['Иванова', 'Петрова'])
@pytest.mark.parametrize('address', ['Любимая 11', 'Ленина 18'])
@pytest.mark.parametrize('phone', ['+7693498684'])
@allure.title('Проверка заказа самоката по кнопке вверху страницы')
@allure.description('На странице с заказом проверяем, что тест в заголовке == "Заказ оформлен"')
def test_samokat_order_top_of_the_page(driver,name,surname,address,phone):
    driver.get('https://qa-scooter.praktikum-services.ru/')
    home_page = OrderPage(driver)
    home_page.click_order_button()
    home_page.wait_loading_page_form()
    home_page.samokat_order_login(name,surname,address,phone)
    home_page.click_metro_field()
    home_page.wait_metro_drop_down()
    if name == 'Мария':
        home_page.select_metro_station_1()
    else:
        home_page.select_metro_station_2()
    home_page.click_further_button()
    home_page.wait_loading_second_pade()
    if surname == 'Петрова':
        home_page.for_second_page_1()
    else:
        home_page.for_second_page_2()
    text_in_header = home_page.for_order_assert()
    assert 'Заказ оформлен' in text_in_header








