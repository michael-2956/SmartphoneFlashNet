"""
This module generates a message using the neural net.
"""
import sys
import numpy as np
import tensorflow as tf
from tensorflow import keras
from dataset_preprocessing_modules.make_vocab import count_vocab_words

tf.get_logger().setLevel('ERROR')

VOC_SIZE = count_vocab_words()

def main():
    """
    Main function generating the message via model.ckpt
    """
    if len(sys.argv) != 3:
        print(f"Usage:\n{sys.argv[0]} WORD NUMBER")
        return

    starting_word = sys.argv[1]
    words_num = int(sys.argv[2])

    vocab = open("vocab.txt", "r")
    voc = [word[:-1] for word in vocab] + ["RANDOM"]
    model = keras.Sequential([
        keras.layers.Dense(5000, activation=tf.nn.relu),
        keras.layers.Dense(VOC_SIZE, activation=tf.nn.softmax)
    ])
    model.load_weights("model.ckpt")

    print("\nTensorflow model successfully loaded!\n")
    print("Generating message...")
    print("\nMessage:", essay(voc, model, starting_word, words_num), '\n')

    while True:
        ans = input("Do you want to continue generating? (Y/n): ")
        if ans in ['Y', 'y', '']:
            starting_word = input("Start you message: ")
            print("Generating...")
            print("Message:", essay(voc, model, starting_word, words_num), '\n')
        elif ans in ['n', 'N']:
            break


def essay(voc, model, start, words_num):
    """
    This function generates the message using preloaded model.ckpt
    """
    ess = start.lower()
    for _ in range(words_num):

        msg_in = [0] * VOC_SIZE

        k = 0

        for word in ess.split()[-3:]:
            k += 1
            if word in voc:
                msg_in[voc.index(word)] = k
            else:
                msg_in[VOC_SIZE - 1] = 1

        inp = []
        inp.append(msg_in)
        inp = np.array(inp)

        ess += " " + voc[np.argmax(model.predict(inp))]
    return ess


if __name__ == '__main__':
    main()
