from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC

from .. import util


class AdminLoginTest01(LiveServerTestCase):
    fixtures = ['user-data.json']

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


class AdminLoginTest02(LiveServerTestCase):
    fixtures = ['user-data.json']

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



# class PollsTest1(LiveServerTestCase):
#     fixtures = ['user-data.json']

#     def setUp(self):
#         self.browser = util.get_test_browser()
#         # self.browser = webdriver.Firefox()
#         self.browser.implicitly_wait(3)

#     def tearDown(self):
#         self.browser.quit()

#     def test_can_create_new_poll_via_admin_site(self):
#         # # Gertrude opens her web browser, and goes to the admin page
#         # self.browser.get(self.live_server_url + '/admin/')
#         #
#         # # She sees the familiar 'Django administration' heading
#         # body = self.browser.find_element_by_tag_name('body')
#         # self.assertIn('Django administration', body.text)

#         self.client.login(username='admin', password='123456')  # Native django test client
#         cookie = self.client.cookies['sessionid']
#         self.browser.get(
#             self.live_server_url + '/admin/')  # selenium will set cookie domain based on current page domain
#         self.browser.add_cookie({'name': 'sessionid', 'value': cookie.value, 'secure': False, 'path': '/'})
#         self.browser.refresh()  # need to update page for logged in user
#         self.browser.get(self.live_server_url + '/admin/')
#         element = WebDriverWait(self.browser, 10).until(
#             EC.presence_of_element_located((By.ID, "recent-actions-module"))
#         )
#         # element = WebDriverWait(self.browser, 10).until(
#         #     EC.presence_of_element_located((By.ID, "recent-actions-module1"))
#         # )

#         # self.browser.get('%s%s' % (self.live_server_url, '/admin/'))
#         # username_input = self.browser.find_element_by_name("username")
#         # username_input.send_keys('admin')
#         # password_input = self.browser.find_element_by_name("password")
#         # password_input.send_keys('123456')
#         # self.browser.find_element_by_xpath('//input[@value="Log in"]').click()
#         # element = WebDriverWait(self.browser, 10).until(
#         #     EC.presence_of_element_located((By.ID, "recent-actions-module"))
#         # )

#         # TODO: use the admin site to create a Poll
#         # self.fail('finish this test')


# class PollsTest2(LiveServerTestCase):
#
#     fixtures = ['user-data.json']
#
#     def setUp(self):
#         self.browser = webdriver.Firefox()
#         self.browser.implicitly_wait(3)
#
#     def tearDown(self):
#         self.browser.quit()
#
#     def test_can_create_new_poll_via_admin_site(self):
#         session_cookie = create_session_cookie(
#             email='admin',
#             password='123456',
#             create_instance=False
#         )
#
#         # visit some url in your domain to setup Selenium.
#         # (404 pages load the quickest)
#         # self.driver.get('your-url' + '/404-non-existent/')
#
#         # add the newly created session cookie to selenium webdriver.
#         self.driver.add_cookie(session_cookie)
#
#         # refresh to exchange cookies with the server.
#         self.driver.refresh()
#
#         # This time user should present as logged in.
#         self.driver.get('/admin/')
