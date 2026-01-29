def ft_count_harvest_recursive() -> None:
    days = int(input("Days until harvest: "))

    def ft_count_days(current_day) -> None:
        if (current_day > days):
            print("Harvest time!")
        else:
            print("Day", current_day)
            ft_count_days(current_day + 1)
    ft_count_days(1)
