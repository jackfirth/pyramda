from pyramda.function.curry import curry


@curry
def item_path(keys, dict):
    if not keys:
        raise ValueError("Expected at least one key, got {0}".format(keys))
    current_value = dict
    for key in keys:
        current_value = current_value[key]
    return current_value
