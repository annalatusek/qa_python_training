from model.contact import Contact
import re

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
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.start_from_homepage()
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

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
        self.contact_cache = None

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.start_from_homepage()
        self.select_contact_by_index(index)
        # edit contact
        xpath = "(//img[@alt='Edit'])" + "["+str(index+1)+"]"
        wd.find_element_by_xpath(xpath).click()
        self.fill_contact_form(new_contact_data)
        # update
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.returns_to_homepage()
        self.contact_cache = None

    def returns_to_homepage(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

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

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.start_from_homepage()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                firstname = cells[1].text
                lastname = cells[2].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_phones = cells[5].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id,
                                                  all_phones_frome_home_page=all_phones, home=all_phones[0],
                                                  mobile=all_phones[1], work=all_phones[2], phone2=all_phones[3]))
        return list(self.contact_cache)

    # my first solution of the function below:
    # def get_contact_list(self):
    #     if self.contact_cache is None:
    #         wd = self.app.wd
    #         self.start_from_homepage()
    #         self.contact_cache = []
    #         for element in wd.find_elements_by_css_selector("tr[name=entry]"):
    #             id = element.find_elements_by_css_selector("td.center input")[0].get_attribute("value")
    #             last_name = element.find_elements_by_css_selector("td:nth-child(2)")[0].text
    #             name = element.find_elements_by_css_selector("td:nth-child(3)")[0].text
    #             self.contact_cache.append(Contact(lastname=last_name, firstname=name, id=id))
    #     return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.start_from_homepage()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.start_from_homepage()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home = wd.find_element_by_name("home").get_attribute("value")
        work = wd.find_element_by_name("work").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, home=home, work=work, mobile=mobile,
                       phone2=phone2)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home = re.search("H: (.*)", text).group(1)
        work = re.search("W: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact(home=home, work=work, mobile=mobile, phone2=phone2)
