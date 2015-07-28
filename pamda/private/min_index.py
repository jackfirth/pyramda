from functools import partial


def index_of(lst, item):
    return lst.index(item)


def indices(lst, items):
    return map(partial(index_of, lst), items)


def min_index(lst, items):
    return min(indices(lst, items))
