import os
import pytest
fixture = None
from fixture.app_manager import AppManager
from data.data_test import testdata


browser_value = None
restart = False


testdata = [{'firefox': {'eng': ['USD', 255]}}]

@pytest.fixture(scope='module', params=testdata, ids=[str(x) for x in testdata])
def app(request):
    global browser_value
    global fixture
    current_param = request.param
    current_browser = list(current_param.keys())[0]
    path_to_target = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))

    if fixture is None \
            or not fixture.is_valid() \
            or current_browser != browser_value:

            fixture = AppManager(browser=current_browser)
            browser_value=current_browser

    smart_start(fixture, current_param)
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture


@pytest.fixture(scope="function")
def func():
    fixture.table.smart_table_to_start_test()


def smart_start(fixture, current_param):
    global restart

    restart = fixture.navigator.smart_home_page_opening(current_param)
    fixture.settings.smart_settings_popup_closed(restart)



def pytest_addoption(parser):
   # parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")
'''
def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_for_test"):
            data_for_test = testdata

            metafunc.parametrize(fixture, data_for_test, ids=[str(x) for x in testdata])
'''


