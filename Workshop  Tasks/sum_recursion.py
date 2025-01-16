def sum_until_index(list_of_numbers, index_point):
    # if the index is 0 it returns the first integer of the list
    if index_point == 0:
        return list_of_numbers[0]
    # returns the sum of the integer at the current index
    # plus the sum of the elements up to the previous index
    else:
        return list_of_numbers[index_point] + sum_until_index(list_of_numbers, index_point - 1)


integer_list = [8, 13, 101, 34, 55]
index = 3
sum_of_integers = sum_until_index(integer_list, index)
print(f"Sum of numbers until index {index}: is equal to {sum_of_integers}")
