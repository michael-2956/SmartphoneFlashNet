"""
This module filters and processes the dataset file for the network to work
"""
import string
import re

FORBIDDEN_WORDS = ["https://botsup.me/", "@multifeed_edge_bot"]
MINIMUM_WORDS = 4
CUSTOM_REPLACEMENTS = [(r'kNUM', 'k20'), (r'aNUM', 'a1')]

def filter_and_process_dataset(dataset_filename="dataset_full.txt"):
    """
    This function filters and processes the dataset file for the network to work
    """
    conv_filename = "dataset_conv.txt"
    dataset = open(dataset_filename, "r")
    out = open(conv_filename, "w")
    i = 0
    used_entries = set()
    ds_size = 0
    words_num = 0
    for line in dataset.readlines():
        i += 1
        if i % 2 == 1:
            words_num = int(line)
        else:
            if words_num >= MINIMUM_WORDS:
                # ignore forbidden words
                ignore = False
                for f_word in FORBIDDEN_WORDS:
                    if f_word in line.split():
                        ignore = True
                        break
                if ignore:
                    continue
                # convert to lower case
                line = line.lower()
                # replace some unique statements
                line = re.sub(r'<[^<>]+>', '', line)
                line = re.sub(r'[0-9]+', 'NUM', line)
                line = re.sub(r'(http|https)://[^\s]*', 'HTTPADDR', line)
                line = re.sub(r'[^\s]+.zip', 'ZIP', line)
                line = re.sub(r'[^\s]+@[^\s]+', 'EMAILADDR', line)
                line = re.sub(r'@[^\s]+', 'TAG', line)
                line = re.sub(r'#[^\s]+', '', line)
                line = re.sub(r'/[^\s]+', '', line)
                # custom replacements for current dataset
                for reg_str, rep_to_str in CUSTOM_REPLACEMENTS:
                    line = re.sub(reg_str, rep_to_str, line)
                # remove punctuation
                line = line.translate(str.maketrans('', '', string.punctuation))
                # split line into words & write results to file
                line_words = line.split()
                for j in range(3, len(line_words)):
                    new_entry = str(" ".join(line_words[j - 3:j + 1])) + "\n"
                    if new_entry not in used_entries:
                        out.write(str(" ".join(line_words[j - 3:j + 1])) + "\n")
                        used_entries.add(new_entry)
                        ds_size += 1
    print("dataset_size =", ds_size)
    return conv_filename


if __name__ == "__main__":
    filter_and_process_dataset("dataset_full.txt")
