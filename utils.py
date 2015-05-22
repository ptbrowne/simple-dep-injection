def result(fn_or_value):
    if getattr(fn_or_value, '__call__', None):
        return fn_or_value()
    else:
        return fn_or_value
