*** Settings ***
Documentation    Suite description
Library   SSHLibrary
Library  Screenshot
Library  SeleniumLibrary
Variables  ./resource.yaml

*** Test Cases ***
Test title
    [Tags]    DEBUG
    Login to linux server and run some commands  ${server_name}  ${user_name}  ${password}

*** Keywords ***
Login to linux server and run some commands
    [Arguments]  ${server_name}  ${user_name}  ${password}
    Open Connection  ${server_name}
    Login  ${user_name}  ${password}  delay=1
    Execute Command  ncs_cli -C
#    Log Screenshot   ./take screenshot
    Close All Connections