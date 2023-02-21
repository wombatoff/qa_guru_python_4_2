import pytest
from selene import be, have
from selene.support.shared import browser

TEST_URL = 'https://demoqa.com/automation-practice-form'


@pytest.fixture
def configured_browser():
    browser.config.window_height = 960
    browser.config.window_width = 720
    return browser


def test_positive(configured_browser):
    browser.open(TEST_URL)
    browser.element('[id="firstName"]').should(be.blank).type('Oleg')
    browser.element('[id="lastName"]').should(be.blank).type('Greckiy')
    browser.element('[for="gender-radio-1"]').should(be.clickable).click()
    browser.element('[id="userNumber"]').should(be.blank).type('1234567890')
    browser.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    browser.element('[id="submit"]').should(be.clickable).click()
    assert browser.element('[id="example-modal-sizes-title-lg"]').should(have.text('Thanks for submitting the form'))


def test_negative(configured_browser):
    browser.open(TEST_URL)
    browser.element('[id="firstName"]').should(be.blank).type('Oleg')
    browser.element('[id="lastName"]').should(be.blank).type('Greckiy')
    browser.element('[for="gender-radio-1"]').should(be.clickable).click()
    browser.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    browser.element('[id="submit"]').should(be.clickable).click()
    assert browser.element('[id="submit"]').should(be.clickable)
