"""
This module creates and trains the neural network.
"""
import numpy as np
import tensorflow as tf
from tensorflow import keras
from dataset_preprocessing_modules.make_vocab import count_vocab_words

tf.get_logger().setLevel('ERROR')

VOC_SIZE = count_vocab_words()

def train_nn(dataset_vocab_filename):
    """
    This function creates and trains the neural network.
    """
    model_filename = 'model.ckpt'

    dataset_voc = open(dataset_vocab_filename, "r")
    train_msg_in = []
    train_msg_out = []
    for samp in dataset_voc:
        i = 0
        msg_in = [0] * VOC_SIZE
        msg_out = 0
        for word in samp.split():
            i += 1
            if i <= 3:
                msg_in[int(word)] = 1
            if i == 4:
                msg_out = int(word)
        train_msg_in.append(msg_in)
        train_msg_out.append(msg_out)

    order = np.random.shuffle(np.arange(len(train_msg_in) - 1))
    train_msg_in = np.array(train_msg_in)[order][0]
    train_msg_out = np.array(train_msg_out)[order][0]

    test_cut = -len(train_msg_in) // 10

    test_msg_in = train_msg_in[test_cut:]
    test_msg_out = train_msg_out[test_cut:]

    train_msg_in = train_msg_in[:test_cut]
    train_msg_out = train_msg_out[:test_cut]

    print(f"--- Train/test split: {train_msg_in.shape[0]}/{test_msg_in.shape[0]}")

    model = keras.Sequential([
        keras.layers.Dense(5000, activation=tf.nn.relu),
        keras.layers.Dense(VOC_SIZE, activation=tf.nn.softmax)
    ])

    model.compile(optimizer='adam',
              loss=keras.losses.sparse_categorical_crossentropy,
              metrics=['accuracy'])

    cp_callback = tf.keras.callbacks.ModelCheckpoint(model_filename,
                                                 save_weights_only=True,
                                                 verbose=1)
    
    model.fit(
        train_msg_in, train_msg_out, epochs=5, 
        validation_data = (test_msg_in, test_msg_out), 
        callbacks = [cp_callback]
    )

    _, test_acc = model.evaluate(test_msg_in, test_msg_out)
    print('--- Test accuracy:', test_acc)
    model.summary()

    return model_filename
    

if __name__ == "__main__":
    train_nn("dataset_voc.txt")
