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
    vocab = open("vocab.txt", "r")
    voc = [word[:-1] for word in vocab] + ["RANDOM"]
    model = keras.Sequential([
        keras.layers.Dense(5000, activation=tf.nn.relu),
        keras.layers.Dense(VOC_SIZE, activation=tf.nn.softmax)
    ])
    model.load_weights("model.ckpt")

    print("\nTensorflow model successfully loaded!\n")
    print("To stop generating, simply press the Enter key.")

    while True:
        starting_word = input("Start you message: ")
        if starting_word == '':
            break
        words_num = int(input("How many words whould you like to generate? "))
        print("Generating...")
        print("Message:", essay(voc, model, starting_word, words_num), '\n')


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
