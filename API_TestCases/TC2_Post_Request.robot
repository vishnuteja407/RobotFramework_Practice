*** Settings ***
Documentation    Suite description
Library     RequestsLibrary
Library     Collections
Library     JSONLibrary
Library     BuiltIn

*** Variables ***
${base_url}     https://gorest.co.in/public
${auth}     Bearer c0185a87cbfcc27f397631eb8bf472b237edb8a7b7081233870671c21b261414



*** Test Cases ***
Customer Registration
    create session  mysession   ${base_url}
    ${body}=    create dictionary   name=Test Automation TestingUser-132    gender=male   email=textEmailtestinguser132@gmail.com   status=active
    ${headers}=  create dictionary  Content-Type=application/json   Authorization=${auth}
    ${response}=    POST request    mysession   /v1/users    headers=${headers}     data=${body}
    log to console  ${response.status_code}
    log to console  ${response.content}

    ${res_body}=    convert to string   ${response.content}
    should contain  ${res_body}  Test Automation TestingUser-132

    ${id}=  Get Value From Json  ${response.json()}     $.data[id]
    ${id1}=  remove from list    ${id}   0
    ${id_value}=    set variable    ${id1}
    set global variable    ${id_value}

Deleting registered customer
    create session  mysession   ${base_url}
    ${headers}=  create dictionary   Authorization=${auth}
    ${response}=    delete request     mysession   /v1/users/${id_value}    headers=${headers}
    should be equal     ${response.status_code}     ${204}


