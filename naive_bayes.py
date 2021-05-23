import math

def naive_bayes(vocab, training, test):
    x = len(vocab) - 1;
    mem = [];
    for i in range(x):
        mem.append([0.0,0.0,0.0,0.0])
    #mem[word][4]
    #0 = {word = F, CL = F}
    #1 = {w = F, CL = T}
    #2 = {w = T, CL = F}
    #3 = {w = T, CL = T}
    #test[statement][word]
    #test[sentence][word]
    guesses = [];
    size_test = len(test);
    size_training = len(training)
    n = 0;
    for i in range(size_training):
        if training[i][-1] == 1:
            n = n + 1;
    for i in range(size_test):
        sum_cl = math.log(n / size_training);
        sum_not_cl = math.log(1 - n/size_training);
        for j in range(x):
            #print(str(i) + " " + str(j));
            y = 0 + 2 * test[i][j];

            if mem[j][y] >= 0.0:
                numerator = 1;
                denominator = 2;
                not_numerator = 1;
                not_denominator = 2;
                for k in range(size_training):
                    if training[k][-1] == 0:
                        not_denominator = not_denominator + 1;
                        if training[k][j] == test[i][j]:
                            not_numerator = not_numerator + 1;
                    else:
                        denominator = denominator + 1;
                        if training[k][j] == test[i][j]:
                            numerator = numerator + 1;
                mem[j][y] = math.log(not_numerator/not_denominator);
                mem[j][y + 1] = math.log(numerator/denominator);

            sum_not_cl += mem[j][y];
            sum_cl += mem[j][y + 1];
        if sum_cl > sum_not_cl:
            guesses.append(1);
        else:
            guesses.append(0);
    return guesses;

def accuracy(test, guesses):
    numerator = 0;
    denominator = len(test);
    for i in range(denominator):
        if test[i][-1] == guesses[i]:
            numerator = numerator + 1;
    return numerator / denominator;
