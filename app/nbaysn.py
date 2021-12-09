# Make Predictions with Naive Bayes On The Iris Dataset
from csv import reader
from math import sqrt
from math import exp
from math import pi
import pandas as pd

def str_column_to_float(dataset,column):
    # print(dataset)

    for row in dataset:
        print(row[column])
        row[column] = float(row[column].strip())

# Convert string column to integer
def str_column_to_int(dataset, column):
    class_values = [row[column] for row in dataset]
    unique = set(class_values)
    lookup = dict()
    for i, value in enumerate(unique):
        lookup[value] = i
        print('[%s] => %d' % (value, i))
    for row in dataset:
        row[column] = lookup[row[column]]
    return lookup

# Split the dataset by class values, returns a dictionary
def separate_by_class(dataset):
    separated = dict()
    for i in range(len(dataset)):
        vector = dataset[i]
        class_value = vector[-1]
        if (class_value not in separated):
            separated[class_value] = list()
        separated[class_value].append(vector)
    return separated
 
# Calculate the mean of a list of numbers
def mean(numbers):
    return sum(numbers)/float(len(numbers))
 
# Calculate the standard deviation of a list of numbers
def stdev(numbers):
    avg = mean(numbers)
    variance = sum([(x-avg)**2 for x in numbers]) / float(len(numbers)-1)
    return sqrt(variance)
 
# Calculate the mean, stdev and count for each column in a dataset
def summarize_dataset(dataset):
    summaries = [(mean(column), stdev(column), len(column)) for column in zip(*dataset)]
    del(summaries[-1])
    return summaries
 
# Split dataset by class then calculate statistics for each row
def summarize_by_class(dataset):
    separated = separate_by_class(dataset)
    summaries = dict()
    for class_value, rows in separated.items():
        summaries[class_value] = summarize_dataset(rows)
    return summaries

def calculate_probability(x,mean,stdev):
    exponent = exp(-((x-mean)**2 / (2 * stdev**2 )))
    return (1 / (sqrt(2 * pi) * stdev)) * exponent

def calculate_class_probabilities(summaries, row):
    total_rows = sum([summaries[label][0][2] for label in summaries])
    probabilities = dict()
    for class_value, class_summaries in summaries.items():
        probabilities[class_value] = summaries[class_value][0][2]/float(total_rows)
        for i in range(len(class_summaries)):
            mean, stdev, count = class_summaries[i]
            probabilities[class_value] *= calculate_probability(row[i], mean, stdev)
    return probabilities

# Predict the class for a given row
def predict(summaries, row):
    probabilities = calculate_class_probabilities(summaries, row)
    best_label, best_prob = None, -1
    for class_value, probability in probabilities.items():
        if best_label is None or probability > best_prob:
            best_prob = probability
            best_label = class_value
    return best_label

# def main():


if __name__ == "__main__":
    # dfTwo.to_csv("test2.csv", index=False, mode=1, header=False)
    dataframe = pd.read_csv('../datasets/test4.csv')
    # print(dataset['song'])

    # Make a prediction with Naive Bayes on Iris Dataset
    dataset = list()
    itty_tracker = 0
    prior_probs = list()


    for column in range(1268):
        dataset.append([float(dataframe['q1'][column]),float(dataframe['q2'][column]),float(dataframe['q3'][column]),float(dataframe['q4'][column]),float(dataframe['q5'][column]),dataframe['subgenre'][column]])
        itty_tracker += 1
        if itty_tracker%3 == 0:
            prior_probs.append([dataframe['subgenre'][column],dataframe['prior_prob'][column]])
    # print(type(dataset[0][4]))
    # print(dataset[0])
    # for i in range(len(dataset[0])-1):
    #     str_column_to_float(dataset, i)

    # convert class column to integers
    str_column_to_int(dataset, len(dataset[0])-1)
    # fit model
    model = summarize_by_class(dataset)
    # # define a new record
    # row = [5.7,2.9,4.2,1.3]
    # # predict the label
    # label = predict(model, row)
    # print('Data=%s, Predicted: %s' % (row, label))


    # dataset = [['The Sound of Deep House','Finally','Kings Of Tomorrow','It\'s In the Lifestyle (Limited Edition)','electronic','deep house',0.010278456,2,2,1,2,5,59,0.859,0.584,-10.933,0.833],
    #             ['The Sound of Swancore','Lemonade,Dwellings,Lavender Town','rock','swancore',0.007299506999999999,2,2,3,2,5,43,0.338,0.924,-4.204,0.18],
    #             ['The Sound of Swancore','Deleto,Wolf & Bear,Deleto','rock','swancore',0.007299506999999999,2,2,3,2,5,43,0.541,0.986,-4.434,0.635],
    #             ['The Sound of Hard Bop','Alone Together - Rudy Van Gelder Remaster,Kenny Dorham,Quiet Kenny','jazz','hard bop',0.008725868000000001,2,2,4,1,5,56,0.336,0.0619,-20.494,0.197],
    #             ['The Sound of Hard Bop','Blues Inn - Remastered,Jackie McLean,Jackie\'s Bag','jazz','hard bop',0.008725868000000001,2,2,4,2,5,49,0.583,0.461,-9.58,0.516],
    #             ['The Sound of Hard Bop','True Blue,Tina Brooks,True Blue','jazz','hard bop',0.008725868000000001,2,2,4,1,5,41,0.631,0.514,-6.68,0.768]]
    
    # print(calculate_probability(1.0, 1.0, 1.0))
    # print(calculate_probability(2.0, 1.0, 1.0))
    # print(calculate_probability(0.0, 1.0, 1.0))

    # dataset = [[2.3,2,1,2,3,0],#'deep house'],
    #             [2,3,4,5,1,2,0],
    #             [1,2.2,3,2,4,0],#'swancore'],
    #             [2,1,3.4,2,5,1],#'swancore'],
    #             [2,2,4,1.5,2,1],#'hard bop'],
    #             [1,2,4,4,5.6,2],#'hard bop'],
    #             [2,2,4,1,1.1,2]]#'hard bop']]
    
    # summaries = summarize_by_class(dataset)
    # probabilities = calculate_class_probabilities(summaries, dataset[0])
    # print(probabilities)


    
    # dataset = [[3,2,3,0],#'deep house'],
    #             [2,3,2,0],#'swancore'],
    #             [4,2,5,1],#'swancore'],
    #             [5,5,2,1],#'hard bop'],
    #             [2,5.6,2],#'hard bop'],
    #             [1,4.1,2],
    #             [1,3.2,3],
    #             [5,1.1,3]]#'hard bop']]

    # dataset = [[3.393533211,2.331273381,0],
    #     [3.110073483,1.781539638,0],
    #     [1.343808831,3.368360954,0],
    #     [3.582294042,4.67917911,0],
    #     [2.280362439,2.866990263,0],
    #     [7.423436942,4.696522875,1],
    #     [5.745051997,3.533989803,1],
    #     [9.172168622,2.511101045,1],
    #     [7.792783481,3.424088941,1],
    #     [7.939820817,0.791637231,1]]

    # summary = summarize_dataset(dataset)
    # print(summary)

    # separated = separate_by_class(dataset)
    # print(separated)
    # for label in separated:
    #     print(label)
    #     for row in separated[label]:
    #         print(row)
    # summary = summarize_by_class(dataset)
    # for label in summary:
    #     print(label)
    #     for row in summary[label]:
    #         print(row)

    # print(df.head())


