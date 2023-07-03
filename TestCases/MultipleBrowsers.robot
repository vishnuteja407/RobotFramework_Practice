*** Settings ***
Documentation    Suite description
Library     SeleniumLibrary

*** Test Cases ***
Switch to Multiple browsers
    open browser    https://www.google.com/  chrome
    maximize browser window

    sleep   3

    open browser    https://www.bing.com/   chrome
    maximize browser window
    switch browser  1
    ${title1}=   get title
    log to console  ${title1}
    switch browser  2
    ${title2}=   get title
    log to console  ${title2}

    sleep   3
    close all browsers
*** Keywords ***
Provided precondition
    Setup system under test