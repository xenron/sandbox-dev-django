import time

from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC

from .. import util


class Admin_Add_User_Group(LiveServerTestCase):
    fixtures = ['user-data.json']

    def setUp(self):
        self.browser = util.get_test_browser()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_create_new_poll_via_admin_site(self):
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

