#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time, uuid

from blogorm import Model, StringField, BooleanField, FloatField, TextField
from functools import reduce
def next_id():
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)

class User(Model):
    __table__ = 'users'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    email = StringField(ddl='varchar(50)')
    passwd = StringField(ddl='varchar(50)')
    admin = BooleanField()
    name = StringField(ddl='varchar(50)')
    image = StringField(ddl='varchar(500)')
    created_at = FloatField(default=time.time)

class Blog(Model):
    __table__ = 'blogs'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    name = StringField(ddl='varchar(50)')
    summary = StringField(ddl='varchar(200)')
    content = TextField()
    created_at = FloatField(default=time.time)

class Comment(Model):
    __table__ = 'comments'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    blog_id = StringField(ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    content = TextField()
    created_at = FloatField(default=time.time)


#generate sql tables
if __name__ == '__main__':

    def initscript():
        dropstr = 'drop database if exists awesome;'
        creatstr = 'create database awesome;'
        usestr = 'use awesome;'
        grantstr = "grant select, insert, update, delete on awesome.* to 'www-data'@'localhost' identified by 'www-data';"
        return '\n\r'.join([dropstr, creatstr, usestr, grantstr])

    def createscript(model):
        cols = []
        for k, v in model.__mappings__.items():
            cols.append("^%s^ %s not null" % (k, v.column_type))
        modelstr = " \n\r create table %s ( %s ) \n\r engine=innodb default charse=utf8;" % (model.__table__, ',\n\r'.join(cols))
        return modelstr

    str = '\n\r'.join([createscript(x) for x in [User, Blog, Comment]])

    with open('schema.sql', 'w', encoding='utf-8') as f:
        f.write(initscript() + str)
