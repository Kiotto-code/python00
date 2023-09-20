import string
import sys


def check_characters(input_string: str):
    """_summary_

    Args:
        input_string (str): input string received to be counted and checked 
                            their characters then printout their character sum
    """
    character_count = len(input_string)
    upper_count = 0
    lower_count = 0
    punctuation_count = 0
    space_count = 0
    digit_count = 0

    for char in input_string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
        elif char in string.punctuation:
            punctuation_count += 1
        elif char.isspace():
            space_count += 1
        elif char.isdigit():
            digit_count += 1

    print(f"The text contains {character_count} characters:")
    print(f"{upper_count} upper letters ")
    print(f"{lower_count} lower letters ")
    print(f"{punctuation_count} punctuation marks ")
    print(f"{space_count} spaces ")
    print(f"{digit_count} digits ")


def main():
    """_summary_
        check if the input is a string is handled by the argument acception or
        input() function reading from stdin
    """
    # input_string = "Hello, World! 123"
    # print("What is the text to count?")
    # print(sys.argv)
    try:
        if len(sys.argv) > 1:
            input_string = sys.argv[1]
            assert len(sys.argv) == 2, "more than one argument is provided"
        else:
            # input_string = input("What is the text to count?\n")
            input_string = sys.stdin.readline()  # Read a line from stdin
    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(1)
    except EOFError:
        print("\nCtrl+D (or Ctrl+Z on Windows) detected. Exiting...")
    except Exception as e:
        print(f"Exception: {e}")
    check_characters(input_string)


if __name__ == "__main__":
    main()
