*** Settings ***
Documentation    Suite description
Library    SeleniumLibrary

# uses frame tag
*** Test Cases ***
Hanling Frames
    open browser   https://www.selenium.dev/blog/     chrome
    maximize browser window
    select frame    packageListFrame    #id name xpath
    click link  org.openqa.com
    unselect frame
    select frame    packageFrame
    click link   webdriver
    unselect frame

*** Keywords ***
Provided precondition
    Setup system under test