# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarioperfil', '0007_auto_20141204_2058'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'permissions': (('list_app', 'Can view list app'), ('view_app', 'Can view app'), ('add_app', 'Can add app'), ('change_app', 'Can change app'), ('delete_app', 'Can delete app'))},
        ),
    ]
