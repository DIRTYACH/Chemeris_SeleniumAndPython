Feature: Checking search
Scenario: Сheck Chrome
  Given open website "https://google.ru"
  Then enter the text "Something"
  #When text is correct