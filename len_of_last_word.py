def length_of_last_word(seq):
    elements = list()
    for (_, elem) in enumerate(seq):
        elements.append(elem)
    elements.reverse()
    count = 0
    passing_units = [' ', '\n', '\t']
    begin_count = False
    for symbol in elements:
        skip = (symbol in passing_units)
        if count == 0 and not skip:
            begin_count = True
        if begin_count and not skip:
            count += 1
        if count > 0 and skip:
            return count
    return count
