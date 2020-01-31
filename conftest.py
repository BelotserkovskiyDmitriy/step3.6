import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: rus or eng")
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_language': user_language})
        print("\n\nStart chrome browser for test...")
        brower = webdriver.Chrome(options=options)
    elif (browser_name == "firefox"):
        fp = webdriver.FirefoxProfile()
        fp.set_perference('intl.accept_language', user_language)
        print("\n\nStart firefox browser for test...")
        brower = webdriver.Firefox(firefox_profile = fp)
    else:
        print("Browser <browser_name> still isn`t implemented")
    yield browser
    print("\nQuit browser...")
    browser.quit()
    
