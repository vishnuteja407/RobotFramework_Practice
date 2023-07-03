*** Settings ***
Documentation    Suite description
Library     XML
Library     os
Library     Collections
Library     RequestsLibrary

*** Variables ***
${base_url}     http://thomas-bayer.com


*** Test Cases ***
Test case1
    ${xml_obj}=     parse xml       ../Testdata/sample-data.xml
    ${artist_name}=     get element text    ${xml_obj}  .//CDS/CD[1]/ARTIST
    should be equal     ${artist_name}      Bob Dylan

    ${artist_name}=     get element    ${xml_obj}  .//CDS/CD[1]/ARTIST
    should be equal     ${artist_name.text}      Bob Dylan

    element text should be      ${xml_obj}      Bob Dylan   .//CDS/CD[1]/ARTIST

    ${count}=   get element count   ${xml_obj}      .//CDS/CD
    should be equal     ${count}    ${5}
    should be equal as integers     ${count}    5

    #check attribute presence
    element attribute should be     ${xml_obj}      id      asc5    .//CDS/CD[5]

    ${elements}=    get child elements      ${xml_obj}   .//CDS/CD[5]
#    log to console      ${elements}
    should not be empty     ${elements}
    ${title}=   get element text    ${elements[0]}
    log to console  ${title}


Test case 2
    create session  mysession   ${base_url}
    ${response}=   Get on session       mysession       /sqlrest/CUSTOMER/15
    ${xml_obj}=     convert to string   ${response.content}
    ${xml}=   parse xml    ${xml_obj}
    log to console      ${xml}
    element text should be      ${xml}      Bill      .//FIRSTNAME

    ${child_elements}=  get child elements      ${xml}
    should not be empty     ${child_elements}
    ${lname}=   get element text    ${child_elements[2]}
    log to console  ${lname}
    should be equal     ${lname}    Clancy
#    element text should be      ${child_elements[2]}      Clancy      .//LASTNAME
    ${city}=   get element text    ${child_elements[4]}
    log to console  ${city}
    should be equal     ${city}    Seattle
#    element text should be      ${child_elements[4]}      Seattle      .//CITY


