from pyramda.function.curry import curry


@curry
def pick(keys, dict):
    picked_dict = {}
    for k in keys:
        if k in dict:
            picked_dict[k] = dict[k]
    return picked_dict
