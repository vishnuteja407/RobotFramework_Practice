*** Settings ***
Documentation    Suite description
Library     RequestsLibrary
Library     Collections

*** Variables ***
${base_url}     http://jsonplaceholder.typicode.com

*** Test Cases ***
Test Headers
    create session  mysession   ${base_url}
    ${response}=    get on session  mysession   /photos

    log to console  ${response.headers}

    ${contentType}=     get from dictionary     ${response.headers}     Content-Type
    should be equal     ${contentType}      application/json; charset=utf-8

    log to console  ${response.cookies}
