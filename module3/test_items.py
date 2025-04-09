import pytest
from selenium.webdriver.common.by import By
import time

def test_baket_button(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    basket_button = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    assert basket_button, "Нет кнопки добавления в корзину!"
    #time.sleep(30)