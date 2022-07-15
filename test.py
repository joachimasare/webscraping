from selenium import webdriver
import time
 
driver = webdriver.Chrome('/home/metulburr/chromedriver')
driver.get('https://python-forum.io/Thread-Need-Help-Opening-A-New-Tab-in-Selenium')
# Open a new window
# This does not change focus to the new window for the driver.
driver.execute_script("window.open('');")
time.sleep(3)
# Switch to the new window
driver.switch_to.window(driver.window_handles[1])
driver.get("http://stackoverflow.com")
time.sleep(3)
# close the active tab
driver.close()
time.sleep(3)
# Switch back to the first tab
driver.switch_to.window(driver.window_handles[0])
driver.get("http://google.se")
time.sleep(3)
# Close the only tab, will also close the browser.
driver.close()
