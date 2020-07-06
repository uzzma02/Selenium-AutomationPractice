from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class ContactUsPage:

    def __init__(self, driver):
        self.driver = driver

    contact_us_heading = (By.XPATH, "//h3[contains(text(),'send a message')]")
    subject_heading = (By.ID, "id_contact")
    contact_form_email = (By.ID, "email")
    contact_form_order_reference = (By.NAME, "id_order")
    contact_form_attachment = (By.XPATH, "//span[@class='action']")
    contact_form_message = (By.ID, "message")
    contact_form_submit = (By.NAME, "submitMessage")
    contact_form_success_message = (By.XPATH, "//p[@class='alert alert-success']")
    contact_form_fail_message = (By.XPATH, "//li[contains(text(),'Invalid email address.')]")

    def get_subject_heading(self, text):
        heading_dropdown = Select(self.driver.find_element(*ContactUsPage.subject_heading))
        heading_dropdown.select_by_visible_text(text)
        return heading_dropdown

    def get_email_address(self):
        return self.driver.find_element(*ContactUsPage.contact_form_email)

    def get_order_reference(self):
        return self.driver.find_element(*ContactUsPage.contact_form_order_reference)

    def get_attachment(self):
        return self.driver.find_element(*ContactUsPage.contact_form_attachment)

    def get_message(self):
        return self.driver.find_element(*ContactUsPage.contact_form_message)

    def send_contact_form(self):
        return self.driver.find_element(*ContactUsPage.contact_form_submit)

    def get_contact_form_success(self):
        return self.driver.find_element(*ContactUsPage.contact_form_success_message)

    def get_contact_form_fail(self):
        return self.driver.find_element(*ContactUsPage.contact_form_fail_message)
