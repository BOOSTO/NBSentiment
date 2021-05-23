import numpy as np

def preprocess(train_raw, test_raw):
    train     = sanitize(train_raw)
    test      = sanitize(test_raw)
    vocab     = get_vocab(train, test)
    train     = process(train, vocab)
    test      = process(test, vocab)

    write_data(vocab, train, test)
    return vocab, train, test

def sanitize(data):
    data_clean = []
    f = open(data, 'r')
    lines = f.readlines()
    punc = '''\n\t!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for line in lines:
        for char in line:
            if char in punc:
                line = line.replace(char, "")
        line = line.lower()
        data_clean.append(line)

    return data_clean
    
def get_vocab(train, test):
    d = {}
    vocab = []

    for line in train:
        words = line.split()
        for word in words:
            if not word in d:
                d[word] = True
                vocab.append(word)

    for line in test:
        words = line.split()
        for word in words:
            if not word in d:
                d[word] = True
                vocab.append(word)

    return vocab

def process(data, vocab):
    output = []
    for line in data:
        clss = line[-2]
        line = line[0:-2]
        arr = []
        for word in vocab:
            if word in line:
                arr.append(1)
            else:
                arr.append(0)
        arr.append(0 if clss == '0' else 1)
        output.append(arr)

    return output

def write_data(vocab, train, test):
    # TODO finish this shiz

    print("TODO lmao")

def print_guesses(vocab, data, predictions):
    # TODO finish this shiz

    print("guess")