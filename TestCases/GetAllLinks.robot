*** Settings ***
Documentation    Suite description
Library    SeleniumLibrary

*** Test Cases ***
Get all links test
    open browser    https://www.selenium.dev/   chrome
    maximize browser window
    ${linksCount}=  get element count   xpath://a
    log to console   ${linksCount}
    ${pageTitle}=    log title
    log to console      ${pageTitle}

    @{linkItems}    create list
    FOR     ${i}    IN RANGE    1   ${linksCount}+1
        ${linkText}=    get text    xpath:(//a)[${i}]
        log to console  ${linkText}
    END
    close browser


*** Keywords ***
