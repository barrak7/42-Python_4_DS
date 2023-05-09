import sys
from ft_filter import ft_filter


def main():
    if (len(sys.argv) != 3) or sys.argv[1].isalnum() or not sys.argv[2].isalnum():
        print("AssertionError: the arguments are bad")

    def a(x): return len(x) >= int(sys.argv[2])

    print(ft_filter(a, (sys.argv[1]).split()))


if __name__ == "__main__":
    main()
