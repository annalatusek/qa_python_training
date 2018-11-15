from model.contact import Contact
import random


def test_modify_contact_names(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Hania", middlename="lala"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.modify_contact_by_id(contact.id, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = db.get_contact_list()
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)