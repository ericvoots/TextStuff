import re
import pandas as pd


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

    # get the numbers
    number_string_list = find_numbers(string)

    # init dataframe with needed columns
    string_df = pd.DataFrame(columns=['id', 'string', 'match_num', 'number',
                                      'word matches before', 'word matches after'])

    # if needed a step to clean the string here and call another created function
    # this would be a place to filter PII prior to going forward


    # loop through the string and keep indexes
    for idx, number in enumerate(number_string_list):
        list_of_words = string.split()

        # create empty string to append
        empty_string_backward = ''
        empty_string_forward = ''

        i = num_of_words
        # start loop for before words
        while i > 0:

            # here is where you change to forward or backwards

            # find index of where to get word and is out of range
            index_num = list_of_words.index(str(number)) - i

            if index_num >= 0:

                # can just replace this part with index num later if need but
                previous_word = list_of_words[list_of_words.index(str(number)) - i]

                # append space if not the first word
                if i != num_of_words:
                    empty_string_backward += ' ' + previous_word

                else:

                    empty_string_backward += previous_word

            else:

                pass

            # increment to stop while loop
            i += - 1


        # same as backwards steps only other order

        j = 0

        next_word = None
        while j < num_of_words and next_word is None:

            # find index of where to get word and is out of range
            index_num = list_of_words.index(str(number)) + j + 1

            print('index num test ****** ', index_num)

            next_word = None

            while next_word is None:
                try:
                    next_word = list_of_words[list_of_words.index(str(number)) + j + 1]

                    if j != num_of_words:
                        empty_string_forward += ' ' + next_word

                    else:
                        empty_string_forward += ' ' + next_word

                    j += 1

                except IndexError as error:

                    # find index of where to get word and is out of range
                    index_num = list_of_words.index(str(number)) + j + 1

                    next_word = list_of_words[list_of_words.index(str(number)) + j]

                    print('index num test ****** ', index_num)

                    j += 1


        string_df = string_df.append({'id': id,
                                      'string': string,
                                      'match_num': idx + 1,
                                      'number': number,
                                      'word matches before': empty_string_backward,
                                      'word matches after': empty_string_forward},
                                      ignore_index=True)


    return string_df


def save_dataframe_matches(save_mathces_df, output_path):
    '''

    :param save_mathces_df: dataframe you want to save off
    :param output_path: where the sas dataset goes and where the csv goes
    :return: nothing, saves to output location
    '''

    save_mathces_df.to_csv(output_path + 'matches.csv', index=False)


if __name__ == "__main__":

    # change this to get more or less words
    num_of_words = 2

    # this is the SQL part here******** test_df is whatever comes from SQL
    test_df = pd.read_csv('test.csv')

    # loop through the dataframe for each id and string

    master_df = pd.DataFrame(columns=['id', 'string', 'match_num', 'number',
                                      'word matches before', 'word matches after'])

    # create lists to loop through from SQL pull
    id_list = test_df['id'].tolist()
    string_list = test_df['string'].tolist()

    # separate loop out here, loop through each string and change the next 3 items as needed
    for idx, id in enumerate(id_list):

        id = id

        string=string_list[idx]

        match_df = main_text_test(id=id, string=string, num_of_words=num_of_words)

        # append master in loop match_df
        master_df = master_df.append(match_df)

    save_dataframe_matches(master_df, 'C:\\textstuff\\')