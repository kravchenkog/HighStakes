from data import data_test

class Navigation_helper:

    def __init__(self, app):
        self.app = app

    def home_page(self, urla):
        global restart
        driver = self.app.driver
        driver.delete_all_cookies()
        driver.get(urla)


    def smart_home_page_opening(self, parameters_for_url):

        driver = self.app.driver
        lang = list(parameters_for_url[list(parameters_for_url.keys())[0]].keys())[0]
        currency = list(parameters_for_url[list(parameters_for_url.keys())[0]].values())[0][0]
        regulation_type_id = list(parameters_for_url[list(parameters_for_url.keys())[0]].values())[0][1]


        urla = data_test.get_url(lang, currency, regulation_type_id)
        if driver.current_url != urla:
            self.home_page(urla)
            restart = True
        else:
            restart = False

        return restart