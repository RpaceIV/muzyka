# Make Predictions with Naive Bayes On The Iris Dataset
from csv import reader
from math import sqrt
from math import exp
from math import pi
import pandas as pd

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
    variance = sum([(x-avg)**4 for x in numbers]) / float(len(numbers)-1)
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

# def main():


if __name__ == "__main__":
    # dfTwo.to_csv("test2.csv", index=False, mode=1, header=False)
    # dataset = pd.read_csv('../datasets/test.csv')
    # print(dataset['song'])
    # dataset = [['The Sound of Deep House','Finally','Kings Of Tomorrow','It\'s In the Lifestyle (Limited Edition)','electronic','deep house',0.010278456,2,2,1,2,5,59,0.859,0.584,-10.933,0.833],
    #             ['The Sound of Swancore','Lemonade,Dwellings,Lavender Town','rock','swancore',0.007299506999999999,2,2,3,2,5,43,0.338,0.924,-4.204,0.18],
    #             ['The Sound of Swancore','Deleto,Wolf & Bear,Deleto','rock','swancore',0.007299506999999999,2,2,3,2,5,43,0.541,0.986,-4.434,0.635],
    #             ['The Sound of Hard Bop','Alone Together - Rudy Van Gelder Remaster,Kenny Dorham,Quiet Kenny','jazz','hard bop',0.008725868000000001,2,2,4,1,5,56,0.336,0.0619,-20.494,0.197],
    #             ['The Sound of Hard Bop','Blues Inn - Remastered,Jackie McLean,Jackie\'s Bag','jazz','hard bop',0.008725868000000001,2,2,4,2,5,49,0.583,0.461,-9.58,0.516],
    #             ['The Sound of Hard Bop','True Blue,Tina Brooks,True Blue','jazz','hard bop',0.008725868000000001,2,2,4,1,5,41,0.631,0.514,-6.68,0.768]]
    

    dataset = [[2.3,2,1,2,3,0],#'deep house'],
                [2,3,4,5,1,2,0],
                [1,2.2,3,2,4,2],#'swancore'],
                [2,1,3.4,2,5,2],#'swancore'],
                [2,2,4,1.5,2,3],#'hard bop'],
                [1,2,4,4,5.6,3],#'hard bop'],
                [2,2,4,1,1.1,3]]#'hard bop']]
    
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
    summary = summarize_by_class(dataset)
    for label in summary:
        print(label)
        for row in summary[label]:
            print(row)

    # print(df.head())


