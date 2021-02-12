#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def check(r, l):
    ci = 0
    if r > 0:
        for c in l:
            if c == '(':
                ci += 1
            elif c == ')':
                ci -= 1
        check(r-1, l)
    else:
        if counter == 0:
            print("CORRECT")
        else:
            return False

if __name__ == '__main__':
    val = input()
    l = list(val)
    r = int(len(l))
    check(r, l)
