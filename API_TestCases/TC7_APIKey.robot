*** Settings ***
Documentation    Suite description
Library     RequestsLibrary
Library     Collections


*** Variables ***
${base_url}     https://maps.googleapis.com
${request_url}      /maps/api/place/nearbysearch/json
${YOUR_API_KEY}     AIzaSyBWAxi_wr02rANmR4RKnKC2Wm2Ks_9b2Vk

*** Test Cases ***
Google maps places API
    create session      mysession       ${base_url}
    ${params}=   create dictionary   location=-33.8670522,151.1957362        radius=500      types=food      name=harbour    key=${YOUR_API_KEY}
    ${response}=    get on session      mysession   ${request_url}      params=${params}
    log to console      ${response.content}
