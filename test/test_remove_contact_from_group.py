from model.contact import Contact
import random
from fixture.orm import ORMFixture


def test_remove_contact_from_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Hania", middlename="lala"))

    # select random contact
    contact_list = db.get_contact_list()
    contact = random.choice(contact_list)
    print(contact)

    # select random group
    group_list = db.get_group_list()
    group_to_add = random.choice(group_list)

    # add selected contact to selected group
    app.contact.add_contact_to_the_group(contact.id, group_to_add)

    # check if selected contact is in any group
    links_of_groups_where_contact_is_connected = app.contact.get_list_of_groups_for_contact(db, contact.id)
    group_id_to_remove = app.contact.select_random_group_from_the_list(links_of_groups_where_contact_is_connected)

    # remove a contact from the group
    app.contact.remove_contact_from_the_group(contact.id)

    # verify if contact has been removed from the group
    db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    contacts_in_selected_group = db.get_contacts_in_group(group_id_to_remove)
    contact_exists = False
    for c in contacts_in_selected_group:
        if c.id == contact.id:
            contact_exists = True
            pass
    assert contact_exists is False