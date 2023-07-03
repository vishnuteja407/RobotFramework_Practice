*** Settings ***
Documentation    Suite description
Library     SeleniumLibrary
Library     BuiltIn

Suite Setup    Login to BPA
Suite Teardown      Close browser

*** Variables ***
${BPA_URL}  https://bpa-mavericks4.cisco.com/#/login
${BPA_USERNAME}     admin
${BPA_PASSWORD}     admin



*** Test Cases ***
Goto Admin tab

*** Keywords ***
Login to BPA
    open browser    ${BPA_URL}      chrome
    maximize browser window
    ${passed}=    Run Keyword And Return Status    Page Should Contain Element    xpath://button[@id='details-button']
    Run keyword if     ${passed}
    ...     Ignore and proceed
    wait until page contains element    xpath://button[@id='loginButton']       timeout=3000
#    click element   xpath://mdl-textfield[@id='username']
    input text   xpath://mdl-textfield[@id='username']       ${BPA_USERNAME}
#    click element   xpath://input[@id='password']
    input text   xpath://input[@id='password']      ${BPA_PASSWORD}


Ignore and proceed
    click button    xpath://button[@id='details-button']
    click link      xpath://a[@id="proceed-link"]

Goto Admin tab
    click button    xpath://mat-icon[contains(text(),'person')]
    click link      xpath://button[@id='goToAdmin']

Remedy Settings
    click element   xpath://img[@id='cisco-bpa-platform_ui-admin_admin_settingsIcon']
    click element   xpath://mat-tab-header/div[3]
    click element   xpath://mat-tab-header/div[3]
#    execute javascript   window.scrollTo(2500, 0)
    click element   xpath://span[@id='scPrefixTabName3']



