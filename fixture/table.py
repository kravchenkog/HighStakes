# coding=utf-8
class TableHelper(object):
    def __init__(self, app):
        self.app = app

    def win_popup_appears(self):
        driver = self.app.driver

        return driver.find_element_by_id("win_money_txt").is_displayed()

    def limits_table_presented(self):
        driver = self.app.driver
        return driver.find_element_by_css_selector("div.info-texts-container")\
            .is_displayed()

    def get_list_of_limits(self):
        driver = self.app.driver

        list_of_limits = [0,0]
        list_of_limits[0] =float(driver.find_element_by_css_selector("span#min_value").text)
        list_of_limits[1] =float(driver.find_element_by_css_selector("span#max_value").text)
        return list_of_limits

    def smart_table_to_start_test(self):
        self.close_disconnection_popup()
        self.close_max_per_spot_popup()
        self.check_that_round_ends()
        self.rebet_tap_smart()
        self.clear_all_bets()

    def close_max_per_spot_popup(self):
        if self.popup_is_appeared():
            driver = self.app.driver
            driver.find_element_by_id("btn0").click()


    def check_that_round_ends(self):
        driver = self.app.driver

        if len(driver.find_elements_by_css_selector("button[class='main-button spin-button hidden']")) != 0 and len(driver.find_elements_by_css_selector("button[class='main-button rebet-button hidden']")) != 0:
            self.app.wait.round_ends()

    def rebet_tap_smart(self):
        driver = self.app.driver
        if len(driver.find_elements_by_css_selector("button[class='main-button rebet-button hidden']")) == 0:
            driver.find_element_by_id("rebet_button").click()
            self.app.wait.spin_button_appears()

    def clear_all_bets(self):
        driver = self.app.driver

        if self.app.game_buttons.clear_all_button_is_presented():
            self.app.game_buttons.clear_all_tap()
            return

        elif self.app.game_buttons.clear_button_is_presented():
            self.app.game_buttons.clear_tap()
            return

    def close_disconnection_popup(self):
        driver = self.app.driver
        if len(driver.find_elements_by_css_selector("div.rl_message_body")) != 0:
            if len(driver.find_elements_by_css_selector("input[value='OK']")) != 0:
                driver.find_element_by_css_selector("input[value='OK']").click()
                return

    def get_list_of_bets(self):
        driver = self.app.driver
        all_chip_values = []
        all_chip_elements = driver.find_elements_by_css_selector("div[id='chip_container'] span.chip")
        for chip in all_chip_elements:
            all_chip_values.append(float(chip.find_element_by_css_selector("span").text))

        return all_chip_values

    def get_max_per_spot(self):
        driver = self.app.driver

        return driver.find_element_by_id("max_spot_value").text

    def get_max_per_table(self):

        driver = self.app.driver

        return driver.find_element_by_id("max_value").text

    def popup_is_appeared(self):
        driver = self.app.driver
        if len(driver.find_elements_by_css_selector("div.rl_message_body"))!=0:
            return driver.find_element_by_css_selector("div.rl_message_body").is_displayed()
        else:
            return False

