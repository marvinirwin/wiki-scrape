def sanitize(filename):
    replace = filename.replace('%', '_')
    return replace