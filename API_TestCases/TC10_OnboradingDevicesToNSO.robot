*** Settings ***
Documentation    Suite description
Library     SeleniumLibrary
Library     BuiltIn
Library     Collections
Library     RequestsLibrary
Library     JSONLibrary
Library     String
Library     OperatingSystem
Library     SSHLibrary
Test Setup       Testcase Setup
Test Teardown    Testcase Teardown

*** Variables ***
${NSO_Host}     10.81.59.59
${Username}     zsnso02
${Password}     rtpR0bot
#${file_name}    TestData/Common-Service-CEWA-Voice-Devices.csv
${file_name}     TestData/common-service-cewa-datacenter-devices.csv
${netsim_device_authgroup}     dc_netsim_local
${real_device_authgroup}       dc_local
${Device_description}       CEWA_DC_Device


*** Test Cases ***
Onboarding devices to NSO
    Fetch existing authgroups
    Devices onboarding to NSO
#    Reading Data From CSV File and Onboard Devices To NSO       ${file_name}

*** Keywords ***
Devices onboarding to NSO
#    [Setup]     Testcase Setup
    write     config
    ${output1}=      read until      Entering configuration mode terminal
    log      ${output1}
    ${data1}=   Run Keyword And Return Status     should not contain      ${command_output}       ${netsim_device_authgroup}
    run keyword if      ${data1}
    ...     Create voice authgroup for netsim device
    ${data2}=   Run Keyword And Return Status     should not contain      ${command_output}       ${real_device_authgroup}
    run keyword if      ${data2}
    ...     Create voice authgroup for real device
    Reading Data From CSV File and Onboard Devices To NSO       ${file_name}
#    [Teardown]      Testcase Teardown

Fetch existing authgroups
#    [Setup]     Testcase Setup
    write   show running-config devices authgroups
    FOR     ${i}    IN RANGE    5
        write    " "
#        ${data}=    read
#        ${result}=  should contain    ${data}    "syntax error: expecting"
#        exit for loop if   ${result}
    END
#    Set Client Configuration       timeout=14
    ${command_output}=      read        delay=20s
    log     ${command_output}
    set suite variable      ${command_output}
#    [Teardown]      Testcase Teardown

Create voice authgroup for netsim device
    write   devices authgroups group ${netsim_device_authgroup} default-map remote-name admin remote-password admin remote-secondary-password admin
    write   commit
    write   exit

Create voice authgroup for real device
    write   devices authgroups group ${real_device_authgroup} default-map remote-name admin remote-password rtpR0bot remote-secondary-password rtpR0bot
    write   commit
    write   exit


Reading Data From CSV File and Onboard Devices To NSO
    [Arguments]     ${file_name}
    ${data}=        OperatingSystem.get file        ${file_name}
    @{LINES}=    Split To Lines    ${data}
    Remove From List    ${LINES}    0
    FOR     ${Line}     IN      @{LINES}
        ${temp}=    remove string     ${Line}     "     \xa0
        @{columns}=     split string    ${temp}     separator=,
        ${device_name}=     get from list    ${columns}     0
        ${ip_address}=      get from list    ${columns}     2
        ${port}=    get from list    ${columns}     3
        ${ned_id}=    get from list    ${columns}     4
        ${authgroup}=    get from list    ${columns}     5
        log to console      ${device_name}: ${ip_address}: ${port}: ${ned_id}: ${authgroup}
        Command to onboard devices to NSO      ${device_name}      ${ip_address}       ${port}     ${ned_id}       ${authgroup}
#        run keyword if      '${authgroup}' == '${netsim_device_authgroup}'
#        ...     Restart netsim device   ${device_name}
    END

Command to onboard devices to NSO
    [Arguments]     ${device_name}      ${ip_address}       ${port}     ${ned_id}       ${authgroup}
    write   devices device ${device_name} address ${ip_address} description ${Device_description} port ${port} authgroup ${authgroup}
    write   device-type cli ned-id ${ned_id}
    write   state admin-state unlocked
    write   commit dry-run
    write   commit
    write   ssh fetch-host-keys
    write   connect
    ${output2}=      read until     info (${Username}) Connected to ${device_name} - ${ip_address}:${port}
    log      ${output2}
    write   sync-from

Restart netsim device
    [Arguments]     ${device_name}
    write   cd netsimautom/
    write   ncs-netsim start ${device_name}
    sleep   5s



Testcase Setup
    open connection     ${NSO_Host}
    login   ${Username}     ${Password}
    write     ncs_cli -C

Testcase Teardown
    close all connections
