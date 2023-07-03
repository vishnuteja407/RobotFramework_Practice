*** Settings ***
Documentation    Suite description
Library     SeleniumLibrary
Library     BuiltIn
Library     Collections
Library     RequestsLibrary
Library     JSONLibrary
Library     String
Library     OperatingSystem


*** Variables ***
${base_url}     https://bpa-temp4.cisco.com
${template_url}     https://10.122.32.51:9201
${form_url}     /bpa/api/v2.0/form-builder/forms?search=undefined&sort=undefined&page=1&limit=-1&startedAfter=undefined&startedBefore=undefined&tags=undefined
${import_form_url}      /bpa/api/v1.0/form-builder/form/import
${delete_form_url}      /bpa/api/v1.0/form-builder/form
${forms_path}       /Users/vibodapa/Documents/BPA-3.1.1/AS-BAC-BPA/microservices/bpa-service-pack/data/

*** Test Cases ***
BPA Service Pack Test cases
    Get all Available Forms in BPA
    Delete Forms
    Upload Forms
#    Form Builder Upload API     ${forms_path}/BPA/forms/formBuilderFormsCollection.json

*** Keywords ***
Get all Available Forms in BPA
    ${header}=      Login API
    create session      mysession       ${base_url}
    ${response}=    get on session    mysession   url=${form_url}     headers=${header}
    ${responsejson}=     Set Variable    ${response.json()}
#    log to console      ${responsejson}
    ${form_names}=   create list
    FOR     ${data}      IN      @{responsejson}
        append to list      ${form_names}      ${data["name"]}
    END
#    log to console      ${form_names}
#    ${count}=   get length      ${form_names}
#    log to console      ${count}
    [Return]        ${form_names}

Upload Forms
    directory should exist      ${forms_path}
    @{list_directories}=    List Directory      ${forms_path}
    log to console      ${list_directories}
    FOR     ${directory}    IN      @{list_directories}
        ${status}=      run keyword and return status       directory should exist      ${forms_path}/${directory}/forms
        RUN KEYWORD IF      ${status}
        ...     run keyword and continue on failure
        ...     Form Builder Upload API       ${forms_path}/${directory}/forms/formBuilderFormsCollection.json
    END

Form Builder Upload API
    [Arguments]     ${file_name}
    ${header}=      Login API
    set to dictionary       ${header}       Accept=application/json     Content-Type=application/json   Content-Length=65535    Host=bpa-temp4.cisco.com
    ${file}=    get file       ${file_name}     encoding=UTF-8     encoding_errors=ignore
#    ${file}=    Replace Variables        ${file}
#    ${file}=    Convert String to JSON      ${file}
    create session      mysession       ${base_url}
    ${response}=    post on session    mysession     url=${import_form_url}    headers=${header}      data=${file}
    LOG      ${response.json()}

Delete Forms
    ${header}=      Login API
    ${forms}=   Get all Available Forms in BPA
    log to console      ${forms}
    create session      mysession       ${base_url}
    FOR     ${form}     IN     @{forms}
            ${response}=    delete on session    mysession   url=${delete_form_url}/${form}      headers=${header}
            ${responsejson}=     Set Variable   ${response.json()}
            Should Be Equal As Numbers  ${response.status_code}      ${200}
            Should Be Equal As Strings  ${responsejson['message']}   Form deleted successfully.
            log     ${responsejson}
    END


Login API
    ${auth}=    create list     admin   admin
    create session  mysession   ${base_url}     auth=${auth}
    ${response}=    post on session     mysession   url=/bpa/api/v1.0/login
    ${token_type}=   Get Value From Json  ${response.json()}  $..token_type
    ${token_type}=   Get From List  ${token_type}  0
    ${bearer_token}=    get value from json     ${response.json()}      $..access_token
    ${bearer_token}=   Get From List  ${bearer_token}  0
#    log to console  ${bearer_token}
    ${API_HEADER}=  create dictionary   Authorization=${token_type} ${bearer_token}
#    set suite variable      ${bearer_token}
    [Return]     ${API_HEADER}