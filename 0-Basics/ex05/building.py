import sys, string

def display(text : str):
    print(f"The text contains {len(text)} characters:")
    count = 0
    for c in text:
        if c.isupper():
            count += 1
    print(f"{count} upper case letters")
    count = 0
    for c in text:
        if c.islower():
            count += 1
    print(f"{count} lower case letters")
    count = 0
    punc = string.punctuation
    for c in text:
        if c in punc:
            count += 1
    print(f"{count} punctuation marks")
    count = 0
    for c in text:
        if c.isspace():
            count += 1
    print(f"{count} spaces")
    count = 0
    for c in text:
        if c.isdigit():
            count += 1
    print(f"{count} digits")

def main():
    if len(sys.argv) == 2:
        display(sys.argv[1])
    elif len(sys.argv) == 1:
        text = input("What is the text to count?\n")
        display(text)
    else:
        print("Invalid Number of arguments!")

if __name__=="__main__":
    main()