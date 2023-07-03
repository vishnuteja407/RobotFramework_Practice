*** Settings ***
Documentation    Validating Login Resources
Library     SeleniumLibrary
Library     BuiltIn
Resource    ../Resources/Login_resources.robot

Test Setup         Open my browser    ${Url}     ${browser}
Test Teardown      Close Browsers

*** Variables ***
#${loginUrl}     https://admin-demo.nopcommerce.com/
${Url}     https://the-internet.herokuapp.com/nested_frames
${browser}      chrome

*** Test Cases ***
Working with Frames
    Handling Frames

*** Keywords ***
Handling Frames
#    set selenium speed  1s
    Wait Until Element Is Visible  css:[frameborder="1"]  timeout=5
    Select Frame  css:[src="/frame_top"]
    Select Frame  css:[src="/frame_left"]
    Current Frame Should Contain  LEFT
    Unselect Frame
    Select Frame  css:[src="/frame_top"]
    Select Frame  css:[src="/frame_middle"]
    Current Frame Should Contain  MIDDLE
    Unselect Frame
    Select Frame  css:[src="/frame_top"]
    Select Frame  css:[src="/frame_right"]
    Current Frame Should Contain  RIGHT
    Unselect Frame
    Select Frame  css:[src="/frame_bottom"]
    Current Frame Should Contain  BOTTOM


#Setup
#    open browser   ${Url}     ${browser}
#    maximize browser window


