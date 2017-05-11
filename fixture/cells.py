# coding=utf-8
from selenium.webdriver.common.action_chains import ActionChains
import random



class Cells(object):
    def __init__(self, app):
        self.app = app

    def tapcel(self, points_collection, type_of_point, number_of_bets):

        current_points_list = []
        for points in self.get_points_from_collection(points_collection, type_of_point):
            current_points_list.append(points)

        # random_points_no = number_of_bets - len(current_points_list)
        # if random_points_no > 0:
        #     real_points_no = number_of_bets - random_points_no
        # else:
        #     real_points_no = number_of_bets

        counre = -1
        for point in range(int(number_of_bets)):
            counre+=1
            if counre > len(current_points_list)-1:
                counre = 0
            self.press_points_action_bulder(current_points_list[counre])

        # if random_points_no > 0:
        #     for point in range(random_points_no):
        #         self.press_points_action_bulder(random.choice(current_points_list))

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
        del(points_collection['red'])
        limits = {'number': 500, 'pair': 1000, 'three': 1500, 'four': 2000, 'six': 2500, 'column': 3000,
                  'dozer':3000, 'blackred':5000, 'even_odd': 5000, 'low_high': 5000}


        max_per_table = float(self.app.table.get_max_per_table())
        selected_chip = float(self.app.chipselector.get_selected_chip_value())

        max_number_of_bets = max_per_table / selected_chip
        counter = 0
        for point_key in points_collection.keys():

            to_one = limits[point_key]/selected_chip
            fuckin_list = points_collection[point_key]
            list_a =[]
            for good_list in fuckin_list:
                list_a.append(good_list)

            max_number = len(list_a)*to_one
            counter = counter+max_number

            if counter > max_number_of_bets:
                max_number = counter- max_number_of_bets

            self.tapcel(points_collection, point_key, max_number)

