def ft_tqdm(lst):
    """progress bar for a list of items
    """
    total = lst[-1] + 1 - lst[0]
    print(total)
    # print(f"  0%|{'-' * 30}|{lst[0]}/{total}", end="", flush=True)
    bar_length = 30

    def ft_update(iteration):
        percent = "{:.0f}".format(100 * (iteration / float(total)))
        filled_length = int(bar_length * iteration // total)
        progress_bar = "|[" + "=" * filled_length + ">" \
            + "-" * (bar_length - filled_length) + "]"
        progress = int(total * float(percent) // 100)
        print(f"{percent.rjust(3)}%{progress_bar}|{progress}/{total}\
              \r", end="", flush=True)
        # print(f"\r{percent.rjust(3)}%{progress_bar}|{progress}/{total}\
        #       ", end="", flush=True)

    for i, elem in enumerate(lst):
        yield elem
        ft_update(i + 1)
    # for i, elem in enumerate(lst):
    #     yield elem
    #     ft_update(i + 1)

    # print()


if __name__ == "__main__":
    total_items = 333
    ft_tqdm(range(total_items))
    # for item in ft_tqdm(range(total_items)):
    #     pass
