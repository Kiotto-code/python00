def ft_filter(function, iterable) -> list:
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which \
function(item)
is true. If function is None, return the items that are true."""
    if function is None:
        return [item for item in iterable if item]
    return [item for item in iterable if function(item)]


def is_even(num):
    """return even number"""
    return num % 2 == 0


def main():
    """do the testing"""
    ft_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ft_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    ft_set = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

    even_numbers = ft_filter(is_even, ft_list)
    odd_numbers = ft_filter(lambda x: x % 2 != 0, ft_list)
    print("Even ft_list:", even_numbers)
    print("Odd ft_list:", odd_numbers)

    even_numbers = ft_filter(is_even, ft_tuple)
    odd_numbers = ft_filter(lambda x: x % 2 != 0, ft_tuple)
    print("Even ft_tuple:", even_numbers)
    print("Odd ft_tuple:", odd_numbers)
    
    even_numbers = ft_filter(is_even, ft_set)
    odd_numbers = ft_filter(lambda x: x % 2 != 0, ft_set)
    print("Even ft_set:", even_numbers)
    print("Odd ft_set:", odd_numbers)
    
    # ft_filter(None, None)
    # ft_filter(is_even, None)
    print(ft_filter(None, ft_list))

    copy = ft_filter.__doc__
    original = filter.__doc__
    
    print(copy)
    print(original)
    
    print(copy == original)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Exception: {e}")
