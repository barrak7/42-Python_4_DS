import numpy as np


def quartile(data):
    return (np.percentile(data, (25, 75)))


def ft_statistics(*args, **kwargs):
    funcs = {'mean': np.mean, 'median': np.median,
             'quartile': quartile, 'std': np.std, 'var': np.var}
    arr = np.array(args)
    for k in kwargs:
        if kwargs[k] in funcs:
            if not args:
                print('ERROR')
            else:
                print(f"{kwargs[k]} : {funcs[kwargs[k]](arr)}")
