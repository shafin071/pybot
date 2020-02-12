import chromedriver_binary  # Adds chromedriver binary to path
import smtplib
import sys
import unittest

from selenium import webdriver


from utils import eLearnUtils
from config import *


class eLearnAppTest(unittest.TestCase, eLearnUtils):

    MESSAGE = ''
    FINAL_MESSAGE = []

    # This method is from stack overflow. I tweaked the function just a wee bit
    def tearDown(self):
        if hasattr(self, '_outcome'):  # Python 3.4+
            result = self.defaultTestResult()  # these 2 methods have no side effects
            self._feedErrorsToResult(result, self._outcome.errors)
        else:  # Python 3.2 - 3.3 or 3.0 - 3.1 and 2.7
            result = getattr(self, '_outcomeForDoCleanups', self._resultForDoCleanups)
        error = self.list2reason(result.errors)
        failure = self.list2reason(result.failures)
        ok = not error and not failure


        if not ok:
            typ, text = ('ERROR', error) if error else ('FAIL', failure)
            msg = [x for x in text.split('\n')[1:] if not x.startswith(' ')][0]
            print(f"TEST: {self.id()} \nSTATUS: {typ} \nREASON: {msg}")
            self.MESSAGE += f"TEST: {self.id()} \nSTATUS: {typ} \nREASON: {msg}"

        else:
            print(f"TEST: {self.id()}... STATUS: PASSED")
            self.MESSAGE +=f"TEST: {self.id()} \nSTATUS: PASSED"

        self.final_func(self.MESSAGE)

    # This method is from stack overflow
    def list2reason(self, exc_list):
        if exc_list and exc_list[-1][0] is self:
            return exc_list[-1][1]



    def test_1_register_user(self):
        '''
        Visit web page and register user. PASSED means user was able to register
        '''
        self.driver = webdriver.Chrome()
        self.driver.get(self.WEBSITE_ADDRESS)
        self.assertEqual(self.attempt_signup(self.driver), True, msg="Signup failed")
        self.driver.close()
        self.driver.quit()




    def test_2_fail_to_buy_course_without_payment(self):
        '''
        Attempt to login and buy a course without entering payment info.
        PASSED means user was unable to checkout without entering payment method.
        '''
        self.driver = webdriver.Chrome()
        self.driver.get(self.WEBSITE_ADDRESS)
        self.assertEqual(self.attempt_login(self.driver), True, msg="Login failed")
        self.assertEqual(self.go_to_courses(self.driver), True, msg="Course Nav Link xpath not found")
        self.assertEqual(self.add_course(self.driver), True, msg="Course add btn xpath not found")
        self.assertEqual(self.go_to_cart(self.driver), True, msg="Navbar Cart xpath not found")
        self.assertEqual(self.go_to_checkout_home(self.driver), True, msg="Checkout btn xpath not found")
        self.assertEqual(self.enter_billing_address(self.driver), True, msg="Billing Address segment xpath not found")
        self.assertEqual(self.click_complete_payment(self.driver), False, msg="Complete payment xpath not found / billing or payment incomplete")
        self.driver.close()
        self.driver.quit()




    def test_3_login_and_delete_account(self):
        '''
        Log in and delete account. PASSED means account was successfully deleted
        '''
        self.driver = webdriver.Chrome()
        self.driver.get(self.WEBSITE_ADDRESS)
        self.assertEqual(self.attempt_login(self.driver), True, msg="Login failed")
        self.assertEqual(self.go_to_profile(self.driver), True, msg="Profile dropdown xpath not found")
        self.assertEqual(self.click_account(self.driver), True, msg="Account xpath not found")
        self.assertEqual(self.delete_account(self.driver), True, msg="Delete account xpath not found")
        self.driver.close()
        self.driver.quit()



    def test_4_confirm_account_deletion(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.WEBSITE_ADDRESS)
        self.assertEqual(self.attempt_login(self.driver), False, msg="Login success. User not deleted")
        self.driver.close()
        self.driver.quit()



    def final_func(self, msg):
        self.FINAL_MESSAGE.append(msg)


    def send_email(self, msg_list):
        email_body = ''
        for msg in msg_list:
            email_body += f"\n\n{msg}\n\n"
            email_body += "\n-----------------------------------------------------------\n"

        smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_server.ehlo()
        smtp_server.starttls()
        smtp_server.login(bot_email, bot_password)

        smtp_server.sendmail(bot_email, admin_email,
                             f'Subject: AUTOMATED TEST REPORT! \nHi Shafin... '
                             f'\nHere is the test report: \n{email_body}\n\n\nRegards,\nPybot')

        smtp_server.quit()
        print('Email sent successfully')


    @classmethod
    def tearDownClass(cls):
        cls.send_email(cls, cls.FINAL_MESSAGE)






if __name__ == '__main__':
    unittest.main()





