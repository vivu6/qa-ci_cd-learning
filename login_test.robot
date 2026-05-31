***Settings***
Library    SeleniumLibrary
Library    XML
Library    OperatingSystem
Library    browser_driver.py

*** Test Cases ***
Login With Valid Credentials
    ${CHROMEDRIVER}=    Get Chrome Driver
    Open Browser    https://opensource-demo.orangehrmlive.com/web/index.php/auth/login    chrome    executable_path=${CHROMEDRIVER}
    Sleep    2s
    Input Text    xpath=//input[@placeholder='Username']    Admin
    Input Text    xpath=//input[@placeholder='Password']    admin123
    Click Button    xpath=//button[normalize-space()='Login']
    sleep    1s
    Wait Until Page Contains Element    xpath=//h6[normalize-space()='Dashboard']
    #Close Browser

