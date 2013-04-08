import sys
data = sys.stdin.readlines()

def min_count_of_candies(no_of_children, children_score):
    candies_given_to_children = [1 for index in range(no_of_children)]

    def neighbours_candie_count_if_my_score_less_than_neighours(my_index, neighbours_index):
        if(children_score[my_index] > children_score[neighbours_index] and candies_given_to_children[my_index] <= candies_given_to_children[neighbours_index]):
            return candies_given_to_children[neighbours_index]
        return 0


    def give_candie_comparing_neighbours(child_index):
        candies_with_neighbours = [0]

        if(child_index != 0):
            candies_with_neighbours.append(neighbours_candie_count_if_my_score_less_than_neighours(child_index, child_index - 1))

        if(child_index != no_of_children - 1):
            candies_with_neighbours.append(neighbours_candie_count_if_my_score_less_than_neighours(child_index, child_index + 1))

        candies_given_to_children[child_index] = max(candies_with_neighbours) + 1


    def see_if_children_on_left_should_be_given_more_candies(child_index):
        for index in reversed(range(1, child_index + 1)):
            if(children_score[index - 1] > children_score[index] and candies_given_to_children[index - 1] <= candies_given_to_children[index]):
                candies_given_to_children[index - 1] = candies_given_to_children[index] + 1
            else:
                break

    for index in range(no_of_children):
        no_of_candies_given_to_child = candies_given_to_children[index]
        give_candie_comparing_neighbours(index)
        if(candies_given_to_children[index] != no_of_candies_given_to_child):
            see_if_children_on_left_should_be_given_more_candies(index)

    print(sum(candies_given_to_children))

no_of_children, children_scores = int(data[0]), [int(score) for score in data[1:]]
min_count_of_candies(no_of_children, children_scores)










