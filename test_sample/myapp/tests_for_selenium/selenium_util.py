import os

from selenium import webdriver

def get_test_browser(name=None):
    browser = None
    
    if not name or name == "ff":
        # Firefox
        browser = webdriver.Firefox()
    elif name == "p":
        browser = webdriver.PhantomJS()
    elif name == "ie":
        # browser = webdriver.IE()
        pass
    elif name == "ch":
        # Chrome
        chromedriver = "d:\\soft\\webdriver\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        browser = webdriver.Chrome(chromedriver)

    return browser
