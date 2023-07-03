*** Settings ***
Documentation    Service catalog order form
Library     SeleniumLibrary
Library     BuiltIn

Suite Setup    Login to BPA
Suite Teardown      Close browser

*** Variables ***
${BPA_URL}  https://10.122.32.87:9091/#/
${BPA_USERNAME}     admin
${BPA_PASSWORD}     admin
${CEWA_Service_Item}    COMMON SERVICE CEWA V1.5.0
${Invalid_BLC_Code}      Test_123
${Valid_BLC_Code}      MA1-225
${BROWSER}        chrome
${NSER}   12345678
${CRQ}    CRQ123456789012
${Work_Order_Number}    0000012345678
${Custom_Note}   CEWA UI
${Snapshot_Name}   CEWA
${Order_Type}     CEWA
${Wait}             1
${Wait_3Sec}        3
${Wait_5Sec}        5
${Wait_8Sec}        8
${Wait_2Sec}        2
${Wait_10Sec}       10
${Wait_20Sec}       20
${Wait_15Sec}       15
${Wait_30Sec}       30
${Wait_45Sec}       45
${DOWNLOAD_DIR}    /tmp/browser-downloads
${CEWA_Input_CSV}      ${CURDIR}/common-service-cewa.csv

*** Test Cases ***
Service Catalog Order Form
    Check BPA UI Version
    Click On Service Catalog
    Fill CEWA Service Order Input Form

*** Keywords ***
Login to BPA
    open browser    ${BPA_URL}      ${BROWSER}
    maximize browser window
    ${passed}=    Run Keyword And Return Status    Page Should Contain Element    xpath://button[@id='details-button']
    Run keyword if     ${passed}
    ...     Ignore and proceed
    wait until page contains element    xpath://button[@id='loginButton']       timeout=3000
    Wait Until Element Is Not Visible    //div[@class='loading-icon']       timeout=1800
#    click element   xpath://mdl-textfield[@id='username']
    input text   xpath://input[@id='username']       ${BPA_USERNAME}
#    click element   xpath://input[@id='password']
    input text   xpath://input[@id='password']      ${BPA_PASSWORD}
    click button   xpath://button[@id='loginButton']

Click On Service Catalog
    Sleep   ${Wait}
    Click Element    xpath://*[@id="app-servicecatalog"]
    Wait Until Element Is Not Visible    //div[@class='loading-icon']       timeout=1800


Fill CEWA Service Order Input Form
    Sleep   ${Wait_8Sec}
    Input Text  xpath=//input[@id='searchGrid']     ${CEWA_Service_Item}
    Wait Until Element Is Visible         //button[@id='Common Service CEWA v1.5.0']        timeout=1800
    Sleep   ${Wait_8Sec}
    Click Button   xpath=//button[@id='Common Service CEWA v1.5.0']
    Capture Page Screenshot
    Wait Until Element Is Visible         //div[contains(text(),'Search Devices By BLC/Site')]        timeout=1800
    input text   xpath://input[@id='nser']       ${NSER}
    Sleep  ${Wait}
    input text   xpath://input[@id='crq']       ${CRQ}
    Sleep  ${Wait}
    input text   xpath://input[@id='workorderNumber']       ${Work_Order_Number}
    Sleep  ${Wait}
    Capture Page Screenshot
    Click Element   xpath://span[contains(text(),'Type *')]
    Capture Page Screenshot
    Click Element   xpath://span[@id='${Order_Type}']
    input text   xpath://input[@id='pid']       ${Custom_Note}
    Sleep  ${Wait}
    input text   xpath://input[@id='snapshotName']       ${Snapshot_Name}
    Sleep  ${Wait}
    Add Devices By BLC Code
    Upload A File

Add Devices By BLC Code
    Click Element   xpath://*[contains(text(),'Search Devices By BLC')]
    Click Element   xpath://*[@id='blc']
    Input Text   XPath=//*[@id="blc"]           ${Invalid_BLC_Code}
    Click Element   xpath://fieldset[@formgroupname='infoFormGroup']
    Sleep   ${Wait}
    Capture Page Screenshot
    Input Text   XPath=//*[@id="blc"]           ${Valid_BLC_Code}
    Click Element   xpath://*[@id='blc']
    Press Keys  id=blc  RETURN
    Wait Until Element Is Not Visible    //div[@class='loading-icon ng-star-inserted']    timeout=1500
    Click Element   xpath://span[contains(text(),'Add All Hostnames')]
    Capture Page Screenshot
    Element Should Be Enabled   //button[@id='order_btn']
    Click Element   xpath://button[contains(text(),'Delete All')]
    Wait Until Element Is Visible         //button[@id='okButton']        timeout=1500
    Click Element   xpath://button[@id='okButton']
    Sleep   ${Wait}
    # Element Should Be Visible    //*[@id='order_btn' and not(contains(@class, 'disabled'))]
    Element Should Be Disabled   //button[@id='order_btn']
    Capture Page Screenshot

Upload A File
    Sleep  ${Wait}
    Click Element   xpath://*[contains(text(),'Device List Bulk Upload')]
    Sleep  ${Wait}
    Choose File        id=cewaFile            ${CEWA_Input_CSV}
    Sleep  ${Wait}
    Capture Page Screenshot
    Click Element   xpath://button[contains(text(),'Upload')]
    Capture Page Screenshot
    Scroll Element Into View    //button[@id='order_btn']
    Capture Page Screenshot
    Element Should Be Enabled   //button[@id='order_btn']

Ignore and proceed
    click button    xpath://button[@id='details-button']
    click link      xpath://a[@id="proceed-link"]

Check BPA UI Version
    Log to Console    Capturing BPA Build Version
    Sleep   ${Wait_10Sec}
    Click Element   xpath://*[@id="openAboutDialogue"]
    Sleep   ${Wait_5Sec}
    Capture Page Screenshot
    Sleep   ${Wait}
    Click Element   xpath://*[@id="aboutCloseDialog"]/mdl-icon
    Sleep   ${Wait}