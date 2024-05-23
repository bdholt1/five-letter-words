
import numpy as np
import itertools

word_bitmask_dictionary = {}

def get_word_bitmask(word):
    if word not in word_bitmask_dictionary:
        word_bitmask = np.zeros(26)
        for letter in word:
            index = ord(letter) - 97 # 'a' is 97 in ascii
            word_bitmask[index] += 1
        # print("adding '{}' with bitmask {} to dictionary".format(word, word_bitmask))
        word_bitmask_dictionary[word] = word_bitmask
    return word_bitmask_dictionary[word]


def is_word_unique_letters(word):
    bitmask = get_word_bitmask(word)
    return np.all(bitmask <= 1)


def is_25_unique_letters(five_words):
    arr = np.zeros(26)
    for word in five_words:
        arr += get_word_bitmask(word)
        if np.any(arr > 1):
            return False
    return arr.sum() == 25


def find_five_uniques(words):
    uniques = []
    for combination in itertools.combinations(words, 5):
        # print("checking combination {}".format(combination))
        if is_25_unique_letters(combination):
            print("found a combination of 25 unique characters".format(combination))
            uniques.append(combination)
    return uniques


def main():    
    words = []
    with open('sgb-words.txt', "r") as txtfile:
        for line in txtfile:
            candidate_word = str(line.rstrip())
            if is_word_unique_letters(candidate_word):
                words.append(candidate_word)

    print("looking for 25 uniques from a list of {} words".format(len(words)))
    unique_combinations = find_five_uniques(words)
    for combo in unique_combinations:
        print("these 5 words cover 25 letters: {}".format(combo))

if __name__ == "__main__":
    main()