*** Settings ***
Documentation    Suite description
Library     RequestsLibrary
Library     Collections
Library     JSONLibrary

*** Variables ***
${base_url}     https://bpa-temp1.cisco.com/monitoring

*** Test Cases ***
Basic Auth
    ${auth}=    create list     admin   Cisc0123
    create session  mysession   ${base_url}     auth=${auth}
    ${response}=    post on session     mysession   url=/api/v1/query?query=probe_success
#    log to console      ${response.content}
    ${listData}=    get value from json     ${response.json()}      $.data.result
#    log to console      ${listData}[0]
    ${lenList}=     get length   ${listData}[0]
    log to console      ${lenList}
    ${endPointsList}=    Create List
    ${endPointsStatusList}=    Create List
    ${dictObj}=     Create Dictionary
    FOR     ${i}    IN RANGE    0     ${lenList}
        exit for loop if    ${i}==${lenList}
        ${endPoint}=   get value from json     ${response.json()}      $.data.result[${i}].metric.instance
        ${endPoints} =	Remove From List	${endPoint} 	0
        Append To List   ${endPointsList}      ${endPoints}
        ${endPointStatus}=   get value from json     ${response.json()}      $.data.result[${i}].value[1]
        ${endPointStatus} =	Remove From List	${endPointStatus} 	0
        Append To List   ${endPointsStatusList}      ${endPointStatus}
    END
#    log to console      ${endPointsList}
    FOR     ${i}     IN RANGE     0    ${lenList}
        ${key}=     get from list   ${endPointsList}    ${i}
        ${value}=     get from list   ${endPointsStatusList}    ${i}
#        log to console     (${key}, ${value})
        set to dictionary   ${dictObj}   ${key}=${value}
    END
    log to console      ${dictObj}



*** Keywords ***
Provided precondition
    Setup system under test