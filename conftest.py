import pytest
from selene import browser


@pytest.fixture(scope="session")
def browser_object():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield browser
    browser.quit()


@pytest.fixture
def yandex(browser_object):
    browser_object.open('https://ya.ru')
