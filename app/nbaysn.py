# Make Predictions with Naive Bayes On The Iris Dataset
from csv import reader
from math import sqrt
from math import exp
from math import pi
import pandas as pd

def separate_by_class(dataset):
    separated = dict()
    for i in range(len(dataset)):
        vector = dataset[i]
        class_value = vector[-12]
        if(class_value not in separated):
            separated[class_value] = list()
        separated[class_value].append(vector)
    return separated

# def mean(numbers):
#     return sum(numbers)/float(len(numbers))

# def stdev(numbers):


# def main():


if __name__ == "__main__":
    # dfTwo.to_csv("test2.csv", index=False, mode='a', header=False)
    # dataset = pd.read_csv('../datasets/test.csv')
    # print(dataset['song'])
    dataset = [['The Sound of Deep House','Finally','Kings Of Tomorrow','It\'s In the Lifestyle (Limited Edition)','electronic','deep house',0.010278456,'b','b','a','b','z',59,0.859,0.584,-10.933,0.833],
                ['The Sound of Swancore','Lemonade,Dwellings,Lavender Town','rock','swancore',0.007299506999999999,'b','b','c','b','z',43,0.338,0.924,-4.204,0.18],
                ['The Sound of Swancore','Deleto,Wolf & Bear,Deleto','rock','swancore',0.007299506999999999,'b','b','c','b','z',43,0.541,0.986,-4.434,0.635],
                ['The Sound of Hard Bop','Alone Together - Rudy Van Gelder Remaster,Kenny Dorham,Quiet Kenny','jazz','hard bop',0.008725868000000001,'b','b','d','a','z',56,0.336,0.0619,-20.494,0.197],
                ['The Sound of Hard Bop','Blues Inn - Remastered,Jackie McLean,Jackie\'s Bag','jazz','hard bop',0.008725868000000001,'b','b','d','b','z',49,0.583,0.461,-9.58,0.516],
                ['The Sound of Hard Bop','True Blue,Tina Brooks,True Blue','jazz','hard bop',0.008725868000000001,'b','b','d','a','z',41,0.631,0.514,-6.68,0.768]]

    separated = separate_by_class(dataset)
    # print(separated)
    for label in separated:
        print(label)
        for row in separated[label]:
            print(row)
    # print(df.head())


