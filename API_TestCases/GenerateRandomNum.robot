*** Settings ***
Documentation    Suite description
Library     SeleniumLibrary
Library     Collections
Library     String
Library     BuiltIn
Library     OperatingSystem

*** Variables ***
${file_name}    TestData/create-srf-request-body.txt

*** Test Cases ***
Generate Random Number
    ${PO_Number}=    Generate random string    13    0123456789
    log to console      ${PO_Number}
    ${PO_Number}=    convert to integer      ${PO_Number}
    log to console      ${PO_Number}
    set global variable    ${PO_Number}
Read data from File
    [Arguments]     ${file_name}
    ${contents}=    Get file    ${file_name}
    ${contents}=    replace variables   ${contents}
    log to console      ${contents}


*** Keywords ***
Provided precondition
    Setup system under test