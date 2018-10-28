# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Anna", middlename="Zofia", lastname="Latusek", nickname="Ania",
                            company="Firma", title="Mrs", address="Klonowa, Katowice", home="555666",
                            mobile="333444555", work="tester", fax="456123", email="a@gmail.com",
                            email2="ab@gmail.com", email3="abc@gmail.com", homepage="www.homepage.pl",
                            bday="//option[@value='20']", bmonth="//option[@value='March']", byear="1987",
                            aday="(//option[@value='19'])[2]", amonth="(//option[@value='July'])[2]",
                            ayear="1999", address2="Kwiatowa, Sosnowiec", phone2="456456", notes="Notes")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# def test_add_empty_contact(app):
#     old_contacts = app.contact.get_contact_list()
#     contact = Contact(firstname="", middlename="", lastname="", nickname="", company="", title="",
#                             address="", home="", mobile="", work="", fax="", email="", email2="", email3="",
#                             homepage="", bday="//option[@value='-']", bmonth="//option[@value='-']",
#                             byear="", aday="(//option[@value='-'])[2]", amonth="(//option[@value='-'])[2]",
#                             ayear="", address2="", phone2="", notes="")
#     app.contact.create(contact)
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) + 1 == len(new_contacts)
#     old_contacts.append(contact)
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)