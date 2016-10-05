import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC

from .. import util


class AdminLoginTest01(unittest.TestCase):
    live_server_url = "http://localhost:80"

    def setUp(self):
        self.browser = util.get_test_browser()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_login_by_add_cookie(self):
        # Native django test client
        self.client.login(username='admin', password='123456')
        cookie = self.client.cookies['sessionid']
        # selenium will set cookie domain based on current page domain
        self.browser.get(self.live_server_url + '/admin/')
        self.browser.add_cookie({'name': 'sessionid', 'value': cookie.value, 'secure': False, 'path': '/'})
        # need to update page for logged in user
        self.browser.refresh()
        self.browser.get(self.live_server_url + '/admin/')
        element = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.ID, "recent-actions-module"))
        )


class AdminLoginTest02(unittest.TestCase):

    def setUp(self):
        self.browser = util.get_test_browser()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_login_by_input_click(self):
        # Native django test client
        self.browser.get(self.live_server_url + '/admin/')
        username_input = self.browser.find_element_by_name("username")
        username_input.send_keys('admin')
        password_input = self.browser.find_element_by_name("password")
        password_input.send_keys('123456')
        self.browser.find_element_by_xpath('//input[@value="Log in"]').click()
        element = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.ID, "recent-actions-module"))
        )


