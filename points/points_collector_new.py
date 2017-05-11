# coding=utf-8
from selenium import webdriver

class CellCollector():
    def __init__(self, app):
        self.app = app
    def get_location(self, range_start, range_stop):
        driver = self.app.driver

        range_for_number = range(range_start, range_stop+1)
        all_elements =  []
        for num in range_for_number:
            all_elements.append(driver.find_element_by_css_selector("div[id='table_cells'] span[id='cell_"+str(num)+"']"))

        all_locations = []
        for loc in all_elements:
            all_locations.append(loc.location)

        list_of_locations = self.conver_to_list_and_add_offset(all_locations)

        return list_of_locations

    def conver_to_list_and_add_offset(self, all_location):
        locations = []
        offset = {"x": 226, "y": 67}
        for element in all_location:
            locations.append([element['x']-offset["x"], element['y']-offset["y"]])
        return locations

    def get_points_collection(self):
        all_points = {}
        all_points["number"] = []
        all_points["number"] = self.get_location(2, 38)
        print("sddd")