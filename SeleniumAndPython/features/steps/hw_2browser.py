# -*- coding: utf-8 -*-
from selenium import webdriver
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@given('browser {browsers}')
def step(context, browser):
    context.browser = webdriver.Firefox
    context.browser.maximize_window()

@then('website {url}')
def step(context, url):
    context.browser.get(url)
