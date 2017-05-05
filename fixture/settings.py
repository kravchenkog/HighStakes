from time import sleep
from fixture.waiter import Waiters as wait
import re

class GameSettings(object):
    def __init__(self, app):
        self.app = app


    def save_button_tap(self):
        driver = self.app.driver

        driver.find_element_by_id("save_settings").click()


    def smart_settings_popup_closed(self, restart):
        dr = self.app.driver

        if not restart and self.settings_popup_is_opened():
            self.save_button_tap()
        elif restart:
            wait.loader_not_presented(self)
            wait.settings_button_presented(self)

            if self.settings_popup_is_opened():
                wait.settings_popup_appear(self)

                self.save_button_tap()

            else:
                timer = range(15)
                for time in timer:
                    sleep(0.1)
                    if self.settings_popup_is_opened():
                        self.save_button_tap()
                    else:
                        return


    def preloader_wrapper_displayed(self):
        dr = self.app.driver

        if len(dr.driver.find_element_by_id("preloader_wrapper")) == 0:
            return False
        else:
            return True

    def settings_popup_is_opened(self):
        dr= self.app.driver
        len_of_popup = len(dr.find_elements_by_css_selector("div[class='settings-popup-container']"))
        if len_of_popup > 0:
            return True
        else:
            return False

    def select_limit_and_save_value(self, type_of_limit):
        driver = self.app.driver
        all_limits = []
        self.app.game_buttons.settings_button_tap()
        all_limits_str = self.get_list_of_limits_values()
        for limit in all_limits_str:
            all_limits.append(self.get_correct_value(limit))

        self.select_limit(type_of_limit)
        self.save_button_tap()
        self.app.wait.settings_popup_closed()

        return all_limits[type_of_limit]

    def get_correct_value(self, limit):

        d_limit = [0,0]
        for l in range(2):
            digits_only = re.sub("[^\d]", "", limit[l])
            without_dot = digits_only[0:-2]
            element = without_dot + ".00"
            d_limit[l] = float(element)
        return d_limit

    def select_limit(self, type_of_limit):
        list_of_limits = self.get_list_of_limits()
        list_of_limits[type_of_limit].click()

    def get_list_of_limits(self):
        driver = self.app.driver
        limit_list = []
        limit_list.append(driver.find_element_by_css_selector("label[for='limit_low']"))
        limit_list.append(driver.find_element_by_css_selector("label[for='limit_norm']"))
        limit_list.append(driver.find_element_by_css_selector("label[for='limit_high']"))

        return limit_list

    def get_list_of_limits_values(self):
        driver = self.app.driver
        limits = []

        limits.append([driver.find_element_by_css_selector
                      ("label[for='limit_low'] span[data-name='minLimit']").text,
                       driver.find_element_by_css_selector
                      ("label[for='limit_low'] span[data-name='maxLimit']").text])
        limits.append([driver.find_element_by_css_selector
                       ("label[for='limit_norm'] span[data-name='minLimit']").text,
                       driver.find_element_by_css_selector
                       ("label[for='limit_norm'] span[data-name='maxLimit']").text])
        limits.append([driver.find_element_by_css_selector
                       ("label[for='limit_high'] span[data-name='minLimit']").text,
                       driver.find_element_by_css_selector
                       ("label[for='limit_high'] span[data-name='maxLimit']").text])

        return limits
        #driver.FindElement(By.CssSelector("label[for='limit_low'] span[data-name='minLimit']")).Text;