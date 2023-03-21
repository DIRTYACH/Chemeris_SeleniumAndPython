# -*- coding: utf-8 -*-
from selenium import webdriver
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


#Откроем главную страницу. Передадим в качестве аргумента адрес страницы.
@given('websites firefoxs')
def step(context):
    WebDriverWait(context.browser, 120)
    context.browser = webdriver.Firefox()
    context.browser.maximize_window()
    context.browser.get('https://google.com')

#Вводим текст в поле поиска
@when("enter the texts {text}")
def step(context, text):
    context.browser.find_element(By.NAME, "text").send_keys("google", Keys.ENTER)

@then('summ of res is 10')
def step(context):
    assert (context.browser.find_element_by_xpath('//*[local-name()=element]/count(*)')==10)
