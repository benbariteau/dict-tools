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
