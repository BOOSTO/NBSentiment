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
            if a != 1 and a != 2:
                a = 7 / 0
            c = True
        except:
            print("please enter a valid integer!")
    if(a == 1):
        test_path = training_path
    vocab, training, test = input_output.preprocess(training_path, test_path)
    guesses = naive_bayes.naive_bayes(vocab, training, test)
    accuracy = naive_bayes.accuracy(test, guesses) * 100.0
    input_output.write_results(training_path, test_path, accuracy)
    print("Classification complete. printed results to results.txt")

if __name__ == "__main__":
    main()
