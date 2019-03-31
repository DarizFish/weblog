#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from webframe import *
from models import *

@get('/')
async def index(request):
    users = await User.findAll()
    return {
        '__template__': 'test.html',
        'users': users
    }