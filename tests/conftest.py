import pytest
from selenium import webdriver
from config_globals import *

## Directory Locations
framework_directory = ROOT_DIR
config_file_directory = CONFIG_PATH
test_case_directory = framework_directory / 'utilities' / 'test_cases'

def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="UAT",
                     help="Environment to run test against")

@pytest.fixture
def env(request):
    return request.config.getoption("--env")


@pytest.fixture(scope='class')
def browser(request):
    print("creating a new webdriver")
    options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    options.add_argument('start-maximized')
    # options.add_experimental_option('prefs', {
    #     "download.default_directory": download_directory,
    #     "download.prompt_for_download": False,
    #     "download.directory_upgrade": True,
    #     "plugins.always_open_pdf_externally": True})
    driver = webdriver.Chrome(executable_path=str(CONFIG_PATH / 'chromedriver.exe'))

    def fin():
        driver.quit()

    request.addfinalizer(fin)
    return driver