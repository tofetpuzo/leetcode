def missing_num(full_set, partial_set):
    xor_sum = 0
    for num in full_set:
        xor_sum ^= num
        
    for num in partial_set:
        xor_sum ^= num

    return xor_sum
print(missing_num([1, 4, 5, 6, 8, 10, 7, 15], [1, 4, 5, 7, 6, 8, 10]))