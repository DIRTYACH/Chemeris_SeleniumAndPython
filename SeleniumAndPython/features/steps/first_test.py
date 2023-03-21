# -*- coding: utf-8 -*-
from selenium import webdriver
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


#Откроем главную страницу. Передадим в качестве аргумента адрес страницы.
@given('open website "{url}"')
def step(context, url):
    context.browser = webdriver.Firefox()
    context.browser.maximize_window()
    context.browser.get(url)

#Теперь нажмем на кнопку "Найти"
@then("push button with text '{text}'")
def step(context, text):
    WebDriverWait(context.browser, 120).until(
        EC.element_to_be_clickable((By.XPATH, '//button'))
    )
    context.browser.find_element_by_xpath('//button').click()

#Проверим, что мы на странице с результатами поиска, есть некоторый искомый текст
@then("page include text '{text}'")
def step(context, text):
    WebDriverWait(context.browser, 120).until(
        EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "%s")]' % text))
    )
    assert context.browser.find_element_by_xpath('//*[contains(text(), "%s")]' % text)
    context.browser.quit()

#Вводим текст в поле поиска
@then("enter the text {text}")
def step(context, text):
    context.browser.find_element(By.NAME, "q").send_keys("minecraft", Keys.ARROW_DOWN)


@when("text is correct")
def step(context):
    
