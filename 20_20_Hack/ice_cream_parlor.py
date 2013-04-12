import sys

class IceCreamParlor(object):
    def __init__(self, prices):
        self.prices = prices
        self.price_map = {}

    def get_flavor(self, money):
        for index, price in enumerate(self.prices):
            index += 1
            pending_money = money - price
            other_flavor_index = self.price_map.get(pending_money, -1)
            if other_flavor_index is not -1:
                return index, other_flavor_index
            else:
                self.price_map[price] = index


def parse_input_and_process():
    data = sys.stdin.readlines()
    no_of_samples = int(data[0])

    def process_sample(index):
        input_start_ln = index * 3 + 1
        money = int(data[input_start_ln])
        no_of_flavors = int(data[input_start_ln + 1])
        flavor_prices = [int(price) for price in data[input_start_ln + 2].split()]
        return IceCreamParlor(flavor_prices).get_flavor(money)

    def print_output(first_flavor_index, second_flavor_index):
        print '{0} {1}'.format(*(
            (first_flavor_index, second_flavor_index) if first_flavor_index < second_flavor_index else (
                second_flavor_index, first_flavor_index)))

    [print_output(*process_sample(sample_index)) for sample_index in range(no_of_samples)]

parse_input_and_process()


