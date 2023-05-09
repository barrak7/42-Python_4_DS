import time


def ft_fqdm(lst: range) -> None:
    '''A loading bar function which yields a value from list each time.

    It updates the loading bar based on how much time is left to finish.'''
    per = 0
    max = len(lst)
    f_t = time.time()
    o_t = f_t
    for elem in lst:
        per = elem / (max - 1) * 100
        tn = time.time()
        if elem == 0:
            print(f"{0:>3}%|[>{' '*101}]| 0/{max} [00:00<?, ?it/s]", end="\r")
        elif elem + 1 == max:
            print(f"{int(per):>3}%|[{('='*int(per))+'>':<101}]| {elem+1}/{max} [{time.strftime('%M:%S', time.gmtime(tn - f_t))}<{time.strftime('%M:%S', time.gmtime((tn - o_t)*(max-elem)))}, {1 / (tn - o_t):.2f}it/s]", end="\n")
        else:
            print(f"{int(per):>3}%|[{('='*int(per))+'>':<101}]| {elem+1}/{max} [{time.strftime('%M:%S', time.gmtime(tn - f_t))}<{time.strftime('%M:%S', time.gmtime((tn - o_t)*(max-elem)))}, {1 / (tn - o_t):.2f}it/s]", end="\r")
        o_t = time.time()
        yield


# test
def main():
    for e in ft_fqdm(range(333)):
        time.sleep(0.1)


if __name__ == "__main__":
    main()
