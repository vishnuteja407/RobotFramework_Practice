*** Settings ***
Documentation    Suite description
Library     SeleniumLibrary

*** Test Cases ***
Tabbed Windows
    open browser    http://demo.automationtesting.in/Windows.html   chrome
    click element   xpath://*[@id="Tabbed"]/a/button
    switch window   title=Selenium
    click element   xpath://*[@id="main_navbar"]/ul/li[5]/a/span
    sleep   3
    close all browsers
*** Keywords ***
Provided precondition
    Setup system under test