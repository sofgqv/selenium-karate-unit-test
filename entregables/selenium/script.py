from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def test_eight_components():
    driver = webdriver.Chrome()

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    #driver.get("https://www.selenium.dev/selenium/web/web-form.html")
    driver.get("http://localhost:3000")

    title = driver.title
    assert title == "Web form"

    driver.implicitly_wait(0.5)

    text_box = driver.find_element(by=By.NAME, value="my-text")
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

    text_box.send_keys("Selenium")
    submit_button.click()

    message = driver.find_element(by=By.ID, value="message")
    value = message.text
    assert value == "Received!"

    driver.save_screenshot("screenshot.png")

    driver.quit()


#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#driver.get("http://localhost:3000")

# TESTEAR ingresar un valor a una caja de texto del miembro que le corresponda. 

#driver.save_screenshot("screenshot.png")

#driver.quit()

# python3 -m pip install urllib3==1.26.6