def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0 and len(tuple_b) == 0:
        t = 0, 0
    elif len(tuple_a) == 1 and len(tuple_b) == 0:
        t = tuple_a[0], 0
    elif len(tuple_a) == 1 and len(tuple_b) == 1:
        t = tuple_a[0] + tuple_b[0], 0
    elif len(tuple_a) == 0 and len(tuple_b) == 1:
        t = tuple_b[0], 0
    elif len(tuple_a) == 1 and len(tuple_b) == 2:
        t = tuple_a[0] + tuple_b[0], tuple_b[1]
    elif len(tuple_a) == 2 and len(tuple_b) == 1:
        t = tuple_a[0] + tuple_b[0], tuple_a[1]
    elif len(tuple_a) == 2 and len(tuple_b) == 0:
        t = tuple_a[0], tuple_a[1]
    elif len(tuple_b) == 2 and len(tuple_a) == 0:
        t = tuple_b[0], tuple_b[1]
    elif len(tuple_a) >= 2 and len(tuple_b) >= 2:
        t = tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
    return t
