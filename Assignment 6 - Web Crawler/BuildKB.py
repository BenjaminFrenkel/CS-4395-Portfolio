"""

Names: Justin Hardy, Benji Frenkel
NETID: JEH180008
Class: Human Language Technologies (CS 4395.001)
Professor: Dr. Mazidi

"""

import os
import pickle
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Define global variables
output_folder = "output"
output_file_name = "linktext"


def clean_text(text):
    """
    Cleans a given text in preparation for NLP.

    :param text: text to clean up
    :return: cleaned up text
    """

    #remove new lines and tabs from the text
    text = text.replace("\n", "")
    text = text.replace("\t", "")

    tokenized_text = word_tokenize(text)


    return tokenized_text


def extract_important_terms(token_list: list):
    """
    Extracts important terms from a list of texts, and ranks them by frequency.

    :param token_list: List of texts to extract terms from.
    :return: List of important terms (by sorted by frequency).
    """
    # Lowercase all tokens
    clean_token_list = []
    for i in range(len(token_list)):
        tokens = token_list[i]
        clean_token_list.insert(len(clean_token_list), [token.lower() for token in tokens
                                                        if token.isalpha() and token not in stopwords.words("english")])
    # print("Cleaned Tokens:\n", clean_token_list)

    # Create dictionary to store counts
    token_dict = {}

    # Loop through tokens of each file, get counts
    for tokens in clean_token_list:
        for token in tokens:
            if not token_dict.keys().__contains__(token):
                # add token to dict
                token_dict[token] = 1
            else:
                # update count of token in dict
                token_dict[token] += 1

    # Sort tokens by frequency into a list (most frequent -> least frequent)
    sorted_token_list = [tup[0] for tup in sorted(token_dict.items(), key=lambda x: x[1], reverse=True)]
    # sorted_token_list = [tup for tup in sorted(token_dict.items(), key=lambda x: x[1], reverse=True)]
    top_tokens = sorted_token_list[:25]
    # print(top_tokens)

    # Return the top 25 tokens
    return top_tokens


def filter_top_10_terms(term_list: list):
    """
    This function will select 10 terms from a list of top 25 words and return those top 10 terms in a list.
    Selection is partially manual as per the instructions, but includes some automatic word filtering.

    :param term_list: List of tokens to extract terms from.
    :return: List of top 10 terms selected from the term_list
    """
    # Requires Benji's code to continue
    return


def important_terms_extraction_test():
    # For testing on this branch
    test_texts = [
        ['This', 'is', 'an', 'example', 'tokenized', 'sentence', ',', 'to', 'use', 'for', 'my', 'function', 'testing', '.'],
        ['This', 'is', 'another', 'example', 'tokenized', 'sentence', '.', 'I', 'use', 'for', 'my', 'function', 'testing', '!'],
        ['This', 'is', 'another', 'example', 'tokenized', 'sentence', '.', 'Is', 'it', 'good', 'for', 'my', 'function', 'testing', '?'],
        ['Just', 'a', 'short', 'tokenized', 'sentence', '.'],
        ['I', 'do', 'not', 'know', 'what', 'else', 'to', 'write', 'for', 'these', '!']
    ]
    top_25_terms = extract_important_terms(test_texts)
    print("Top 25:", top_25_terms)
    top_10_terms = filter_top_10_terms(top_25_terms)
    print("Top 10", top_10_terms)
    return


def main():
    """
    Builds a knowledge base using the texts read in from the pickle files from a given output folder and set of
    15 output files.

    :return: exit code (0 = success, 1 = error)
    """
    # Get global
    global output_folder, output_file_name

    # Read pickle files
    print("Loading pickles...")
    texts = []
    for i in range(15):
        # Go from 1-15 instead of 0-14
        _i = i+1

        # Read pickle file
        texts.insert(len(texts), pickle.load(open(os.path.join(output_folder, output_file_name + str(_i) + ".p"), "rb")))
    print("Done loading pickles.")

    # ...


    # Program complete, terminate the program. (exit code 0)
    exit(0)


if __name__ == "__main__":
    main()
