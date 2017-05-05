from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Waiters:
    def __init__(self, app):
        self.app = app

    def settings_popup_appear(self):

        driver = self.app.driver

       # WebDriverWait(driver, 10).until(EC.element_to_be_clickable(By.CSS_SELECTOR("div[class='settings-popup-container']")))
        i = range(100)
        for time in i:
            if len(driver.find_elements_by_css_selector("div[class='settings-popup-container']")) >0:
                return
            else:
                sleep(0.1)
        sleep(1)


    def loader_not_presented(self):
        driver = self.app.driver

        for time in range(50):
            sleep(0.1)
            if len(driver.find_elements_by_css_selector("div[id='preloader']")) != 0:
                break
        for time in range(50):
            sleep(0.1)
            if len(driver.find_elements_by_css_selector("div[id='preloader']")) == 0:
                break
        # WebDriverWait(driver, 5).until(
        #     EC.visibility_of_element_located((By.CSS_SELECTOR, "div[id='preloader']")))
        # WebDriverWait(driver, 5).until_not(
        #     EC.visibility_of_element_located((By.CSS_SELECTOR, "div[id='preloader']")))

    def settings_button_displayed(self):
        driver = self.app.driver

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div[id='settings_button']")))

    def settings_button_presented(self):
        driver = self.app.driver

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "settings_button")))

    def round_ends(self):
        driver = self.app.driver

        for time in range(100):
            if len(driver.find_elements_by_css_selector("div[class='doll start']")) == 0:
                sleep(0.02)

            else:
                break

        for time in range(100):
            if len(driver.find_elements_by_css_selector("div[class='doll']")) == 0:
                sleep(0.07)

            else:
                break

        '''WebDriverWait(driver, 2).until(
            EC.presence_of_element_located(By.CSS_SELECTOR("div[class='doll start']")))
        WebDriverWait(driver, 7).until(
            EC.presence_of_element_located(By.CSS_SELECTOR("div[class='doll']")))'''
        print("stop")
    def settings_popup_closed(self):
        driver = self.app.driver

        for time in range(100):
            if len(driver.find_elements_by_css_selector("div[class='settings-popup-container hidden']"))== 0:
                sleep(0.01)
            else:
                return

    def spin_button_appears(self):
        driver = self.app.driver
        timer = range(100)
        for time in timer:
            if len(driver.find_elements_by_css_selector("button[class='main-button spin-button']")) ==0:
                sleep(0.02)
            else:
                return
