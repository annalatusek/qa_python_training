# -*- coding: utf-8 -*-

from model.group import Group


def test_add_group(app):
    app.group.create(Group(name ="Grupa nr 1", header ="Grupa pierwsza", footer ="Group no 1"))


def test_add_empty_group(app):
    app.group.create(Group(name ="", header ="", footer =""))
