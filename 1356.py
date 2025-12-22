def get_name_by_symbol(symbol):
    for name, sym in elements.items():
        if sym == symbol:
            return name
