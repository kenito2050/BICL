"""
    This global_variables.py file contains all global variables that will be used for test
    configuration
"""
from pathlib import Path

# declare global variables
ROOT_DIR = Path(__file__).parent.resolve()
CONFIG_PATH = ROOT_DIR / 'config_files'

## Directory Locations
framework_directory = ROOT_DIR
config_file_directory = CONFIG_PATH
test_case_directory = framework_directory / 'utilities' / 'test_cases'
screenshot_directory = framework_directory / 'utilities' / 'test_results' / 'screenshots'
download_directory = framework_directory / 'utilities' / 'test_results' / 'downloads'

# csv directory where test scenarios are located
# csv_directory = str(test_case_directory / "test_scenarios_dev.csv")
csv_directory = str(test_case_directory / "test_scenarios_uat.csv")
# csv_directory = str(test_case_directory / "test_scenarios_prod.csv")