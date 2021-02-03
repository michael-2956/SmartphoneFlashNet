from pytg.receiver import Receiver
from pytg.sender import Sender
from pytg.utils import coroutine
from pytg import exceptions

# Helper libraries
import numpy as np
import time
import math
import threading
import random
import re
import string
import sys
import logging

sender = 0
receiver = 0

DATASET_FILENAME = "dataset.txt"

def main():
    """
    starts dataset collector on port provided in sys.argv[1], where telegram-cli runs.
    """

    arg_port = int(sys.argv[1])
    logging.basicConfig(filename="dataset_collector.log", level=logging.INFO)

    receiver = Receiver(host="localhost", port=arg_port)
    sender = Sender(host="localhost", port=arg_port)

    receiver.start()

    receiver.message(message_rec(sender))

    receiver.stop()


@coroutine
def message_rec(sender):
    dataset_file = open(DATASET_FILENAME, "a+")
    file_counter = 0
    messages_set = set()
    while True:
        msg = (yield)

        if msg.event != "message":
            continue
        if msg.own:
            continue
        if msg.text is None:
            continue  

        # if message text not in set:
        if not (msg.text in messages_set):
            messages_set.add(msg.text)
            # try to write it to a file
            data_words = (msg.text).split(' ')
            try:
                dataset_file.write(
                    str(len(data_words)) + "\n" 
                    + str(" ".join(data_words)) + "\n"
                )
                dataset_file.flush()

                file_counter += 1
                # update the file every 100 messages
                if file_counter % 100 == 0:
                    dataset_file.close()
                    dataset_file = open(DATASET_FILENAME, "a+")
            except Exception as e:
                # a shortcut test for emojis and other non-text junk
                print(
                    "Exception occured at message_rec while trying to write to file. e:", e
                )


if __name__ == '__main__':
    main()
