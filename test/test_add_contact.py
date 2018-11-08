# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app, json_contacts):
    contact = json_contacts
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