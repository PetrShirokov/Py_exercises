def find_range(lst):
    range_end = lst[0]
    range_len = 1
    for i in range(1, len(lst)):
        if lst[i] == lst[i - 1] + 1:
            range_end = lst[i]
            range_len = i
            continue
        break
    range_begin = lst[0]
    if range_begin != range_end:
        return "{}->{}".format(range_begin, range_end), range_len
    return "", range_len

def summary_ranges(long_lst):
    result_list = []
    index = 0
    while index < len(long_lst):
        current_range, range_len = find_range(long_lst[index:])
        if current_range:
            result_list.append(current_range)
        index += range_len
    return result_list

long_lst = [1, 2, 3, 4, 8, 9, 7, 8, 9, 0]
print(summary_ranges(long_lst))

