def ft_filter(func, iter):
    '''filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.'''
    lst = []
    if func == None:
        return ([e for e in iter if e == True])
    return ([e for e in iter if func(e)])
