from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import datetime

def geoLocationTest():
    mobileEmulation = {'deviceName': 'iPhone 4'}
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('no-sandbox')
    options.add_argument('disable-dev-shm-usage')
    prefs = {"profile.default_content_setting_values.geolocation": 1}
    options.add_experimental_option("prefs", prefs)
    options.add_experimental_option('mobileEmulation', mobileEmulation)
    driver = webdriver.Chrome(executable_path="./chromedriver", options=options)
    driver.execute_cdp_cmd(
        "Browser.grantPermissions",
        {
            "origin": "https://m.amap.com/",
            "permissions": ["geolocation"]
        },
    )
    Map_coordinates = dict({
        "latitude": 99.910066,
        "longitude": 120.560344,
        "accuracy": 100
    })
    driver.execute_cdp_cmd("Emulation.setGeolocationOverride", Map_coordinates)
    driver.get("https://m.amap.com/")
    button = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[6]/div[1]/a'))
        )
    button.click()
    time.sleep(3)
    driver.save_screenshot(f'{datetime.datetime.now():%Y-%m-%d}-geolocation.png')

geoLocationTest()