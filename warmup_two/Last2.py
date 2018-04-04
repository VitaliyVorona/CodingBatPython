def last2(str):
    str_pattern = str[-2:]
    str_index = 0
    counter = 0
    while str_index < len(str) - 2:
        if str_pattern in str[str_index:str_index + 2]:
            counter += 1
        str_index += 1
    return counter
