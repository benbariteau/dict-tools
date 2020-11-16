def map_keys(function, dictionary):
    return {
        function(key): value
        for key, value in dictionary.items()
    }


def map_values(function, dictionary):
    return {
        key: function(value)
        for key, value in dictionary.items()
    }


def flattened_items(dictionary):
    for key, value in dictionary.items():
        for subvalue in value:
            yield (key, subvalue)


def invert_dict(dictionary):
    return {
        value: key
        for key, value in dictionary.items()
    }


def group_by(iterable, key=lambda value: value):
    """
    Takes an iterable and construct a dictionary with keys as created by the key
    function to lists of values.

    This function is useful when you need to construct a mapping from a sequence,
    but the key value might be repeated.
    """
    result = {}
    for value in iterable:
        key_value = key(value)
        if key_value not in result:
            result[key_value] = [value]
        else:
            result[key_value] += [value]

    return result
