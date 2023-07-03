*** Settings ***
Documentation    Suite description
Library     SeleniumLibrary
Library     RequestsLibrary
Library     Collections


*** Variables ***
${base_url}     https://www.metaweather.com/api/location
${city}     Delhi

*** Test Cases ***
Weather info
    Get Weather Info



*** Keywords ***
Get Weather Info
    create session  mySession   ${base_url}
    ${response}=    get request     mySession   /search/?query=${city}
#    log to console  ${response.status_code}
#    log to console  ${response.content}
#    log to console  ${response.headers}

    ${status_code}=     convert to string   ${response.status_code}
    should be equal   ${status_code}    200

    ${body}=    convert to string   ${response.content}
    should contain  ${body}     Delhi

    ${contentTypeValue}=    get from dictionary     ${response.headers}  Content-Type
    should be equal     ${contentTypeValue}     application/json