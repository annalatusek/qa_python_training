from model.group import Group
from random import randrange


def test_modify_group_name(app, db):
    if len(db.get_group_list()) == 0:
        db.create(Group(name="test"))
    old_groups = db.get_group_list()
    group = Group(name="F")
    index = randrange(len(old_groups))
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
