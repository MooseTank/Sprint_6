from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver.support.wait import WebDriverWait

from locators.main_page_locators import MainPageLocators
from page_objects.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Ожидание загрузки кнопки "Заказать" в хэдере')
    def wait_visibility_of_order_button_in_header(self):
        self.wait_visibility_of_element(MainPageLocators.order_button_in_header)

    @allure.step('Нажать кнопку "Заказать" в хэдере')
    def click_on_order_button_in_header(self):
        self.click_on_element(MainPageLocators.order_button_in_header)

    @allure.step('Дождаться загрузки лого "Самокат" в хэдере')
    def wait_visibility_of_header_logo_scooter(self):
        self.wait_visibility_of_element(MainPageLocators.header_logo_scooter)

    @allure.step('Дождаться загрузка лого "Яндекс" в хэдере')
    def wait_visibility_of_header_logo_yandex(self):
        self.wait_visibility_of_element(MainPageLocators.header_logo_yandex)

    @allure.step('Кликнуть по лого "Самокат" в хэдере')
    def click_on_logo_scooter(self):
        self.click_on_element(MainPageLocators.header_logo_scooter)

    @allure.step('Кликнуть по лого "Яндекс" в хэдере')
    def click_on_logo_yandex(self):
        self.click_on_element(MainPageLocators.header_logo_yandex)

    @allure.step('Дождаться загрузки зоголовка главной страницы')
    def wait_visibility_of_main_header(self):
        self.wait_visibility_of_element(MainPageLocators.main_header)

    @allure.step('Проверить отображение заголовка главной страницы')
    def check_displaying_of_main_header(self):
        return self.check_displaying_of_element(MainPageLocators.main_header)

    @allure.step('Проскроллить до раздела "Вопросы о важном"')
    def scroll_to_faq_section(self):
        self.scroll_to_element(MainPageLocators.faq_section)

    @allure.step('Дождаться загрузки нужного номера вопроса в секции "Вопросы о важном"')
    def wait_visibility_of_faq_items(self, data):
        self.wait_visibility_of_element(MainPageLocators.faq_questions_items[data])

    @allure.step('Кликнуть на нужный номер вопроса в секции "Вопросы о важном"')
    def click_on_faq_items(self, data):
        self.click_on_element(MainPageLocators.faq_questions_items[data])

    @allure.step('Дождаться загрузки нужного ответа в секции "Вопросы о важном"')
    def wait_visibility_of_faq_answer(self, data):
        self.wait_visibility_of_element(MainPageLocators.faq_answers_items[data])

    @allure.step('Получить текст нужного отвеета в секции "Вопросы о важном"')
    def get_displayed_text_from_faq_answers(self, data):
        return self.get_text_on_element(MainPageLocators.faq_answers_items[data])

    @allure.step('Получить адрес текущей страницы')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Ожидание загрузки страницы "Дзен"')
    def wait_for_dzen_load(self):
        WebDriverWait(self.driver, 20).until(EC.url_contains('https://dzen.ru'))