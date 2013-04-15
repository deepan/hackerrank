def print_array(array):
    print ' '.join([str(element) for element in array])

def insert_right_most_element_in_place(ar):
    def compare_and_shift(array, index, no_to_compare_with):
        if(array[index] >= no_to_compare_with):
            array[index + 1] = array[index]
            return True
        return False

    element_to_insert = ar[-1]
    for index in reversed(range(len(ar) - 1)):
        if not compare_and_shift(ar, index, element_to_insert):
            ar[index + 1] = element_to_insert
            break

    if(len(ar) > 1 and ar[0] == ar[1]):
        ar[0] = element_to_insert;

    return ar


# Head ends here
def insertionSort(ar):
    for index in range(2, len(ar) + 1):
        array_subset = insert_right_most_element_in_place(ar[:index])
        ar = array_subset + ar[len(array_subset): ]
        print_array(ar)

# Tail starts here

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)