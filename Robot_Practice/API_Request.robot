*** Settings ***
Documentation    Suite description
Library     SeleniumLibrary
Library     BuiltIn
Library     Collections
Library     RequestsLibrary
Library     JSONLibrary
Library     String
Library     OperatingSystem
#Variables   TestData/process-template.json
Variables   ../API_TestCases/TestData/Setup_details.yaml
Variables   ../API_TestCases/TestData/cewa_variables.yaml

*** Variables ***
${base_url}     https://10.122.32.87:9091
${template_url}     https://10.122.32.87:9201


*** Test Cases ***
Process Template Execution
    Generate Payload for process template execution     Common-Services-Redundant-Power-Supply-CEWA-V1P4P0    power_supply_template_postfix
    Execute Process Templates       ../API_TestCases/TestData/process-template.json      ${ServiceCatalog.order_details.power_supply.expected_fail_command}
#    Generate Payload for process template execution     Common-Services-Pre-Post-Checks-Validations-CEWA-V1P4P0    platform_template_postfix
#    Execute Process Templates       TestData/process-template.json      ${ServiceCatalog.order_details.platform_validation.expected_fail_command}
    Generate Payload for Device Authorization
    Execute Device Auth     ../API_TestCases/TestData/device-auth.json

*** Keywords ***
Generate Payload for process template execution
    [Arguments]     ${Template_Name}    ${Task}
    ${Process_Template_Payload}=    create list
    FOR     ${dev}      IN      @{netsim_devices.devices}
            ${device}=  set variable      ${dev['device']}
            ${postfix}=     set variable    ${dev['${Task}']}
            ${payload}=     create dictionary
            ...     deviceName=${device}
            ...     templateId=${Template_Name}${postfix}
            append to list   ${Process_Template_Payload}    ${payload}

    END
    set suite variable      ${Process_Template_Payload}
#    log to console      ${Process_Template_Payload}


Generate Payload for Device Authorization
    ${Device_Auth_Payload}=     create list
    FOR     ${dev}      IN      @{netsim_devices.devices}
            ${device}=  set variable      ${dev['device']}
            append to list      ${Device_Auth_Payload}     ${device}
    END
    SET SUITE VARIABLE      ${Device_Auth_Payload}

Check BPA Build
    ${header}=      Login API
    create session  mysession   ${base_url}
    ${response}=     get on session     mysession   url=/bpa/api/v1.0/about     headers=${header}
    ${responsejson}=     Set Variable    ${response.json()}
    FOR     ${data}      IN      @{responsejson}
        Run Keyword IF      "${data['name']}" == "@cisco-bpa-platform/mw-core"
        ...     RUN KEYWORD
        ...     set suite variable      ${build_Number}    ${data['version']}
    END
    log to console      ${build_Number}


Set build Number
    [Arguments]     ${build}
    ${build_number}=    Set variable       ${build}
    [Return]        ${build_number}

Execute Device Auth
    [Arguments]     ${payload}
    ${header}=      Login API
    ${payload}=    Get File   ${Payload}
    ${payload}=   Replace Variables     ${payload}
    ${payload}=   Replace String   ${payload}   \'   \"
    create session  mysession   ${base_url}
    set to dictionary       ${header}       Content-Type=application/json   Content-Length=65535
    ${response}=    post on session     mysession   url=/bpa/api/v1.0/common-service/devices/authorization   headers=${header}   data=${Payload}
    ${responsejson}=     Set Variable    ${response.json()}
#    log to console  ${responsejson}
    ${Host_Domain_Arr}=     create list
    set global variable       ${Host_Domain_Arr}
    FOR     ${arr}  IN  @{responsejson['data']['results']}
#        ${arr['domain']}=    Convert To Upper Case    ${arr['domain']}
          run keyword if    '${arr['domain']}' != ''
          ...       Creating Hostname and domain array      ${arr}

    END
    log to console  ${Host_Domain_Arr}
    @{Sorted_host_domain_array}=    evaluate   sorted(${Host_Domain_Arr}, key=lambda i: i['hostname'], reverse=True)
    log   ${Sorted_host_domain_array}
    @{Sorted_expected_array}=      evaluate   sorted(${ServiceCatalog.order_details.device_auth}, key=lambda i: i['hostname'], reverse=True)
    log   ${Sorted_expected_array}
    ${count}=   get length      ${Host_Domain_Arr}

Creating Hostname and domain array
    [Arguments]     ${arr}
    ${host_domain}=     create dictionary
        ...     hostname=${arr['deviceName']}
        ...     domain=${arr['domain']}
    append to list     ${Host_Domain_Arr}       ${host_domain}


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


Execute Process Templates
    [Arguments]     ${payload}      ${expected_fail_commands}
    ${header}=      Login API
#    log to console      ${header}
    ${payload}=    Get File   ${Payload}
    ${payload}=   Replace Variables     ${payload}
    ${payload}=   Replace String   ${payload}   \'   \"
#    log to console  ${payload}
    create session  mysession   ${template_url}
    set to dictionary       ${header}       Content-Type=application/json   Content-Length=65535
#    log to console      ${header}
    ${response}=    post on session     mysession   url=/api/v2.0/template-manager/executions/execute   headers=${header}   data=${Payload}
    ${responsejson}=     Set Variable    ${response.json()}
    should be equal as integers     ${response.status_code}     ${200}
    ${executionObjects}=    get value from json    ${responsejson}       $..executionObjects
    ${executionObjects}=   Get From List  ${executionObjects}  0
    ${CommandList}=    Create List
    log to console      ${expected_fail_commands}
    FOR     ${data}     IN      @{executionObjects}
            ${device_name}=     set variable     ${data['deviceName']}
            ${template_result}=     set variable     ${data['overallTmplResult']}
#            log to console		${device_name}:${template_result}
            ${Length}=     Get Length    ${data['commands']}
#            log to console      ${Length}
            FOR     ${command}      IN      @{data['commands']}
                 ${command_executed}=   set variable    ${command['command']}
                 ${command_index}=   set variable    ${command['cmdIndex']}
                 ${command_result}=   set variable    ${command['overAllCmdResult']}
                 ${command_output}=   set variable    ${command['cmdOutPut']}
                 log to console     ${command_executed}:${command_result}

                 ${deviceIsExists}=     run keyword and return status       dictionary should contain key   ${expected_fail_commands}   ${device_name}
                 log to console     ${deviceIsExists}
                 ${commandIsExists}=    Run Keyword And Return Status        list should contain value    ${expected_fail_commands}[${device_name}]   ${command_executed}
                 log to console     ${commandIsExists}
                 Run Keyword IF   '${command_result}' != 'True' and '${deviceIsExists}' == 'True'
                 ...   Append To List   ${CommandList}   ${command_executed}
                 ...   ELSE IF    ('${command_result}' != 'True' and '${deviceIsExists}' == 'True') and '${commandIsExists}' != 'True'
                 ...   Append To List   ${CommandList}   ${command_executed}
                 ...   ELSE IF    ('${command_result}' == 'True' and '${deviceIsExists}' == 'True') and '${commandIsExists}' == 'True'
                 ...   Append To List   ${CommandList}   ${command_executed}
            END
    END
    log to console      ${CommandList}

