from model.contact import Contact


def test_modify_contact_names(app):
    app.contact.modify_first_contact(Contact(firstname="Ela", middlename="Żet", lastname="Lala", nickname="Nina"))