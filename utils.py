from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from config import *

class eLearnUtils():

    DELAY = 3  # seconds

    WEBSITE_ADDRESS = 'http://shafin-elearning.herokuapp.com/'
    USERNAME = bot_username
    PASSWORD = bot_password

    FIRST_NAME = 'pybot'
    LAST_NAME = 'noob'
    EMAIL = bot_email


    # XPATHS/SELECTORS

    # Login page
    USERNAME_SELECTOR = "//*[@id='id_username']"
    LOGIN_PW_SELECTOR = "//*[@id='id_password']"
    SUBMIT_SELECTOR = "//*[@value='Submit']"

    # Signup page
    FIRST_NAME_SELECTOR = '// *[ @ id = "id_first_name"]'
    LAST_NAME_SELECTOR = '//*[@id="id_last_name"]'
    EMAIL_SELECTOR = '//*[@id="id_email"]'
    PASSWORD_1_SELECTOR = '//*[@id="id_password1"]'
    PASSWORD_2_SELECTOR = '//*[@id="id_password2"]'

    # Navbar
    LOGIN_SELECTOR = "//a[contains(@href,'login')]"
    SIGNUP_SELECTOR = ".nav-link.signup-link"
    COURSES_SELECTOR = "//a[contains(@href,'courses')]"
    NAV_CART_SELECTOR = "//a[contains(@href,'cart')]"
    PROFILE_DROPDOWN_SELECTOR = "navbarDropdown"
    PROFILE_SELECTOR = "//a[contains(@href,'profile')]"

    # Course List Page
    ADD_TO_CART_SELECTOR = "/ html / body / div / div[3] / div / div[3] / div[2] / form / div / center / span / button[1]"

    # Cart home
    CHECKOUT_SELECTOR = "//a[contains(@href,'checkout')]"

    # Checkout home
    PAYMENT_EDIT_SELECTOR = "edit-payment-info"
    # CARD_NUM_SELECTOR = "cardnumber"
    CARD_NUM_SELECTOR = "/html/body/div/form/div/div[2]/span[1]/span[2]/span/input"
    CARD_NUMBER = "4"
    CARD_EXP_SELECTOR = "exp-date"
    CARD_EXP = "0424"
    CARD_CVC_SELECTOR = "cvc"
    CARD_CVC = "242"
    CARD_ZIP_SELECTOR = "postal"
    CARD_ZIP = "42424"

    BILLING_ADDRESS_EDIT_SELECTOR = "edit-address"
    ADDRESS_LINE_1 = "1111 Python Lane"
    ADDRESS_LINE_1_SELECTOR = "address_line_1"
    CITY = "Silicon Valley"
    CITY_SELECTOR = "city"
    COUNTRY_SELECTOR = "//*[@id='id_country']/option[238]"
    STATE = "CA"
    STATE_SELECTOR = "state"
    POSTAL_CODE = "94027"
    POSTAL_CODE_SELECTOR = "postal_code"
    BILLING_ADDRESS_SUBMIT_SELECTOR = "submit-address"

    COMPLETE_CHECKOUT_BTN_SELECTOR = "complete-payment-btn"

    # Profile
    ACCOUNT_TAB_SELECTOR = '.nav-link.account-tab'
    DELETE_ACCOUNT_BTN_SELECTOR = "//a[contains(@href,'delete-account-confirm')]"
    DELETE_ACCOUNT_CONFIRM_BTN_SELECTOR = "//input[contains(@value,'delete account')]"



    def validate_action_success(self, driver, url):
        next_page_url = driver.current_url

        if next_page_url == url:
            return False
        else:
            return True


    def attempt_login(self, driver):
        driver.find_element_by_xpath(self.LOGIN_SELECTOR).click()
        login_page_url = driver.current_url

        driver.implicitly_wait(10)

        username = driver.find_element_by_xpath(self.USERNAME_SELECTOR).send_keys(self.USERNAME)
        pw = driver.find_element_by_xpath(self.LOGIN_PW_SELECTOR).send_keys(self.PASSWORD)
        submit = driver.find_element_by_xpath(self.SUBMIT_SELECTOR).click()

        result = self.validate_action_success(driver, login_page_url)
        return result


    def attempt_signup(self, driver):
        signup_link = driver.find_element_by_css_selector(self.SIGNUP_SELECTOR)
        ActionChains(driver).move_to_element(signup_link).click().perform()
        signup_page_url = driver.current_url

        myElem = WebDriverWait(driver, self.DELAY).until(EC.presence_of_element_located((By.XPATH, self.FIRST_NAME_SELECTOR)))

        first_name = driver.find_element_by_xpath(self.FIRST_NAME_SELECTOR).send_keys(self.FIRST_NAME)
        last_name = driver.find_element_by_xpath(self.LAST_NAME_SELECTOR).send_keys(self.LAST_NAME)
        username = driver.find_element_by_xpath(self.USERNAME_SELECTOR).send_keys(self.USERNAME)
        email = driver.find_element_by_xpath(self.EMAIL_SELECTOR).send_keys(self.EMAIL)
        pw = driver.find_element_by_xpath(self.PASSWORD_1_SELECTOR).send_keys(self.PASSWORD)
        pw2 = driver.find_element_by_xpath(self.PASSWORD_2_SELECTOR).send_keys(self.PASSWORD)
        submit = driver.find_element_by_xpath(self.SUBMIT_SELECTOR).click()

        result = self.validate_action_success(driver, signup_page_url)
        return result


    def go_to_courses(self, driver):
        try:
            courses_nav_link = driver.find_element_by_xpath(self.COURSES_SELECTOR).click()
            return True
        except:
            return False


    def add_course(self, driver):
        try:
            course_add_btn = driver.find_element_by_xpath(self.ADD_TO_CART_SELECTOR)
            course_add_btn.click()
            return True
        except:
            return False


    def go_to_cart(self, driver):
        try:
            cart_nav_link = driver.find_element_by_xpath(self.NAV_CART_SELECTOR)
            cart_nav_link.click()
            return True
        except:
            return False


    def go_to_checkout_home(self, driver):
        try:
            checkout_btn = driver.find_element_by_xpath(self.CHECKOUT_SELECTOR)
            checkout_btn.click()
            return True
        except:
            return False



    def enter_billing_address(self, driver):
        try:
            edit_btn = driver.find_element_by_class_name(self.BILLING_ADDRESS_EDIT_SELECTOR).click()
            driver.find_element_by_name(self.ADDRESS_LINE_1_SELECTOR).send_keys(self.ADDRESS_LINE_1)
            driver.find_element_by_name(self.CITY_SELECTOR).send_keys(self.CITY)
            driver.find_element_by_name(self.STATE_SELECTOR).send_keys(self.STATE)
            driver.find_element_by_name(self.POSTAL_CODE_SELECTOR).send_keys(self.POSTAL_CODE)
            driver.find_element_by_xpath(self.COUNTRY_SELECTOR).click()
            driver.find_element_by_class_name(self.BILLING_ADDRESS_SUBMIT_SELECTOR).click()
            return True
        except:
            return False


    def click_complete_payment(self, driver):
        try:
            checkout_page_url = driver.current_url
            driver.find_element_by_class_name('complete-payment-btn').click()
            result = self.validate_action_success(driver, checkout_page_url)
            return result
        except:
            return False


    def go_to_profile(self, driver):
        current_page_url = driver.current_url
        driver.find_element_by_id(self.PROFILE_DROPDOWN_SELECTOR).click()
        driver.find_element_by_xpath(self.PROFILE_SELECTOR).click()
        result = self.validate_action_success(driver, current_page_url)
        return result


    def click_account(self, driver):
        myElem = WebDriverWait(driver, self.DELAY).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.ACCOUNT_TAB_SELECTOR)))
        # tab_selector = driver.find_element_by_css_selector(self.ACCOUNT_TAB_SELECTOR)
        ActionChains(driver).move_to_element(myElem).click().perform()
        driver.execute_script("arguments[0].click();", myElem)
        myElem.click()
        return True


    def delete_account(self, driver):
        try:
            driver.find_element_by_xpath(self.DELETE_ACCOUNT_BTN_SELECTOR).click()
            driver.find_element_by_xpath(self.DELETE_ACCOUNT_CONFIRM_BTN_SELECTOR).click()
            return True
        except:
            return False


if __name__ == '__main__':
    eLearnUtils()
