from selenium.webdriver.common.by import By


class MainPageLocators:
    main_header = By.CLASS_NAME, 'Home_Header__iJKdX'
    # Секция вопросы о важном
    faq_section = By.CLASS_NAME, 'Home_FAQ__3uVm4'
    faq_questions_items = {
        1: [By.XPATH, '//div[@id="accordion__heading-0"]/parent::div'],
        2: [By.XPATH, '//div[@id="accordion__heading-1"]/parent::div'],
        3: [By.XPATH, '//div[@id="accordion__heading-2"]/parent::div'],
        4: [By.XPATH, '//div[@id="accordion__heading-3"]/parent::div'],
        5: [By.XPATH, '//div[@id="accordion__heading-4"]/parent::div'],
        6: [By.XPATH, '//div[@id="accordion__heading-5"]/parent::div'],
        7: [By.XPATH, '//div[@id="accordion__heading-6"]/parent::div'],
        8: [By.XPATH, '//div[@id="accordion__heading-7"]/parent::div']
    }

    faq_answers_items = {
        1: (By.XPATH, '//div[@id="accordion__panel-0"]'),
        2: (By.XPATH, '//div[@id="accordion__panel-1"]'),
        3: (By.XPATH, '//div[@id="accordion__panel-2"]'),
        4: (By.XPATH, '//div[@id="accordion__panel-3"]'),
        5: (By.XPATH, '//div[@id="accordion__panel-4"]'),
        6: (By.XPATH, '//div[@id="accordion__panel-5"]'),
        7: (By.XPATH, '//div[@id="accordion__panel-6"]'),
        8: (By.XPATH, '//div[@id="accordion__panel-7"]')
    }

    # Кнопка "Заказать" в хэдере
    order_button_in_header = By.XPATH, '//div[@class = "Header_Nav__AGCXC"]/button[text() = "Заказать"]'

    # Кнопка "Заказать" внизу страницы
    order_button_in_main = By.XPATH, '//div[contains(@class, "Home_FinishButton")]/button'

    # Лого "Самокат" в хэдере
    header_logo_scooter = By.XPATH, '//a[@href="/" and contains(@class, "Header_LogoScooter")]'

    # Лого "Яндекс" в хэдере
    header_logo_yandex = By.XPATH, '//a[@href="//yandex.ru" and contains(@class, "Header_LogoYandex")]'

    title_of_page = By.TAG_NAME, 'title'
