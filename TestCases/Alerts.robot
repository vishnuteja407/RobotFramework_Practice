*** Settings ***
Documentation    Suite description
Library     SeleniumLibrary

*** Test Cases ***
Handling Alerts
    open browser    https://testautomationpractice.blogspot.com/    chrome
    maximize browser window
    click button    xpath://*[@id="HTML9"]/div[1]/button
    sleep   3
    handle alert    accept
    page should contain     You pressed OK!
    click button    xpath://*[@id="HTML9"]/div[1]/button
    sleep   3
    handle alert    dismiss
    page should contain     You pressed Cancel!
#    close browser
    click button    xpath://*[@id="HTML9"]/div[1]/button[2]
    handle alert    leave
    alert should be present     Press a button!
    close browser



*** Keywords ***
