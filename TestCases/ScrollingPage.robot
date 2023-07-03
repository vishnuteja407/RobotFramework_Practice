*** Settings ***
Documentation    Suite description
Library     SeleniumLibrary

*** Test Cases ***
Scrolling Test
    open browser    https://10.122.32.51:9091/#/login   chrome
    sleep   60
    maximize browser window
    input text      xpath://input[@id='username']       admin
    input text      xpath://mdl-textfield[@id='password']       admin
    click button    xpath://button[@id="loginButton"]
    sleep       20
    click link      xpath://body/app-root[1]/div[1]/app-home[1]/div[1]/div[1]/mdl-card[1]/mdl-card-supporting-text[1]/div[2]/div[26]/div[1]/h5[1]
    sleep       20
    click link      //a[@id='item1']
    sleep   20
    set selenium speed  3 seconds
#    execute javascript   window.scrollTo(0, 2500)
#
#    scroll element into view    xpath://*[@id="content"]/div[2]/div[2]/table[1]/tbody/tr[86]/td[1]/img
#
#    execute javascript  window.scrollTo(0, document.body.scrollHeight)
#
#    execute javascript  window.scrollTo(0, document.body.scrollHeight)

#    scroll element into view    xpath://td[contains(text(),'Madagascar')]
    execute javascript   window.scrollTo(0, 20)
    close browser



