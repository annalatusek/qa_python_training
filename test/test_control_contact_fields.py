from model.contact import Contact
from random import randrange
import re


def test_contact_compare_home_page_with_db_data(app, db):
    contact = Contact(firstname="Anna", lastname="Latusek", address="Klonowa, Katowice", home="555666",
                      mobile="333444555", work="tester", email="a@gmail.com", email2="ab@gmail.com",
                      email3="abc@gmail.com", phone2="456456")
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(contact))
    contacts_from_home_page = app.contact.get_contact_list()
    contacts_from_db = db.get_contact_list()
    for contact_from_home_page in contacts_from_home_page:
        for contact_from_db in contacts_from_db:
            if contact_from_home_page.id == contact_from_db.id:
                assert contact_from_home_page.firstname == contact_from_db.firstname
                assert contact_from_home_page.lastname == contact_from_db.lastname
                assert contact_from_home_page.address == contact_from_db.address
                assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(
                    contact_from_db)
                assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(
                    contact_from_db)


def test_contact_compare_home_and_view_page(app):
    contact = Contact(firstname="Anna", lastname="Latusek", address="Klonowa, Katowice", home="555666",
                            mobile="333444555", work="tester", email="a@gmail.com", email2="ab@gmail.com",
                            email3="abc@gmail.com", phone2="456456")
    if app.contact.count() == 0:
        app.contact.create(contact)
    contacts_from_home_page = app.contact.get_contact_list()
    index = randrange(len(contacts_from_home_page))
    contact_from_home_page = contacts_from_home_page[index]
    contact.id = contact_from_home_page.id
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            (map(lambda x: clear(x),
                                 filter(lambda x: x is not None,
                                                [contact.home, contact.mobile, contact.work, contact.phone2])))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            (map(lambda x: clear(x),
                                 filter(lambda x: x is not None,
                                                [contact.email, contact.email2, contact.email3])))))