"""
This module does all the steps nessesary to train the model
"""
from dataset_preprocessing_modules.dataset_process import filter_and_process_dataset
from dataset_preprocessing_modules.make_vocab import extract_vocabulary
from dataset_preprocessing_modules.dataset_to_numbers import dataset_to_numbers
from trainNN import train_nn

def main():
    dataset_conv_filename = filter_and_process_dataset()
    vocab_filename = extract_vocabulary(dataset_conv_filename)
    dataset_vocab_filename = dataset_to_numbers(dataset_conv_filename, vocab_filename)
    print("Dataset prepared", dataset_vocab_filename)
    train_nn(dataset_vocab_filename)
    print("Neural network trained", dataset_vocab_filename)
    print("To start generating messages, type:\n$ python3 runNN.py WORD NUMBER")


if __name__ == "__main__":
    main()

