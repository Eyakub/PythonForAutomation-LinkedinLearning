from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome('chromedriver')
driver.maximize_window()
driver.get('http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')

source = driver.find_element_by_xpath('//*[@id="box3"]')
des = driver.find_element_by_xpath('//*[@id="box106"]')

actions = ActionChains(driver)
actions.drag_and_drop(source, des).perform()