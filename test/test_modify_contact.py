from model.contact import Contact


def test_modify_contact_names(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Hania", middlename="lala"))
    app.contact.modify_first_contact(Contact(firstname="Ela", middlename="Żet", lastname="Lala", nickname="Nina"))