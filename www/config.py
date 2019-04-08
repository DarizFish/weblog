#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import config_default

class Dict(dict):

    def __init__(self, names=(), values=(), **kw):
        super(Dict, self).__init__(**kw)
        for k, v in zip(names, values):
            self[k] = v

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

def merge(default, override):

    for k, v in override.items():
        if isinstance(v, dict):
            merge(default[k], override[k])
        else:
            default[k] = v
    return default

configs = config_default.configs

try:
    import config_override
    configs = merge(configs, config_override.configs)
    print(configs)
except ImportError:
    pass