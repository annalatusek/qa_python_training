class ContactHelper:

    def __init__(self, app):
        self.app = app


    def start_from_homepage(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name("searchform")) > 0):
            wd.find_element_by_xpath("//a[contains(text(),'home')]").click()

    def create(self, contact):
        wd = self.app.wd
        self.start_from_homepage()
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # submit
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.returns_to_homepage()

    def delete_first_contact(self):
        wd = self.app.wd
        self.start_from_homepage()
        self.select_first_contact()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.start_from_homepage()
        self.select_first_contact()
        # edit contact
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_form(new_contact_data)
        # update
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.returns_to_homepage()

    def returns_to_homepage(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_value_xpath(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_xpath(text).click()

    def fill_contact_form(self, contact):
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        # write telephone info
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        # write email addresses
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        # give additional info
        self.change_field_value("homepage", contact.homepage)
        self.change_value_xpath("bday", contact.bday)
        self.change_value_xpath("bmonth", contact.bmonth)
        self.change_field_value("byear", contact.byear)
        self.change_value_xpath("aday", contact.aday)
        self.change_value_xpath("amonth", contact.amonth)
        self.change_field_value("ayear", contact.ayear)
        # give secondary info
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def count(self):
        wd = self.app.wd
        self.start_from_homepage()
        return len(wd.find_elements_by_name("selected[]"))