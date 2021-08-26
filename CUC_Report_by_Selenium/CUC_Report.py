# -*- coding: utf-8 -*-

import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import logging
import json
import time

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


def main():
    mobile_emulation = {'deviceName': 'iPhone 4'}
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('no-sandbox')
    options.add_argument('disable-dev-shm-usage')
    options.add_experimental_option('mobileEmulation', mobile_emulation)
    driver = webdriver.Chrome(service=Service("./chromedriver"), options=options)
    driver.set_window_size(320, 680)
    driver.execute_cdp_cmd(
        "Browser.grantPermissions",
        {
            "origin": "https://www.jiandaoyun.com/",
            "permissions": ["geolocation"]
        },
    )
    map_coordinates = dict({
        "latitude": 39.909000,
        "longitude": 116.554600,
        "accuracy": 1
    })
    driver.execute_cdp_cmd("Emulation.setGeolocationOverride", map_coordinates)
    try:
        driver.get('https://www.jiandaoyun.com/dashboard#')
        f1 = open('c.txt')
        cookie = f1.read()
        cookie = json.loads(cookie)
        for c in cookie:
            try:
                c.pop('sameSite')
            except:
                pass
            driver.add_cookie(c)
        driver.refresh()
        xsgzb_button = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[2]/div[2]/div[2]'))
        )
        xsgzb_button.click()
        xsmrxxtb = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div[2]/div/div[2]'))
        )
        xsmrxxtb.click()
        # 手机号码
        phone_number = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH,
                                            '//*[@id="root"]/div/div/div/div[1]/div/div[5]/div[2]/div[1]/div'))
        )
        phone_number.send_keys("17360077007")
        # 生源所在地
        syszd_click = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH,
                                            '//*[@id="root"]/div/div/div/div[1]/div/div[6]/div[2]/div/div/div[1]'))
        )
        syszd_click.click()  # syszd_click
        syszd_select_l = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH,
                                            '/html/body/div[3]/div/div[2]/div[1]/div'))
        )
        syszd_select_m = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH,
                                            '/html/body/div[3]/div/div[2]/div[2]/div'))
        )
        syszd_select_r = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH,
                                            '/html/body/div[3]/div/div[2]/div[3]/div'))
        )
        webdriver.ActionChains(driver).drag_and_drop_by_offset(syszd_select_l, 0, -350).perform()
        webdriver.ActionChains(driver).drag_and_drop_by_offset(syszd_select_l, 0, -350).perform()
        webdriver.ActionChains(driver).drag_and_drop_by_offset(syszd_select_l, 0, -335).perform()
        webdriver.ActionChains(driver).drag_and_drop_by_offset(syszd_select_m, 0, -270).perform()
        webdriver.ActionChains(driver).drag_and_drop_by_offset(syszd_select_r, 0, -90).perform()
        time.sleep(1)
        syszd_qd_click = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH,
                                            '/html/body/div[3]/div/div[1]/div[2]/div'))
        )
        syszd_qd_click.click()  # syszd_qd_click
        syszd_xxdz = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH,
                                            '//*[@id="root"]/div/div/div/div[1]/div/div[6]/div[2]/div/div/div[2]/div'))
        )
        syszd_xxdz.send_keys("*********")  # syszd_xxdz
        driver.save_screenshot(f'{datetime.datetime.now():%Y-%m-%d}-1.png')
        # 目前所在地
        mqszd = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH,
                                            '//*[@id="root"]/div/div/div/div[1]/div/div[9]/div[2]/div/div/div[1]'))
        )
        mqszd.click()  # mqszd
        # 目前所在地详细地址
        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, '//*[@class="map-container amap-container"]/iframe'))  # gaodedw
        )  # wait for amap api loaded
        mqszdxxdz_click = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH,
                                            '//*[@id="root"]/div/div/div/div[1]/div/div[10]/div[2]/div/div/div[1]'))
        )
        mqszdxxdz_click.click()
        mqszdxxdz_select_l = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[2]/div[1]/div'))
        )
        mqszdxxdz_select_m = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[2]/div[2]/div'))
        )
        mqszdxxdz_select_r = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[2]/div[3]/div'))
        )
        webdriver.ActionChains(driver).drag_and_drop_by_offset(mqszdxxdz_select_l, 0, -45).perform()
        webdriver.ActionChains(driver).drag_and_drop_by_offset(mqszdxxdz_select_m, 0, -45).perform()
        webdriver.ActionChains(driver).drag_and_drop_by_offset(mqszdxxdz_select_r, 0, -135).perform()
        time.sleep(1)
        mqszdxxdz_qd_click = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[1]/div[2]/div'))
        )
        mqszdxxdz_qd_click.click()  # mqszdxxdz_qd_click
        mqszd_xxdz = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH,
                                            '//*[@id="root"]/div/div/div/div[1]/div/div[10]/div[2]/div/div/div[2]/div'))
        )
        mqszd_xxdz.send_keys("*********")  # mqszd_xxdz
        driver.save_screenshot(f'{datetime.datetime.now():%Y-%m-%d}-2.png')
        # 该区域是否为中高风险区
        gqysfwzgfxq = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH,
                                            '//*[@id="root"]/div/div/div/div[1]/div/div[12]/div[2]/div/div/div[1]'))
        )
        gqysfwzgfxq.click()  # gqysfwzgfxq
        # 以上“目前所在地”勾选选项较昨日是否有变化
        ysmqszdgxxxjzrsfybh = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH,
                                            '//*[@id="root"]/div/div/div/div[1]/div/div[13]/div[2]/div/div/div[2]'))
        )
        ysmqszdgxxxjzrsfybh.click()  # ysmqszdgxxxjzrsfybh
        driver.save_screenshot(f'{datetime.datetime.now():%Y-%m-%d}-3.png')
        tw_morning = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH,
                                            '//*[@id="root"]/div/div/div/div[1]/div/div[15]/div[3]/div/div[1]/div[2]/div/div[2]/div/div[1]'))
        )
        tw_morning.send_keys("35.6")  # tw_morning
        tw_afternoon = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH,
                                            '//*[@id="root"]/div/div/div/div[1]/div/div[15]/div[3]/div/div[1]/div[3]/div/div[2]/div/div'))
        )
        tw_afternoon.send_keys("35.5")  # tw_afternoon
        tw_night = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH,
                                            '//*[@id="root"]/div/div/div/div[1]/div/div[15]/div[3]/div/div[1]/div[4]/div/div[2]/div/div'))
        )
        tw_night.send_keys("35.6")  # tw_night
        driver.save_screenshot(f'{datetime.datetime.now():%Y-%m-%d}-4.png')
        tijiao = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div/div[3]/div/div'))
        )
        tijiao.click()  # tijiao
        # time.sleep(5)
        driver.implicitly_wait(10)
        driver.save_screenshot(f'{datetime.datetime.now():%Y-%m-%d}-5.png')
    except Exception as e:
        logging.warning(e)
    finally:
        driver.close()
        driver.quit()


if __name__ == "__main__":
    main()
