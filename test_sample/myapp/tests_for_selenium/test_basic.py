import sys
sys.path.append('..')
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC

from .. import util


class PollsTest(unittest.TestCase):
    live_server_url = "http://localhost:80"

    def setUp(self):
        self.browser = util.get_test_browser()
        self.browser.implicitly_wait(100)
        # self.browser.set_page_load_timeout(100)

    def tearDown(self):
        self.browser.quit()

    def test_can_create_new_poll_via_admin_site(self):
        # Gertrude opens her web browser, and goes to the admin page
        self.browser.get(self.live_server_url + '/admin/')

        # She sees the familiar 'Django administration' heading
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Django administration', body.text)

        # TODO: use the admin site to create a Poll
        # self.fail('finish this test')

if __name__ == '__main__':
    unittest.main(verbosity=2)
