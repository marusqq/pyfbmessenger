import unittest

from messenger.login_to_messenger import login_to_messenger


class TestLoginToMessenger(unittest.TestCase):

    def test_login_to_messenger(self):
        print('Testing login to messenger')
        self.assertTrue(login_to_messenger())


unittest.main()
