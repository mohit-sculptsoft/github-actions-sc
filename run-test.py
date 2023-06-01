from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
import time

# Create a new Firefox driver
driver = webdriver.Firefox(service=GeckoDriverManager().install())


# Open the test file
driver.get("./testing.side")

# Wait for the page to load
time.sleep(3)

# Run the test
driver.find_element_by_id("edit-1-1").click()

# Wait for the test to complete
time.sleep(5)

# Close the browser
driver.quit()
