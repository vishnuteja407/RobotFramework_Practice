*** Settings ***
Documentation    Suite description
Library     SeleniumLibrary
Library     BuiltIn
Library     Collections
Library     RequestsLibrary
Library     JSONLibrary
Library     String
Library     OperatingSystem


#Suite Setup        open browser        https://www.google.com/     chrome    desired_capabilities=${capabilities}
#Suite Teardown      close browser

*** Variables ***
#${base_url}     http://localhost:8000
${base_url}     https://10.122.32.87:9091
${get_workflow_instances_url}       /bpa/api/v1.0/workflow/history/process-instances/get
${delete_workflow_instances_url}      /bpa/api/v1.0/workflow/process-instance
&{browser_logging_capability}    browser=ALL
&{capabilities}    browserName=chrome    version=${EMPTY}    platform=ANY    goog:loggingPrefs=${browser_logging_capability}


*** Test Cases ***
Parse jwt token
    Generate Random Data
#    Decode JWT Token
#    Generate Payload for Device Authorization

*** Keywords ***
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


Decode JWT Token
    ${header}=  Login API
    @{data}=     get value from json       ${header}        $..Authorization
    ${data}=     split string       @{data}
    log     ${data}
    ${data}=     split string       ${data}[1]       .
    log     ${data}
    ${data}=     Replace String     ${data}[1]      -   +
    log     ${data}
    ${data}=     Replace String     ${data}         _   /
    log     ${data}
    ${JSONResponse}=    execute javascript   return decodeURIComponent(window.atob(arguments[0]).split('').map(function(c) { return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);}).join(''));       ARGUMENTS      ${data}
    ${ParsedJSONResponse}=      execute javascript      return JSON.parse(arguments[0]);     ARGUMENTS   ${JSONResponse}
    set global variable     ${ParsedJSONResponse}

Generate Payload for Device Authorization
    ${device_auth_payload}=     create dictionary
    ${GroupsInfo}=  get value from json     ${ParsedJSONResponse}   $..rol
    ${GroupsInfo}=  split string    ${GroupsInfo}[0]   ,
    log     ${GroupsInfo}
    ${IsAdminUser}=    get value from json   ${ParsedJSONResponse}      $..adm
    ${IsAdminUser}=    execute javascript   return arguments[0]==='True' ? true : false;    ARGUMENTS      ${IsAdminUser}[0]
    log     ${IsAdminUser}
    set to dictionary   groups=${GroupsInfo}        admin=${IsAdminUser}


#Decode JWT Token
#    ${header}=  Login API
#    @{data}=     get value from json       ${header}        $..Authorization
#    ${token}=     split string       @{data}
#    ${token}=     set variable      ${token}[1]
#    set suite variable      ${token}
#    ${file}=      get file      TestData/decodejwt.js
#    ${resultfile}=      replace variables       ${file}
#    log     ${resultfile}
#    execute javascript      ${resultfile}       ARGUMENTS      ${token}


Get Browser Console Log Entries
    ${selenium}=    Get Library Instance    SeleniumLibrary
    ${webdriver}=    Set Variable     ${selenium._drivers.active_drivers}[0]
    ${log entries}=    Evaluate    $webdriver.get_log('browser')
    [Return]    ${log entries}

Generate Random Data
    ${Process_Instance_ID}=      generate random string      25      [NUMBERS][LETTERS]
    log to console   ${Process_Instance_ID}

