*** Settings ***
Documentation    Suite description
Library     SeleniumLibrary
Resource    ./../Resources/Login_resources.robot

*** Variables ***
${browser}      chrome
${url}      https://demo.nopcommerce.com/

*** Test Cases ***
TestingInputBox
    Input Box Validation


*** Keywords ***
Input Box Validation
    ${speed}=   get selenium speed
    log to console  ${speed}
    Open my browser     ${url}    ${browser}
#    open browser    ${url}  ${browser}
#    maximize browser window
    title should be    nopCommerce demo store
    click link  xpath://a[@class='ico-login']
    title should be     nopCommerce demo store. Login
    ${email_txt}    set variable    id:Email
    element should be visible   ${email_txt}
    element should be enabled   ${email_txt}

    input text  ${email_txt}    123@gmail.com
    sleep   5
    clear element text  ${email_txt}
    sleep   5
    close browser
    ${speed}=   get selenium speed
    log to console  ${speed}

    ${speed2}=   get selenium timeout
    log to console  ${speed2}

#    select radio button     name    value
#    select checkbox
