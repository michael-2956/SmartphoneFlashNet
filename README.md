# Telegram Speaker (tensorflow 2.4, python 3.8)

## Table of Contents

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
  - [Collect the Dataset](#collect-the-dataset)
  - [Train & Run The model](#train-&-run-the-model)
- [How clusters look like](#how-clusters-look-like)
- [Author](#author)

## Description

This program collects a message dataset from open telegram chats. It then uses it to trin a neural network, which learns to simulate human speech. In `dataset_full.txt`, messages collected from Mi A1 and Mi 9T community chats are stored.\
The idea behind this program was to try to simulate human speech using a smalll net.\
Please note that this program is under **testing & development**. The main pending problems include:
1) The `collect_dataset.py` script should be modified to accept special non-unicode symbols.
2) The program module structure should be rebuilt.

## Installation

First, clone the repository into you current folder:\
```$ git clone https://github.com/michael-2956/SmartphoneFlashNet.git```\
Get into the root folder of the repository:\
```$ cd SmartphoneFlashNet```\
For the scripts to run, you need tensorflow, pytg and numpy preinstalled. To install all the needed libraries in your activated local or global environment, run:\
```$ pip install -r requirements.txt```\
When all the needed libraries are installed, you are ready to execute the train & run scripts.

## Usage

### Collect the Dataset

To start collecting the dataset, you need telegram-cli to be running on some port in json mode. For example:\
```$ screen ./path/to/telegram-cli -W -P 4480 --json -p main```\
Where `4480` is the port number and `main` is the user session. To detach the `screen` session, press `Ctrl + a` followed by `d`.\
Now you are ready to run the collector script. It will save all the incoming messages to `dataset.txt`. To do this, run the following:\
```$ python3 collect_dataset.py 4480```\
Where 4480 is the port number. The script now should start appending the messages to `dataset.txt`. To append the resulting dataset to the current one, run the following:\
```$ cat dataset.txt >> dataset_full.txt```

### Train & Run The model
To train the model, run the following:\
```$ python3 dataset_train.py```\
It uses the `dataset_full.txt` file by default. To train on custom file, type the following:\
```$ python3 dataset_train.py dataset.txt```\
When the network is trained, the `model.ckpt` files will appear in the current folder. You can now run the network by the following:\
```$ python3 runNN.py```

## Author

Mykhailo Bondarenko