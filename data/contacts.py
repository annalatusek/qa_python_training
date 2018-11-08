from model.contact import Contact

testdata = [
    Contact(firstname="firstname1", middlename="middlename1", lastname="lastname1", nickname="nickname1",
            company="company1", title="title1", address="address1", home="home1", mobile="mobile1", work="work1",
            fax="fax1", email="email1", email2="email2.1", email3="email3.1", homepage="homepage",
            bday="//option[@value='12']", bmonth="//option[@value='-']", byear="byear", aday="(//option[@value='16'])[2]",
            amonth="(//option[@value='March'])[2]", ayear="ayear1", address2="address2.1", phone2="phone2.1",
            notes="notes1"),
    Contact(firstname="firstname2", middlename="middlename2", lastname="lastname2", nickname="nickname2",
            company="company2", title="title2", address="address1.1", home="home2", mobile="mobile2", work="work2",
            fax="fax2", email="email1.1", email2="email2.2", email3="email3.2", homepage="homepage",
            bday="//option[@value='16']", bmonth="//option[@value='January']", byear="byear2",
            aday="(//option[@value='-'])[2]", amonth="(//option[@value='July'])[2]", ayear="ayear2",
            address2="address2.2", phone2="phone2.2", notes="notes2")
]