*** Settings ***
Documentation    Suite description
Library     SeleniumLibrary

*** Test Cases ***
Mouse Actions
    open browser    https://swisnl.github.io/jQuery-contextMenu/demo.html   chrome
    maximize browser window

    open context menu   xpath://span[@class="context-menu-one btn btn-neutral"]    #right click action
    sleep   3

    go to   https://testautomationpractice.blogspot.com/
    double click element    xpath://button[contains(text(),'Copy Text')]
    ${text}=    get text  id:field2
    log to console  ${text}
    sleep   3

    go to   https://example.com
    drag and drop   id:box6     id:box106

    close browser




*** Keywords ***
Provided precondition
    Setup system under test