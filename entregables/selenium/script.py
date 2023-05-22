from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://localhost:3000")

# TESTEAR ingresar un valor a una caja de texto del miembro que le corresponda. 

#driver.save_screenshot("screenshot.png")

#driver.quit()

# python3 -m pip install urllib3==1.26.6