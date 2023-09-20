import sys


def checkodd(n: int) -> str:
    if n % 2 == 0:
        return "I'm Even"
    else:
        return "I'm Odd"


# while True:
# 	user_input = input()
# 	if user_input != "":
# 		break

# args = user_input.split()  # Split the input string into individual arguments


try:
    if len(sys.argv) == 1:
        pass
    elif len(sys.argv) != 2:
        raise AssertionError("more than one argument is provided")
    else:
        user_input = int(sys.argv[1])
        number = int(user_input)
        result = checkodd(number)
        print(f"{result}.")

except AssertionError as e:
    print(f"AssertionError: {e}")
except ValueError:
    print("AssertionError: Input must be an integer.")
except Exception as e:
    print(f"Exception: {e}")
