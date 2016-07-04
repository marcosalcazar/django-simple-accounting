# -*- coding: utf-8 -*-
import json

from django.db import migrations

INITIAL = """
[
{
    "fields": {
        "rght": 2,
        "code": "1",
        "mandatory": true,
        "name": "Asset",
        "parent": null,
        "level": 0,
        "lft": 1,
        "tree_id": 1
    },
    "model": "accountancy.account",
    "pk": 1
},
{
    "fields": {
        "rght": 2,
        "code": "2",
        "mandatory": true,
        "name": "Liability",
        "parent": null,
        "level": 0,
        "lft": 1,
        "tree_id": 2
    },
    "model": "accountancy.account",
    "pk": 2
},
{
    "fields": {
        "rght": 2,
        "code": "3",
        "mandatory": true,
        "name": "Equity",
        "parent": null,
        "level": 0,
        "lft": 1,
        "tree_id": 3
    },
    "model": "accountancy.account",
    "pk": 3
},
{
    "fields": {
        "rght": 2,
        "code": "4",
        "mandatory": true,
        "name": "Revenue",
        "parent": null,
        "level": 0,
        "lft": 1,
        "tree_id": 4
    },
    "model": "accountancy.account",
    "pk": 4
},
{
    "fields": {
        "rght": 2,
        "code": "5",
        "mandatory": true,
        "name": "Expense",
        "parent": null,
        "level": 0,
        "lft": 1,
        "tree_id": 5
    },
    "model": "accountancy.account",
    "pk": 5
}
]
"""

def combine_names(apps, schema_editor):
    Acc = apps.get_model("accounting", "Account")
    for datum in json.loads(INITIAL):
        data = datum['fields']
        a = Acc.objects.create(code=data['code'],
                               name=data['name'],
                               parent=data['parent'],
                               mandatory=data['mandatory'],
                               lft=data['lft'],
                               rght=data['rght'],
                               tree_id=data['tree_id'],
                               level=data['level']
        )


class Migration(migrations.Migration):
    dependencies = [
        ('accounting', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(combine_names),
    ]
