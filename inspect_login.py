from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

path = ChromeDriverManager().install()
service = Service(path)
driver = webdriver.Chrome(service=service)
try:
    driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    wait = WebDriverWait(driver, 20)
    wait.until(EC.presence_of_element_located((By.NAME, 'username')))
    wait.until(EC.presence_of_element_located((By.NAME, 'password')))
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type=submit]')))
    username = driver.find_element(By.NAME, 'username')
    password = driver.find_element(By.NAME, 'password')
    button = driver.find_element(By.CSS_SELECTOR, 'button[type=submit]')
    print('username input visible:', username.is_displayed(), 'password input visible:', password.is_displayed())
    print('button visible:', button.is_displayed(), 'button text:', button.text)
    username.send_keys('Admin')
    password.send_keys('admin')
    button.click()
    time.sleep(8)
    print('TITLE:', driver.title)
    print('URL:', driver.current_url)
    body = driver.find_element(By.TAG_NAME, 'body').text
    print('BODY TEXT START:')
    print(body[:1000])
    elems = driver.find_elements(By.XPATH, "//span[contains(text(),'Welcome') or contains(text(),'Admin') or contains(text(),'Dashboard')]")
    print('MATCHES:', len(elems))
    print([e.text for e in elems])
except Exception as e:
    print('ERROR:', type(e).__name__, e)
finally:
    driver.quit()
