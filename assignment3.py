import input_output
import naive_bayes

def main():
    c = False
    training_path = "data/trainingSet.txt"
    test_path = "data/testSet.txt"
    a = 0
    while not c:
        print("Assignment 3: Sentiment Analysis menu!")
        print("1) Use training set as the test data.")
        print("2) Use test set as the test data.")
        i = input("Enter your choice here: ")
        try:
            a = int(i)
            if a != 1 && a != 2:
                a = 7 / 0
            c = True
        except:
            print("please enter a valid integer!")

    test_path = training_path;
    vocab, training, test = input_output.preprocessing(training_path, test_path);
    guesses = naive_bayes.naive_bayes(vocab, training, test);
    input_output.print_guesses(vocab, test, guesses);
    accuracy = naive_bayes.accuracy(test, guesses) * 100;
    print("We had an accuracy of " + accuracy + " percent.");

if __name__ == "__main__":
    main()
