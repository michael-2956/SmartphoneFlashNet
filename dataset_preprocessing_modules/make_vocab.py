"""
This module extracts vocabulary from the given dataset file
"""

MINIMAL_FREQUENCY = 2

def extract_vocabulary(converted_dataset_filename):
    """
    This function extracts vocabulary from the given dataset file
    """
    vocab_filename = "vocab.txt"

    dataset = open(converted_dataset_filename, "r")
    word_num_dict = {}
    for line in dataset:
        for word in line.split():
            if word in word_num_dict:
                word_num_dict[word] += 1
            else:
                word_num_dict[word] = 1
    dataset.close()

    # write words to vocabulary in frequency order
    vocab_file = open(vocab_filename, "w")
    word_num = sorted(word_num_dict.items(), key=lambda kv: kv[1])
    frequent_words_num = sum([1 for el in word_num if el[1] >= MINIMAL_FREQUENCY])
    for word, _ in reversed(word_num):
        vocab_file.write(word + "\n")
    vocab_file.close()
    print(f"unique_words_number = {frequent_words_num}")

    return vocab_filename


def count_vocab_words(vocab_file="vocab.txt"):
    return sum(1 for line in open(vocab_file, "r"))


if __name__ == "__main__":
    extract_vocabulary("dataset_conv.txt")
