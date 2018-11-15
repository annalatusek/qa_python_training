from model.group import Group
import random


def test_modify_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        db.create(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.modify_group_by_id(group.id, group)
    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)