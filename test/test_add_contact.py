# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.session.login(username = "admin", password = "secret")
    app.contact.create(Contact(firstname="Anna", middlename="Zofia", lastname="Latusek", nickname="Ania",
                            title="Mrs", company="Firma", address="Klonowa, Katowice", home="555666",
                            mobile="333444555", work="tester", fax="456123", email="a@gmail.com",
                            email2="ab@gmail.com", email3="abc@gmail.com", homepage="www.homepage.pl",
                            bday="//option[@value='20']", bmonth="//option[@value='March']", byear="1987",
                            aday="(//option[@value='19'])[2]", amonth="(//option[@value='July'])[2]",
                            ayear="1999", address2="Kwiatowa, Sosnowiec", phone2="456456", notes="Notes"))
    app.session.logout()

def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="", middlename="", lastname="", nickname="", title="", company="",
                            address="", home="", mobile="", work="", fax="", email="", email2="", email3="",
                            homepage="", bday="//option[@value='-']", bmonth="//option[@value='-']",
                            byear="", aday="(//option[@value='-'])[2]", amonth="(//option[@value='-'])[2]",
                            ayear="", address2="", phone2="", notes=""))
    app.session.logout()
