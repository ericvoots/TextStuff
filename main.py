import re


'''
helpful links
https://stackoverflow.com/questions/4289331/how-to-extract-numbers-from-a-string-in-python
https://stackoverflow.com/questions/17686809/how-to-find-word-next-to-a-word-in-python
'''

def find_numbers(number_string):
    """

    :param number_string: comes from main_text_test
    :return: the numbers found in a list
    """

    number_list = [int(s) for s in number_string.split() if s.isdigit()]

    return number_list

def main_text_test(id, string, num_of_words):
    '''
    :param id: how to identify the string
    :param string: called from main
    :param num_of_words: how many words to extract prior to each number
    :return: master_string_dict of all numbers and the first two characters
    '''

    print(f'This is the string \n{string}')

    # get the numbers
    number_string_list = find_numbers(string)

    temp = []

    # inner string dict
    inner_string_dict = {}

    for idx, number in enumerate(number_string_list):
        list_of_words = string.split()

        # create empty string to append
        empty_string = ''

        i = num_of_words
        # start loop
        while i > 0:
            previous_word = list_of_words[list_of_words.index(str(number)) - i]

            i+=-1

            # append space
            if i != num_of_words:
                empty_string += ' ' + previous_word
            else:
                empty_string += previous_word

        #print(f'The previous two words for {number} are {empty_string}')

        # that way if there are duplicates have index of match
        number = str(idx) + str(number)

        master_dict_key = 'id-' + str(id) + ' match_num_' + str(idx)

        print(master_dict_key)
        # init master dict
        master_string_dict = {}

    return master_string_dict


if __name__ == "__main__":

    id = 1

    test_string = 'The first number is 1111 but the number 2222 is not far behind'

    num_of_words = 2

    main_text_test(id=id, string=test_string, num_of_words=num_of_words)