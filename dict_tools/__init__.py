def map_keys(function, dictionary):
    return {
        function(key): value
        for key, value in dictionary.items()
    }


def map_values(function, dictionary):
    return {
        key: function(value),
        for key, value in dictionary.items()
    }
