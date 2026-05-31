from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://google.com")

input("Press Enter to close...")
driver.quit()