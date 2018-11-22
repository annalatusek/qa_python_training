from model.contact import Contact
import random
from fixture.orm import ORMFixture


def test_add_contact_to_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Hania", middlename="lala"))

    # select random contact
    contact_list = db.get_contact_list()
    contact = random.choice(contact_list)
    print(contact)

    # select random group
    group_list = db.get_group_list()
    one_group = random.choice(group_list)

    # add selected contact to selected group
    app.contact.add_contact_to_the_group(contact.id, one_group)

    # verify if contact has been added to the group
    db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    contacts_in_selected_group = db.get_contacts_in_group(one_group.id)
    contact_exists = False
    for c in contacts_in_selected_group:
        if c.id == contact.id:
            contact_exists = True
            pass
    assert contact_exists is True


