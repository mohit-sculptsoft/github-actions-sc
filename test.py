from selenium import webdriver

def test_example():
    driver = webdriver.Firefox()
    driver.get("https://www.example.com")
    assert driver.title == "Example Domain"
    driver.quit()
