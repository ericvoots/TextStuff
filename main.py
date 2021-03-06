import re
import pandas as pd


'''
helpful links
https://stackoverflow.com/questions/4289331/how-to-extract-numbers-from-a-string-in-python
https://stackoverflow.com/questions/17686809/how-to-find-word-next-to-a-word-in-python

# dataframe part to remove placeholders in string columns
https://stackoverflow.com/questions/13682044/remove-unwanted-parts-from-strings-in-a-column
'''


def find_numbers(number_string):
    """

    :param number_string: comes from main_text_test
    :return: the numbers found in a list
    """

    # list comprehension to get digits
    number_list_comprehension = [int(s) for s in number_string.split() if s.isdigit()]

    # do regex in case there is no spaces and a double for digits
    number_list_regex = re.findall(r"\d+", number_string)

    number_list = list(set(number_list_comprehension) | set(number_list_regex))

    return number_list


def placeholder_function(string, placeholder_num_of_words):
    '''

    :param string:
    :param placeholder_num_of_words:
    :return:

    '''




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

        # ****PLACEHOLDER STEP with list_of_words *****


        # create empty string to append
        empty_string_backward = ''
        empty_string_forward = ''

        i = num_of_words
        # start loop for before words
        while i > 0:

            # can just replace this part with index num later if need but
            previous_word = list_of_words[list_of_words.index(str(number)) - i]

            # append space if not the first word
            if i != num_of_words:
                empty_string_backward += ' ' + previous_word

            else:

                empty_string_backward += previous_word

            # increment to stop while loop
            i += - 1

        # same as backwards steps only other order
        j = 0

        while j < num_of_words:

            next_word = list_of_words[list_of_words.index(str(number)) + j + 1]

            if j == num_of_words - 1:
                empty_string_forward += ' ' + next_word

            # for the first word
            else:

                empty_string_forward += next_word

            j += 1

        string_df = string_df.append({'id': id,
                                      'string': string,
                                      'match_num': idx + 1,
                                      'number': number,
                                      'word matches before': empty_string_backward,
                                      'word matches after': empty_string_forward},
                                      ignore_index=True)

    # remove placeholder strings leftover here before returning


    # final QA step to look for prior number in case not enough words

    return string_df


def save_dataframe_matches(save_mathces_df, output_path):
    '''

    :param save_mathces_df: dataframe you want to save off
    :param output_path: where the sas dataset goes and where the csv goes
    :return: nothing, saves to output location
    '''

    save_mathces_df.to_csv(output_path + 'matches.csv', index=False)


if __name__ == "__main__":

    # change this to get more or less words, much later for fancy stuff add argparse
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