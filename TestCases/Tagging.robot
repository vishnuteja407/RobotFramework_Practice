*** Settings ***
Documentation    Suite description

*** Test Cases ***
TC01 User registration test
    [Tags]      regression
    Log to console  This is user registration test
    Log to console      User registration test completed

TC02 Login Test
    [Tags]      sanity
    Log to console  This is login test
    Log to console  Login test is over

TC03 change user settings
    [Tags]      regression
    Log to console  This is changing user settings test
    Log to console  Change User settings test is over

TC04 logout test
    [Tags]      sanity
    Log to console  This is logout test
    Log to console  Logout test is over

*** Keywords ***
Provided precondition
    Setup system under test