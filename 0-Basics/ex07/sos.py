import sys


def sos(text: str) -> None:
    '''a function to translate a python string into morse code.

    It prints the result to the screen and returns None.
    '''
    morse = {' ': '/ ', 'A': '.- ', 'B': '-... ',
             'C': '-.-. ', 'D': '-.. ', 'E': '. ',
             'F': '..-. ', 'G': '--. ', 'H': '.... ',
             'I': '.. ', 'J': '.--- ', 'K': '-.- ',
             'L': '.-.. ', 'M': '-- ', 'N': '-. ',
             'O': '--- ', 'P': '.--. ', 'Q': '--.- ',
             'R': '.-. ', 'S': '... ', 'T': '- ',
             'U': '..- ', 'V': '...- ', 'W': '.-- ',
             'X': '-..- ', 'Y': '-.-- ', 'Z': '--.. ',
             '1': '.---- ', '2': '..--- ', '3': '...-- ',
             '4': '....- ', '5': '..... ', '6': '-.... ',
             '7': '--... ', '8': '---.. ', '9': '----. ',
             '0': '----- ', ',': '--..-- ', '.': '.-.-.- ',
             '?': '..--.. ', '/': '-..-. ', '-': '-....- ',
             '(': '-.--. ', ')': '-.--.- '}
    text = text.upper()
    mc = text.maketrans(morse)
    print(text.translate(mc).rstrip())


def main():
    sos('test')


if __name__ == "__main__":
    main()
