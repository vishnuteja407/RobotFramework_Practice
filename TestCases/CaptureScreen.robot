*** Settings ***
Documentation    Suite description
Library     SeleniumLibrary


*** Test Cases ***
Login Test case
    open browser    https://opensource-demo.orangehrmlive.com/  chrome
    input text  id:txtUsername  admin
    input text  id:txtPassword  admin123
    capture element screenshot      xpath://*[@id="divLogo"]/img    /Users/vibodapa/PycharmProjects/robot_Framework_practice/TestCases/Screenshots/logo.png
    capture page screenshot     /Users/vibodapa/PycharmProjects/robot_Framework_practice/TestCases/Screenshots/login-test-case.png
    close all browsers


*** Keywords ***
Provided precondition
    Setup system under test