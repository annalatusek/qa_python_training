# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


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
            email3=random_string("email3", 20), homepage=random_string("email", 15), bday="//option[@value='20']",
            bmonth="//option[@value='March']", byear=random_string("", 4), aday="(//option[@value='19'])[2]",
            amonth="(//option[@value='July'])[2]", ayear=random_string("", 4), address2=random_string("address2", 30),
            phone2=random_string("phone2", 20), notes=random_string("notes", 20))
    for i in range(5)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)