

class Game_button_helper(object):
    def __init__(self, app):
        self.app = app

    def spin_button_is_displayed(self):
        driver = self.app.driver
        if len(driver.find_elements_by_css_selector("button[class='main-button spin-button']")) > 0:
            return True
        else:
            return False

    def spin_press(self):
        driver = self.app.driver
        driver.find_element_by_id("spin_button").click()

    def rebet_button_is_presented(self):
        driver = self.app.driver

        if len(driver.find_elements_by_css_selector("button[class='main-button rebet-button hidden']")) == 0:
            return True
        else:
            return False

    def autoplay_button_is_presented(self):
        driver = self.app.driver

        autoplay_button = driver.find_element_by_id("autoplay_button")
        return autoplay_button.is_displayed()

    def settings_button_is_displayed(self):
        driver = self.app.driver
        settings_button = driver.find_element_by_id("settings_button")
        return settings_button.is_displayed()

    def settings_button_tap(self):
        driver = self.app.driver

        driver.find_element_by_id("settings_button").click()
        self.app.wait.settings_popup_appear()

    def clear_button_is_presented(self):
        driver = self.app.driver

        if len(driver.find_elements_by_css_selector("button[class='main-button remove-bet-button']")) !=0:
            return True
        else:
            return False

    def clear_all_button_is_presented(self):
        driver = self.app.driver
        if len(driver.find_elements_by_css_selector("button[class='main-button clear-button']")) != 0:
            return True
        else:
            return False

    def clear_all_tap(self):
        driver = self.app.driver

        driver.find_element_by_css_selector("button[class='main-button clear-button']").click()

    def clear_tap(self):
        driver = self.app.driver

        driver.find_element_by_css_selector("button[class='main-button remove-bet-button']").click()

    def rebet_button_tap(self):
        driver = self.app.driver

        driver.find_element_by_id("rebet_button").click()
