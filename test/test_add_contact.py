# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
from random import randint
import string
import re


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    random_str = prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
    return re.sub(' +', ' ', random_str.strip())


def random_day(format):
    return format % randint(1, 31)


def random_month(format):
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]
    return format % months[randint(0, 11)]


testdata = [
Contact(firstname="", middlename="", lastname="", nickname="", company="", title="", address="", home="",
                    mobile="", work="", fax="", email="", email2="", email3="", homepage="", bday="//option[@value='-']",
                    bmonth="//option[@value='-']", byear="", aday="(//option[@value='-'])[2]",
                    amonth="(//option[@value='-'])[2]", ayear="", address2="", phone2="", notes="")] + [
    Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10),
            lastname=random_string("lastname", 15), nickname=random_string("nickname", 10),
            company=random_string("company", 25), title=random_string("title", 5), address=random_string("address", 30),
            home=random_string("home", 10), mobile=random_string("mobile", 13), work=random_string("work", 13),
            fax=random_string("fax", 13), email=random_string("email", 20), email2=random_string("email2", 20),
            email3=random_string("email3", 20), homepage=random_string("email", 15), bday=random_day("//option[@value='%d']"),
            bmonth=random_month("//option[@value='%s']"), byear=random_string("by", 2), aday=random_day("(//option[@value='%d'])[2]"),
            amonth=random_month("(//option[@value='%s'])[2]"), ayear=random_string("ay", 2), address2=random_string("address2", 30),
            phone2=random_string("phone2", 20), notes=random_string("notes", 20))
    for i in range(5)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    all_phones = contact.home + '\n' + contact.mobile + '\n' + contact.work + '\n' + contact.phone2
    all_emails = contact.email + '\n' + contact.email2 + '\n' + contact.email3
    new_contact_id = max(c.id for c in new_contacts)
    cleaned_test_contact = Contact(firstname=contact.firstname, lastname=contact.lastname, id=new_contact_id,
                                 address=contact.address, all_emails_from_home_page=all_emails,
                                 all_phones_from_home_page=all_phones)
    old_contacts.append(cleaned_test_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)