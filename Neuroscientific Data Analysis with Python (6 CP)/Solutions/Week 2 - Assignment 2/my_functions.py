def my_max(data):
    max_val = None
    for d in data:
        if max_val is None or d > max_val:
            max_val = d
    return max_val