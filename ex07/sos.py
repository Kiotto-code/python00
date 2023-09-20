import sys


def sos(text: str) -> str:
    """
        convert string into morse code
    """
    MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                       'C': '-.-.', 'D': '-..', 'E': '.',
                       'F': '..-.', 'G': '--.', 'H': '....',
                       'I': '..', 'J': '.---', 'K': '-.-',
                       'L': '.-..', 'M': '--', 'N': '-.',
                       'O': '---', 'P': '.--.', 'Q': '--.-',
                       'R': '.-.', 'S': '...', 'T': '-',
                       'U': '..-', 'V': '...-', 'W': '.--',
                       'X': '-..-', 'Y': '-.--', 'Z': '--..',
                       '1': '.----', '2': '..---', '3': '...--',
                       '4': '....-', '5': '.....', '6': '-....',
                       '7': '--...', '8': '---..', '9': '----.',
                       '0': '-----', ', ': '--..--', '.': '.-.-.-',
                       '?': '..--..', '/': '-..-.', '-': '-....-',
                       '(': '-.--.', ')': '-.--.-'}

    assert (char.upper() in MORSE_CODE_DICT for char in text),\
        "the arguments are bad"
    return ' '.join([MORSE_CODE_DICT[char.upper()] if char.upper() in
                     MORSE_CODE_DICT else char for char in text])


def main():
    try:
        assert (len(sys.argv) == 2), "the arguments are bad"
        assert (sys.argv[1].isalnum()), "the arguments are bad"
        print(sos(sys.argv[1]))
    except AssertionError as e:
        print(f"AssertionError: {e}")
    except Exception as e:
        print(f"Exception: {e}")
        return


if __name__ == "__main__":
    main()
