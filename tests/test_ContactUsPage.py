import time

from selenium.webdriver.support.select import Select

from pageObjects.ContactUsPage import ContactUsPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestContactUsPage(BaseClass):

    def test_contact_us_submission(self):
        home_page = HomePage(self.driver)
        home_page.get_contact_us()

        # Redirection to Contact Us form page
        contact_us_page = ContactUsPage(self.driver)
        contact_us_page.get_subject_heading("Customer service")
        contact_us_page.get_email_address().click()
        contact_us_page.get_email_address().send_keys("abcd1234@abcd.com")
        contact_us_page.get_order_reference().click()
        contact_us_page.get_order_reference().send_keys("123456789")
        contact_us_page.get_message().click()
        contact_us_page.get_message().send_keys("Hi there!")
        time.sleep(5)
        contact_us_page.send_contact_form().click()
        time.sleep(5)
        success_text = contact_us_page.get_contact_form_success().text
        form_submission_success = "Your message has been successfully sent to our team."
        assert (success_text in form_submission_success)
        self.driver.refresh()

    def test_empty_contact_us_submission(self):
        home_page = HomePage(self.driver)
        home_page.get_contact_us()

        # Redirection to Contact Us form page
        contact_us_page = ContactUsPage(self.driver)
        contact_us_page.send_contact_form().click()
        failure_text = contact_us_page.get_contact_form_fail().text
        form_submission_fail = "Invalid email address."
        assert (failure_text in form_submission_fail)
        self.driver.refresh()



