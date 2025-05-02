import pytest
from selenium import webdriver
from locators.urls import BaseUrls

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(BaseUrls.BASE_URL)
    yield driver
    driver.quit()