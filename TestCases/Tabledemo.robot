*** Settings ***
Documentation    Suite description
Library     SeleniumLibrary
Library     String

*** Test Cases ***
Table Validations
    open browser    https://testautomationpractice.blogspot.com/    chrome
    maximize browser window
    ${rowCount}=    get element count   xpath://table[@name="BookTable"]/tbody/tr
    log to console  ${rowCount}
    ${columnCount}=    get element count   xpath://table[@name="BookTable"]/tbody/tr[1]/th
    log to console  ${columnCount}

    ${data}=    get text    xpath://table[@name="BookTable"]/tbody/tr[5]/td[1]
    log to console  ${data}

    table column should contain     xpath://table[@name="BookTable"]    2   Author

    table row should contain        xpath://table[@name="BookTable"]    4   Learn JS

    table cell should contain       xpath://table[@name="BookTable"]    5   2   Mukesh

    table header should contain     xpath://table[@name="BookTable"]       BookName
    close browser

*** Keywords ***
Provided precondition
    Setup system under test