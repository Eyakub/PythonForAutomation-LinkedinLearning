from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome('chromedriver')
url = 'https://www.google.com/earth/'
driver.get(url)
wait = WebDriverWait(driver, 10) # wait 10 sec

launchEarthButton = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/header/div/nav[1]/ul[2]/li[2]/a/span/span')))
launchEarthButton.click()