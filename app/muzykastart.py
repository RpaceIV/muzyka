import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.naive_bayes import GaussianNB
import seaborn as sns; sns.set(color_codes=True)
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
# %matplotlib inline

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


if __name__ == "__main__":

    # iris = load_iris()

    # print(len(iris.data)) #feature data list
    # print(len(iris.feature_names)) #feature names list
    # print(len(iris.target)) #class lables list

    # dfTwo.to_csv("test2.csv", index=False, mode=1, header=False)
    dataframe = pd.read_csv('../datasets/test4.csv')
    # print(dataset['song'])

    # Make a prediction with Naive Bayes on Iris Dataset
    dataset = list()
    itty_tracker = 0
    class_lables = list()
    prior_probs = list()


    for column in range(1268):
        dataset.append([float(dataframe['q1'][column]),float(dataframe['q2'][column]),float(dataframe['q3'][column]),float(dataframe['q4'][column]),float(dataframe['q5'][column]),dataframe['subgenre'][column]])
        itty_tracker += 1
        if itty_tracker%3 == 0:
            prior_probs.append([dataframe['subgenre'][column],dataframe['prior_prob'][column]])


    # convert class column to integers
    str_column_to_int(dataset, len(dataset[0])-1)
    
    for i in range(len(dataset)):
        # print(i[5])
        class_lables.append(dataset[i][5])
        dataset[i].pop(5)
        # print(dataset[i])

    # print(dataset)
    # print(class_lables)
    clf = GaussianNB()

    clf.fit(dataset,class_lables)

    print(clf.predict([[1.0,2.0,2.0,2.0,4.0]]))

    # gnb = GaussianNB()

    # gnb.fit(df,iris.target)