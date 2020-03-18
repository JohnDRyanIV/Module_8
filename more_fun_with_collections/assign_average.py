def switch_average(key):
    """
    :param key: key being searched for in dictionary
    :return: value at key's location in dictionary
    """
    switcher = {
        'A': 90,
        'B': 80,
        'C': 70,
        'D': 60,
        'F':  0
    }
    return switcher.get(key, KeyError)


