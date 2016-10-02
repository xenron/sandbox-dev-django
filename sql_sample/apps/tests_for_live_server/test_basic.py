from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from apps.util import create_session_cookie
from apps import util
from django.contrib.staticfiles.testing import StaticLiveServerTestCase


# class PollsTest(LiveServerTestCase):
class PollsTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = util.get_test_browser()
        self.browser.implicitly_wait(100)
        self.browser.set_page_load_timeout(100)

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

