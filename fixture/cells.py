# coding=utf-8
from selenium.webdriver.common.action_chains import ActionChains
import random



class Cells(object):
    def __init__(self, app):
        self.app = app

    def tapcel(self, points_collection, type_of_point, number_of_bets):

        current_points_list = self.get_points_from_collection(points_collection, type_of_point)

        random_points_no = number_of_bets - len(current_points_list)
        if random_points_no > 0:
            real_points_no = number_of_bets - random_points_no
        else:
            real_points_no = number_of_bets

        for point in range(real_points_no):
            self.press_points_action_bulder(current_points_list[point])

        if random_points_no > 0:
            for point in range(random_points_no):
                self.press_points_action_bulder(random.choice(current_points_list))

    def get_points_from_collection(self, points_collection, type_of_points):
        return points_collection[type_of_points]

    def press_points_action_bulder(self, xy):
        driver = self.app.driver
        bulder = ActionChains(driver)

        table_hover = driver.find_element_by_id("table")
       # table_hover.setAttribute("rect", {'width':100, 'height': 100})
       # table_hover.rect = {'width':100, 'height': 100}

        bulder.move_to_element_with_offset(table_hover, xy[0], xy[1]).click().perform()

    def set_bet_more_max_limit_per_spot(self, point_collection):
       max_per_spot = float(self.app.table.get_max_per_spot())
       selected_chip = float(self.app.chipselector.get_selected_chip_value())

       max_number_of_bets = max_per_spot/selected_chip
       result = round(float(max_number_of_bets))
       self.tapcel(point_collection, "red", result+1)

    def set_bet_more_max_limit_per_table(self, points_collection):
        max_per_table = float(self.app.table.get_max_per_table())
        selected_chip = float(self.app.chipselector.get_selected_chip_value())

        max_number_of_bets = max_per_table / selected_chip
        result = round(float(max_number_of_bets))
        self.tapcel(points_collection, "number", result + 1)