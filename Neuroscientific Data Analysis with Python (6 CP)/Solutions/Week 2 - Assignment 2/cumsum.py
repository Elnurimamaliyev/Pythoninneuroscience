def cumsum(x):
    emptylist = []
    for idx in range(len(x)):
        emptylist.append(sum(x[:idx+1]))
    return emptylist