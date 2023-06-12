#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    n1 = 0
    n2 = 0
    if len(tuple_a) - 1 >= 0:
        n1 += tuple_a[0]
    if len(tuple_b) - 1 >= 0:
        n1 += tuple_b[0]
    if len(tuple_a) - 1 >= 1:
        n2 += tuple_a[1]
    if len(tuple_b) - 1 >= 1:
        n2 += tuple_b[1]
    return (n1, n2)
