

# selenium test first practice

#from selenium import webdriver

# def test_ope_browser():
#     driver=webdriver.Chrome()
#     driver.get("https://www.selenium.dev/")
#     print(driver.title)
#     driver.quit()


#
# def test_open_browser():
#     driver=webdriver.Chrome()
#     driver.get("https://www.selenium.dev/")
#     assert "Selenium" in driver.title
#     driver.quit()


# Task 1 with pytest.fixtures open selenium.dev and validate the title Selenium

import pytest
from selenium import webdriver
@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

def test_selenium_title(driver):
    driver.get("https://www.selenium.dev/")
    assert "Selenium" in driver.title

def test_selenium_url(driver):
    driver.get("https://www.selenium.dev/")
    assert "selenium.dev" in driver.current_url

def test_selenium_refresh(driver):
    driver.get("https://www.selenium.dev/")
    driver.refresh()
    assert "Selenium" in driver.title








