*** Settings ***
Library  SeleniumLibrary

*** Variables ***

*** Test Cases ***
LoginBrowser
#    create webdriver    chrome     executable_path="/usr/local/bin/chromedriver.dmg"
    open browser  https://demo.nopcommerce.com/  chrome
    Login to Application
    close browser

*** Keywords ***
Login to Application
    maximize browser window
    click link  xpath://a[contains(text(),'Register')]
    click button    xpath://input[@id='gender-male']
    input text   //input[@id='FirstName']   Vishnu Teja
    input text   id:LastName    Bodapati
    select from list by index    name:DateOfBirthDay     5
    select from list by index    name:DateOfBirthMonth     8
    select from list by index    name:DateOfBirthYear     50
    input text      id:Email    vishnuteja407@gmail.com
    input text      id:Company  Company
    input password     xpath://input[@id='Password']   tqsy7k@jWFFiABd
    input password      id:ConfirmPassword      tqsy7k@jWFFiABd
    click button        xpath://button[@id='register-button']

