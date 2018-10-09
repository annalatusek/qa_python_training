from model.contact import Contact

def test_modify_first_contact(app):
    app.session.login(username = "admin", password = "secret")
    app.contact.modify_first_contact(Contact(firstname="Ela", middlename="Żet", lastname="Lala", nickname="Nina",
                                             title="pani", company="Firemka", address="Zielona, Sosnowiec",  home="",
                                             mobile="", work="", fax="", email="", email2="", email3="", homepage="",
                                             bday="//option[@value='-']", bmonth="//option[@value='-']", byear="",
                                             aday="(//option[@value='-'])[2]", amonth="(//option[@value='-'])[2]",
                                             ayear="", address2="", phone2="", notes=""))
    app.session.logout()