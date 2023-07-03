*** Settings ***
Documentation    Suite description
Library     SeleniumLibrary


*** Variables ***

@{data}    63ea3a698edb750037d0a2db    63ea3b1486ff52003d072f76    63ea3a698edb750037d0a2da    63ea3b1486ff52003d072f74       63ea3a698edb750037d0a2d9    63ea3b1486ff52003d072f75
${rules}
*** Test Cases ***

For loop1
    Log to console   ${data}
    ${cnt}=     Get length      ${data}
    FOR   ${i}    IN RANGE    0   ${cnt}
    Set Test Variable     ${devices${i}}     ${data}[${i}]
    END
    Log to console    ${devices0}
    Log to console    ${devices1}
    Log to console    ${devices2}
    Log to console    ${devices3}
    Log to console    ${devices4}
    Log to console    ${devices5}



#For Loop2
#    FOR     ${i}    IN      123456789
#        LOG TO CONSOLE  ${i}
#    END
#
#For Loop3
#    FOR     ${i}    IN      1 2 3 4 5 6  7 8 9
#        LOG TO CONSOLE  ${i}
#    END
#
#For Loop4
#    FOR  ${i}    IN      1   2   3   4   5   6   7   8   9
#        LOG TO CONSOLE  ${i}
#    END
#
#For loop5
#    @{items}    create list     10   20   30   40   5   6   7   8
#    FOR     ${i}    IN  @{items}
#        LOG TO CONSOLE  ${i}
#    END
#
#For loop6
#    FOR     ${i}    IN  JOHN    DAVID   SMITH  SCOT
#        LOG TO CONSOLE  ${i}
#    END
#
#For loop7 with exit
#    @{items}    create list     10   20   30   40   55   66   77   88
#    FOR     ${i}    IN  @{items}
#        continue for loop if    ${i}==10
#        LOG TO CONSOLE  ${i}
#        exit for loop if    ${i}==30
#    END
*** Keywords ***
