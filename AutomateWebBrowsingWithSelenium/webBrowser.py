from selenium import webdriver

driver = webdriver.Chrome('chromedriver')
driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

messageField = driver.find_element_by_xpath('//*[@id="user-message"]')
messageField.send_keys('Its me Eyakub')

showMessageButton = driver.find_element_by_xpath('//*[@id="get-input"]/button')
showMessageButton.click()

addA = driver.find_element_by_xpath('//*[@id="sum1"]')
addA.send_keys('11')
addB = driver.find_element_by_xpath('//*[@id="sum2"]')
addB.send_keys('10')
addResult = driver.find_element_by_xpath('//*[@id="gettotal"]/button')
addResult.click()

closePopup = driver.find_element_by_xpath('//*[@id="at-cv-lightbox-close"]')
closePopup.click()