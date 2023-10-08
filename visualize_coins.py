from collections import Counter
def visualize(coins, bar_char="₽"):
    """Visualize money in a money box."""
    keys_count = Counter(coins)
    keys = list(sorted(Counter(coins)))
    lines_in_graph = max(keys_count.values()) + 1
    zero_line = ""
    for i in range(len(keys)):
        space = " " if keys[i] >= 10 else "  "
        if i == len(keys) - 1:
            space = ""
        zero_line += str(keys[i]) + space
    first_line = "-" * (3 * len(keys) - 1)
    res_line = ""
    for line_num in range(lines_in_graph):
        for i_in_line in range(len(keys)):
            gap = " "
            current_coin = keys[i_in_line]
            coin_sum = keys_count[current_coin]
            str_num_reverse = lines_in_graph - line_num - 1
            if i_in_line == len(keys_count) - 1:
                gap = "\n"
            if line_num == lines_in_graph - 1 and i_in_line == len(keys) - 1:
                gap = ""
            if str_num_reverse < coin_sum:
                el = bar_char * 2
            if str_num_reverse == coin_sum:
                space = " " if coin_sum < 10 else ""
                el = str(coin_sum) + space
            elif lines_in_graph-line_num - 1 > coin_sum:
                el = "  "
            res_line += el + gap
    res_line += '\n' + first_line + '\n' + zero_line
    return res_line

print(visualize((10,1,1,1,1,1,20,20,20,2,2,2,2,3,3,3,3)))
print(visualize((10,1,1,1,1,1,20,20,20,2,2,2,2,3,3,3,3), bar_char='$'))