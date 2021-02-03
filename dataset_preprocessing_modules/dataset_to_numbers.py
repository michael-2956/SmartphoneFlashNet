"""
This module converts the dataset into id's of vocabulary entries.
"""

def dataset_to_numbers(dataset_conv_filename, vocab_filename):
    """
    This function converts the dataset into id's of vocabulary entries.
    """
    numbers_dataset_name = "dataset_voc.txt"

    dataset_conv = open(dataset_conv_filename, "r")

    vocab = open(vocab_filename, "r")
    voc = [word[:-1] for word in vocab.readlines()] + ["RANDOM"]

    dataset_voc = open(numbers_dataset_name, "w")

    for samp in dataset_conv:
        line_to_write = ""
        for word in samp.split():
            if word not in voc:
                line_to_write += str(voc.index("RANDOM")) + " "
            else:
                line_to_write += str(voc.index(word)) + " "
        dataset_voc.write(line_to_write + "\n")
    dataset_voc.close()

    return numbers_dataset_name


if __name__ == "__main__":
    dataset_to_numbers("dataset_conv.txt", "vocab.txt")
