def running_sum_of_1d_Array(n):
    new_lsr = []
    if n is []:
        return 0
    else:
        lst_sum = 0
        lst_sum += n.pop(0)
        new_lsr.append(lst_sum)
        return running_sum_of_1d_Array(n)
    return new_lsr


nums = [1, 2, 3, 4]
print(running_sum_of_1d_Array(nums))
