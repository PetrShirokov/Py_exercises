def pair_sum(lst):
    pair_list = list(zip(lst, lst[1:]))
    sum_list = []
    for pair in pair_list:
        pair_sum = pair[0] + pair[1]
        sum_list.append(pair_sum)
    return sum_list


def triangle(line_num):
    "Returns line (№ line_num) in Pascal's triangle."
    if line_num == 0:
        return [1]
    sum_list = [1, 1]
    if line_num == 1:
        return sum_list
    for line in range(2, line_num + 1):
        sum_list = pair_sum(sum_list)
        sum_list.insert(0, 1)
        sum_list.append(1)
    return sum_list
