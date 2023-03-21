Feature: Checking search
Scenario: Сheck Chrome
  Given browser "Chrome"
Scenario: Check Chrome "https://ya.ru"
  Then website "https://ya.ru"
Scenario: Сheck Firefox
  Given browser "Firefox"
Scenario: Check Firefox "https://ya.ru"
  Then website "https://ya.ru"