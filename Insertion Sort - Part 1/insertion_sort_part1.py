def insertionSort(ar):
    def print_array(array):
        print ' '.join([str(element) for element in array])

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
        print_array(ar)

    if(ar[0] == ar[1]):
        ar[0] = element_to_insert;

    print_array(ar)

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)