*** Settings ***
Documentation    Suite description
Library     BuiltIn
Library     String
Library     OperatingSystem
Library     Collections
Variables   ../Testdata/setup-details.yaml

*** Test Cases ***
Parsing YAML File
    FOR    ${dev}    IN    @{netsim_devices.devices}
        log to console      ${dev['device']}
    END
*** Keywords ***
log data
    log to console      @{netsim_devices}
