from model.contact import Contact
import re
import random


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

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.start_from_homepage()
        self.select_contact_by_id(id)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def remove_contact_from_group(self, id):
        wd = self.app.wd
        self.select_contact_by_id(id)
        wd.find_element_by_xpath("//input[@name='remove']").click()

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

    def modify_contact_by_id(self, id, new_contact_data):
        wd = self.app.wd
        self.start_from_homepage()
        self.select_contact_by_id(id)
        # edit contact

        wd.find_element_by_xpath("//a[contains(href,'edit.php?id=%s')]" % id and "(//img[@alt='Edit'])").click()
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

    def select_contact_by_id(self, id):
        wd = self.app.wd
        # wd.find_element_by_css_selector("input[value='%s']" % id).click()
        wd.find_element_by_xpath("//*[@id='%s']" % id).click()

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
        wd = self.app.wd
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
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                firstname = cells[2].text
                lastname = cells[1].text
                address = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id, address=address,
                                                  all_emails_from_home_page=all_emails,
                                                  all_phones_from_home_page=all_phones))
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

    def open_contact_view_by_id(self, id):
        wd = self.app.wd
        self.start_from_homepage()
        wd.find_element_by_xpath("//a[contains(href,'edit.php?id=%s')]" % id and "(//img[@alt='Details'])").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        address = wd.find_element_by_name("address").text
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        home = wd.find_element_by_name("home").get_attribute("value")
        work = wd.find_element_by_name("work").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, address=address, email=email, email2=email2,
                       email3=email3, home=home, work=work, mobile=mobile, phone2=phone2)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home = re.search("H: (.*)", text).group(1)
        work = re.search("W: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact(home=home, work=work, mobile=mobile, phone2=phone2)

    @todo
    def check_if_contact_is_a_group_member(self, id, one_group):
        wd = self.app.wd
        self.open_contact_view_by_id(id)
        text = wd.find_element_by_id("content").text
        random_group_id = one_group.id
        member_of = re.search("./index.php?group=%s" % random_group_id, text).group(1)

    @todo
    def select_random_group_of_membership()


    def remove_contact_from_the_group(self, id):
        # go to selected group membership page
        self.remove_contact_from_group(id)

    def add_contact_to_the_group(self, id, one_group):
        wd = self.app.wd
        self.start_from_homepage()
        self.select_contact_by_id(id)
        random_group_id = one_group.id
        print(random_group_id)
        random_group_name = one_group.name
        print(random_group_name)
        # add contact to the group of random id
        wd.find_element_by_xpath("//select[@name='to_group']/option[@value='%s']" % random_group_id).click()
        wd.find_element_by_xpath("//input[@name='add']").click()
        wd.find_element_by_link_text("group page \"%s\"" % random_group_name).click()
        self.contact_cache = None

