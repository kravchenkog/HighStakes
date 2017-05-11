from selenium import webdriver
from fixture.game_buttons import Game_button_helper
from fixture.navigation import Navigation_helper
from fixture.settings import GameSettings
from fixture.waiter import Waiters
from fixture.chipselector import Chipselector
from fixture.cells import Cells
from points.points_collector_new import CellCollector
from fixture.table import TableHelper



class AppManager:

    def __init__(self, browser):


        if browser=="firefox":
            self.driver = webdriver.Firefox(capabilities={"marionette": False})
            #self.driver = webdriver.Firefox()

        elif browser == "chrome":
            self.driver = webdriver.Chrome()

        else:
            "incorrect browser"
        self.driver.set_window_size(1024, 768)
        self.driver.implicitly_wait(0.5)
        self.game_buttons = Game_button_helper(self)
        self.navigator = Navigation_helper(self)
        self.settings = GameSettings(self)
        self.wait = Waiters(self)
        self.chipselector = Chipselector(self)
        self.cells = Cells(self)
        self.table = TableHelper(self)
        self.cell_new = CellCollector(self)

    def destroy(self):
        self.driver.quit()

    def is_valid(self):
        try:
            self.driver.current_url
            return True
        except:
            return False


    def correct_browser(self, browser):

        global browser_type
        if browser == browser_type:
            return True
        else:
            return False