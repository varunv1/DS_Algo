def string_matching_bruteforce(input_str, pattern):
    # for each item in string, we match the pattern
    # we only need to match for n-m+1 (m = lenght of pattern,
    #  no need to match last m-1 items)
    if not pattern:
        return 0
    n = len(input_str)
    m = len(pattern)
    for i in range(n-m+1):
        input_str_idx = i
        pattern_index = 0
        while input_str_idx < n and pattern_index < m and input_str[input_str_idx] == pattern[pattern_index]:
            input_str_idx += 1
            pattern_index += 1
        if pattern_index == m:
            return i
    return -1


print(string_matching_bruteforce('abcdefghi', 'bcd'))
