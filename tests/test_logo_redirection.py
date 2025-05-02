import allure
from page_objects.main_page import MainPage


class TestLogoRedirect:
    @allure.title('Проверка перехода на главную страницу при клике на лого "Самокат" в хэдере')
    def test_logo_transfer_to_main_page_success(self, driver):
        main_page = MainPage(driver)
        main_page.wait_visibility_of_order_button_in_header()
        main_page.click_on_order_button_in_header()
        main_page.wait_visibility_of_header_logo_scooter()
        main_page.click_on_logo_scooter()
        main_page.wait_visibility_of_main_header()
        assert main_page.check_displaying_of_main_header()

    @allure.title('Провера перехода на страницу "Дзен" при клике на лого "Яндекс"')
    def test_logo_transfer_to_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.wait_visibility_of_header_logo_yandex()
        main_page.click_on_logo_yandex()
        main_page.swich_to_next_tab()
        main_page.wait_for_dzen_load()
        assert main_page.get_current_url().startswith('https://dzen.ru')
