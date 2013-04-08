import sys
data = sys.stdin.readlines()

def get_suffixes(string):
    suffixes = set()
    string_len = len(string)
    for index in range(0, string_len):
        suffixes.add(string[index: string_len])
    return suffixes

def get_longest_common_prefix(string1, string2):
    longest_common_index = 0
    for index in range(len(string1)):
        try:
            if(string1[index] != string2[index]):
                return string1[0: longest_common_index]
            else:
                longest_common_index = longest_common_index + 1
        except IndexError:
            return string1[0: longest_common_index]

def compute_cumulative_substrings_count(suffixes):
    result = []

    for index in range(len(suffixes)):
        suffix = suffixes[index]
        substrings_count = len(suffix)
        previous_cumulative_substrings_count, previous_suffix = result[index - 1] if index != 0 else (0, '')
        length_of_longest_common_prefix = len(get_longest_common_prefix(suffix, previous_suffix))
        substrings_count = substrings_count - length_of_longest_common_prefix
        result.append((previous_cumulative_substrings_count + substrings_count, suffix))
    return result

def  binary_search_for_nearest_big_number(array, number):
    left_edge = 0
    right_edge = len(array) - 1

    if(number < 0 or number > array[right_edge]):
        return None
    if(number <= array[0]):
        return 0

    while right_edge - left_edge > 1:
        mid_index = (left_edge + right_edge) // 2
        mid_val = array[mid_index]
        if(mid_val < number):
            left_edge = mid_index
        elif(mid_val > number):
            right_edge = mid_index
        elif(mid_val == number):
            return mid_index

    if(array[left_edge] == number):
        return left_edge

    return  right_edge

def parse_input():
    no_of_strings = int(data[0])
    strings_input, queries_input = data[:no_of_strings + 1], data[no_of_strings + 1:]
    strings = [strings_input[index].strip() for index in range(1, no_of_strings + 1)]
    no_of_queries = int(queries_input[0])
    queries = [int(queries_input[index]) for index in range(1, no_of_queries + 1)]
    return (strings, queries)

def find_strings():
    strings, queries = parse_input()
    suffixes = set()

    [suffixes.update(get_suffixes(string)) for string in strings]
    suffixes_with_cumulative_substrings_count = compute_cumulative_substrings_count(sorted(list(suffixes)))
    cumulative_substrings_count = [count for count, suffix in suffixes_with_cumulative_substrings_count]

    for query in queries:
        index = binary_search_for_nearest_big_number(cumulative_substrings_count, query)
        if(index == None):
            print('INVALID')
        else:
            cumulative_index, suffix = suffixes_with_cumulative_substrings_count[index]
            previous_cumulative_index, previous_suffix = suffixes_with_cumulative_substrings_count[index - 1] if index != 0 else (0, '')
            delta_index = query - previous_cumulative_index
            if(delta_index == 0):
                print(suffix)
            else:
                longest_common_prefix = get_longest_common_prefix(suffix, previous_suffix)
                len_of_longest_common_prefix = len(longest_common_prefix)
                print(longest_common_prefix + suffix[len_of_longest_common_prefix: len_of_longest_common_prefix + delta_index])

find_strings()
