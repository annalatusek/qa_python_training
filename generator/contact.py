from model.contact import Contact
from random import randint
import random
import string
import os.path
import re
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts:", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    random_str = prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
    return re.sub(' +', ' ', random_str.strip())


def random_day(format):
    return format % randint(1, 31)


def random_month(format):
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]
    return format % months[randint(0, 11)]


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
            email3=random_string("email3", 20), homepage=random_string("email", 15),
            bday=random_day("//option[@value='%d']"), bmonth=random_month("//option[@value='%s']"),
            byear=random_string("by", 2), aday=random_day("(//option[@value='%d'])[2]"),
            amonth=random_month("(//option[@value='%s'])[2]"), ayear=random_string("ay", 2), address2=random_string("address2", 30),
            phone2=random_string("phone2", 20), notes=random_string("notes", 20))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))