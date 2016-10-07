import unittest
import test_admin_add_user_group
import test_admin_login
import test_basic


def suite():
    """
    Gather all the tests from this module in a test suite.
    """
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(test_admin_add_user_group.AdminAddUserGroup))
    test_suite.addTest(unittest.makeSuite(test_admin_login.AdminLoginTest02))
    test_suite.addTest(unittest.makeSuite(test_basic.BasicTest))
    return test_suite


if __name__ == '__main__':
    # log_file = 'log_file.txt'
    # f = open(log_file, "w")
    # runner = unittest.TextTestRunner(f)
    # unittest.main(testRunner=runner)
    # f.close()
    suite_set = suite()
    runner=unittest.TextTestRunner()
    runner.run(suite_set)

