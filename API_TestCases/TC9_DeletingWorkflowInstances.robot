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
#${base_url}     http://localhost:8000
${base_url}     https://10.122.32.87:9091
${get_workflow_instances_url}       /bpa/api/v1.0/workflow/history/process-instances/get
${delete_workflow_instances_url}      /bpa/api/v1.0/workflow/process-instance

*** Test Cases ***
Deleting Workflow Instances
    Get all Workflow Instances
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

Get all Workflow Instances
    ${header}=  Login API
    set to dictionary       ${header}
    create session   mysession   ${base_url}
    ${response}=    post on session    mysession     url=${get_workflow_instances_url}    headers=${header}
    ${responseJson}=    set variable    ${response.json()}
    FOR     ${data}     IN      @{responseJson}
#        run keyword if      '${data["processDefinitionName"]}'=='Remedy.WorkOrder.AddPhone' and '${data["state"]}'=='ACTIVE'
        run keyword if      '${data["state"]}'=='ACTIVE'
        ...     Delete Workflow instances      ${data["id"]}
    END

Delete Workflow instances
    [Arguments]     ${id}
    ${header}=  Login API
    create session   mysession   ${base_url}
    ${response}=    delete on session    mysession     url=${delete_workflow_instances_url}/${id}    headers=${header}
    should be equal as numbers      ${response.status_code}     ${200}
