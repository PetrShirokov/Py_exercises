def chunked(chunk, items):
    if chunk <= 0:
        return []
    index = 0
    result_lst = []
    while items[index:]:
        items_chunk = items[index:index + chunk]
        result_lst.insert(len(items), items_chunk)
        index += chunk
    return result_lst


print(chunked(2, [1, 2, 3, 4, 5, 6, 7])) # [[1, 2], [3, 4], [5, 6], [7]]
print(chunked(3, [1, 2, 3, 4, 5, 6, 7])) # [[1, 2, 3], [4, 5, 6], [7]]
print(chunked(3, 'abcdefHi!!!')) # ['abc', 'def', 'Hi!', '!!']
print(chunked (0, (1, 2, 3))) # []
print(chunked (2, (1, 2, 3))) # [(1, 2), (3,)]