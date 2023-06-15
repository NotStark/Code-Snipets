from collections import namedtuple

def dict_to_namedtuple(d):
    for key, value in d.items():
        if isinstance(value, dict):
            d[key] = dict_to_namedtuple(value)
    return namedtuple("DotDict", d.keys())(**d)
