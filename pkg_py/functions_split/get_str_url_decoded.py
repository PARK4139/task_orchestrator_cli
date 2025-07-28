def get_str_url_decoded(str_working):
    import urllib
    from urllib.parse import quote
    return urllib.parse.unquote(str_working)
