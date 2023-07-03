*** Settings ***
Documentation    Suite description
Library     JSONLibrary
Library     os
Library     Collections
Library     RequestsLibrary

*** Variables ***
${base_url}     https://jsonplaceholder.typicode.com


*** Test Cases ***
Test case1
    ${json_obj}=     load json from file    ../Testdata/Sample.json
    ${value}=   get value from json     ${json_obj}     $..create[0]["ios-global-conf-aaa-cfs:ios-global-conf-aaa-cfs"][0].tacacs[1]["server-name"]
    log to console      ${value[0]}
    should be equal     ${value[0]}     10.122.32.90

    ${value}=   get value from json     ${json_obj}     $.create[0]["ios-global-conf-aaa-cfs:ios-global-conf-aaa-cfs"][0].device
    log to console      ${value[0]}
    should be equal     ${value[0]}     ROBOT-C9300-48U-2-V17

Test case 2
    create session  mysession   ${base_url}
    ${response}=    GET On Session     mysession   /users
    ${json_object}=     to json     ${response.content}
    ${email}=   get value from json     ${json_object}     $[1].email
    log to console  ${email[0]}
    should be equal     ${email[0]}     Shanna@melissa.tv
    should not contain any      ${email[0]}     Shanna@email.tv     Shanna@lissa.tv

*** Keywords ***
Provided precondition
    Setup system under test