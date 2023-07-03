*** Settings ***
Documentation    Suite description
Library     SeleniumLibrary
Library     BuiltIn


*** Variables ***

*** Test Cases ***
TC01
    set suite variable   ${suite_variable}   This is suite variable
    Log to console       ${suite_variable}

TC02
    Log to console       ${suite_variable}


*** Keywords ***

