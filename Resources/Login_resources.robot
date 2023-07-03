*** Settings ***
Library     SeleniumLibrary
Library     BuiltIn


*** Variables ***
#${loginUrl}     https://admin-demo.nopcommerce.com/
${loginUrl}     https://www.google.com
${browser}      chrome

*** Keywords ***
Open my browser
    [Arguments]      ${loginUrl}     ${browser}
    open browser    ${loginUrl}     ${browser}
    maximize browser window

Close Browsers
    close all browsers

Open Login Page
    go to   ${loginUrl}

Input username
    [Arguments]     ${username}
    clear element text      id:Email
#    Fatal Error
    input text      id:Email    ${username}

Input pwd
    [Arguments]     ${password}
    clear element text      id:Password
    input text   id:Password    ${password}

Click Login Button
    click element       xpath://button[@class="button-1 login-button"]

Click Logout link
    click link      Logout

Error message should be visible
    page should contain     Login was unsuccessful

Dashboard page should be visible
    page should contain     Dashboard


