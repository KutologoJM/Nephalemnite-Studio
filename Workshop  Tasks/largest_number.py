def largest_number(list_of_integers, index=0, largest_num=None):
    """
    Find the largest number in a list of integers using recursion.

    Parameters:
    - list_of_integers (list): A list of integers used as an argument.
    - index (int): The current index being checked in the list. Default is 0.
    - largest_num (int): The largest number found so far. Default is None.

    Returns:
    - The largest number found after index has matched the length of the list.
    """

    if index == 0:
        largest_num = list_of_integers[0]  # Initialize largest_num with the first index of the list

    if index == len(list_of_integers):
        return largest_num
    else:
        if list_of_integers[index] > largest_num:
            largest_num = list_of_integers[index]
        return largest_number(list_of_integers, index + 1, largest_num)


print(largest_number([23, 9, 17, 17, 26, 4, 11, 11, 19, 12]))
