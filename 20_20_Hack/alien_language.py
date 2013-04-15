import sys

def multiply(numbers):
    return reduce(lambda acc, number: acc * number, numbers, 1)

def possible_words_count(alphabet_letters_count, word_length):
    no_of_low_freq_letters = alphabet_letters_count // 2
    no_of_high_freq_letters = alphabet_letters_count - no_of_low_freq_letters

    possible_letter_count_to_form_high_freq_ending_words = [alphabet_letters_count for i in range(word_length - 1)] + [no_of_high_freq_letters]
    no_of_high_freq_letter_ending_words = multiply(possible_letter_count_to_form_high_freq_ending_words)

    def find_no_of_words_with_successive_low_freq_letters():
        no_of_words_with_successive_low_freq_letters = 0
        for i in range(word_length - 2):
            possible_letter_counts = list(possible_letter_count_to_form_high_freq_ending_words)
            possible_letter_counts[i] = no_of_low_freq_letters
            possible_letter_counts[i + 1] = no_of_low_freq_letters
            if i > 0:
                possible_letter_counts[i - 1] = no_of_high_freq_letters

            no_of_words_with_successive_low_freq_letters += multiply(possible_letter_counts)
        return no_of_words_with_successive_low_freq_letters

    return no_of_high_freq_letter_ending_words - find_no_of_words_with_successive_low_freq_letters()


def parse_input_and_process():
    #data = sys.stdin.readlines()
    data = ['1', '3 2']
    no_of_samples = int(data[0])

    def read_input(index):
        input_ln = index + 1
        alphabet_letters_count, word_length = [int(input) for input in data[input_ln].split()]
        return alphabet_letters_count, word_length

    def process_sample(sample_index):
        return possible_words_count(*read_input(sample_index))

    def print_output(word_count):
        print word_count % 100000007

    [print_output(process_sample(sample_index)) for sample_index in range(no_of_samples)]

parse_input_and_process()



