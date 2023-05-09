import sys
if len(sys.argv) > 2 or not sys.argv[1].isnumeric():
    raise(AssertionError('No more than one int value is allowed!'))
else:
    if (int(sys.argv[1]) % 2):
        print("I'm Odd!")
    else:
        print("I'm Even!")