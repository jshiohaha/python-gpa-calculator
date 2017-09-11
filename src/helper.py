#!/usr/bin/python3

from tables import *


def get_from_table(code, table):
    if code in table:
        return table.get(code)
    else:
        return -1
