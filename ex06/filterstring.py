import sys
from ft_filter import ft_filter


def main():
    """use lambda to run the function ft_filtersring
    """
    assert len(sys.argv) == 3, "the arguments are bad"
    string = sys.argv[1].split()
    integer = int(sys.argv[2])

    assert [char for char in string if char.isalpha()], "the arguments are bad"

    print(list(ft_filter((lambda s: len(s) > integer), string)))


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
    except ValueError:
        print("AssertionError: the arguments are bad")
    except Exception as e:
        print(f"Exception: {e}")
