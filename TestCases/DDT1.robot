*** Settings ***
Documentation    Suite description
Library     SeleniumLibrary
Resource    ../Resources/Login_resources.robot

Suite Setup     Open my browser
Suite Teardown      Close Browsers
Test Template       Invalid Login

*** Test Cases ***      username        password
Right user empty pass       admin@yourstore.com     ${EMPTY}
Right user wrong pass       admin@yourstore.com     adsaf
wrong user right pass       adm@sotre.com       admin
wrong user emptypass        admi@ds.com     ${EMPTY}
wrong user wrong pass       admin@sdasd.com     sdsad



*** Keywords ***
Invalid Login
    [Arguments]     ${username}     ${password}
    Input username      ${username}
    Input pwd       ${password}
    click login button
    Error message should be visible
