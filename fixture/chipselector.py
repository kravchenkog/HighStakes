# coding=utf-8

class Chipselector(object):
    def __init__(self, app):
        self.app = app

    def selectchip(self, number_of_chip):

        list_of_chips = self.get_list_of_chips()
        list_of_chips[number_of_chip].click()

    def get_list_of_chips(self):
        driver = self.app.driver

        return driver.find_elements_by_css_selector("span.chip")

    def chips_are_displayed(self):
        driver = self.app.driver
        if len(driver.find_elements_by_css_selector("div#chip-selector span.chip")) >=0:
            return True
        else:
            return False

    def get_list_of_chips_values(self):
        elements = []
        chips = self.get_list_of_chips()
        for chip in chips:
            elements.append(int(chip.get_attribute('innerText')))
        return elements

    def get_selected_chip_value(self):
        driver = self.app.driver

        return driver.find_element_by_css_selector("span.selected span").text