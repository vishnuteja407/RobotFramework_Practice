*** Settings ***
Documentation    Suite description
Library     SeleniumLibrary
Library     DataDriver      file=../TestData/LoginData.xlsx      sheet_name=Sheet1
Resource    ../Resources/Login_resources.robot
Suite Setup     Open my browser
Suite Teardown      close browsers
Test Template       Invalid Login

*** Test Cases ***
LoginTestwithExcel using ${username} ${password}

*** Keywords ***
Invalid Login
    [Arguments]     ${username}     ${password}
    Input username      ${username}
    Input pwd       ${password}
    click login button
    Error message should be visible