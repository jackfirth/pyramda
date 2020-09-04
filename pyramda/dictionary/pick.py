from pyramda.function.curry import curry


@curry
def pick(keys, dict):
    return {k: v for k, v in dict.items() if k in keys}
