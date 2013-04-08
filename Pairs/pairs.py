no_of_elements, difference = raw_input().strip().split()
no_of_elements, difference = int(no_of_elements), int(difference)
elements = [int(i) for i in raw_input().strip().split()]

def pairs(elements, difference, no_of_elements):
    sorted_elements = sorted(elements)
    count = 0
    for index in range(no_of_elements):
        element = sorted_elements[index]
        for sub_index in range(index + 1, min(index + 1 + difference, no_of_elements)):
            if(element + difference == sorted_elements[sub_index]):
                count = count + 1
                break
    print count

pairs(elements, difference, no_of_elements)