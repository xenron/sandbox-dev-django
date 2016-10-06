import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC

import util


class AdminAddUserGroup(unittest.TestCase):
    live_server_url = "http://localhost:80"

    def setUp(self):
        self.browser = util.get_test_browser()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_add_user_group(self):
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

        time.sleep(2)

        self.browser.get(self.live_server_url + '/admin/auth/group/')
        element = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "addlink"))
        )
        self.browser.find_element_by_class_name('addlink').click()
        element = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.NAME, "_save"))
        )

        time.sleep(2)
        groupname = 'テストグループ１'
        groupname_input = self.browser.find_element_by_id('id_name')
        groupname_input.send_keys(groupname)
        self.browser.find_element_by_name("_save").click()
        element = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "success"))
        )

        time.sleep(2)
        success_message = self.browser.find_element_by_class_name('success')
        self.assertIn(groupname, success_message.text)

