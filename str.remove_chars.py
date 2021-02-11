
def remove_characters(value, chars='\\/:*?"<>|'):
    """
    used to remove invalid chars in filenames
    """
    for ch in chars:
        value = value.replace(ch, '')
    return value
