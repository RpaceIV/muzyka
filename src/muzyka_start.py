import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.naive_bayes import GaussianNB
import seaborn as sns; sns.set(color_codes=True)
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
from ordered_set import OrderedSet
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

def str_column_to_int(dataset, column):
    class_values = [row[column] for row in dataset]
    # print(set(class_values))
    unique = OrderedSet(class_values)
    # print(unique)
    lookup = dict()
    for i, value in enumerate(unique):
        lookup[value] = i
        print('[%s] => %d' % (value, i))
    for row in dataset:
        row[column] = lookup[row[column]]
    # print(lookup)
    # return lookup
    return unique


if __name__ == "__main__":

    # iris = load_iris()

    # print(len(iris.data)) #feature data list
    # print(len(iris.feature_names)) #feature names list
    # print(len(iris.target)) #class lables list

    # dfTwo.to_csv("test2.csv", index=False, mode=1, header=False)
    dataframe = pd.read_csv('datasets/csv_data/song_dataset.csv')
    # print(dataset['song'])

    # Make a prediction with Naive Bayes on Iris Dataset
    dataset = list()
    itty_tracker = 0
    class_lables = list()
    prior_probs = list()
    parent_genres = list()

    for column in range(1268):
        dataset.append([float(dataframe['q1'][column]),float(dataframe['q2'][column]),float(dataframe['q3'][column]),float(dataframe['q4'][column]),float(dataframe['q5'][column]),dataframe['subgenre'][column]])
        parent_genres.append(dataframe['genre'][column])
        # itty_tracker += 1
        # if itty_tracker%3 == 0:
        #     prior_probs.append([dataframe['subgenre'][column],dataframe['prior_prob'][column]])

    parent_genres = OrderedSet(parent_genres)

    # convert class column to integers
    unique = str_column_to_int(dataset, len(dataset[0])-1)
    
    for i in range(len(dataset)):
        # print(i[5])
        class_lables.append(dataset[i][5])
        dataset[i].pop(5)
        # print(dataset[i])

    # print(dataset)
    # print(class_lables)
    clf = GaussianNB()
    
    # print(dataset)
    clf.fit(dataset,class_lables)

    questions = [
    "Do you like pop?\na) yes \tb)no \n :",
    "Do you like foreign music outside of the United States?\na) yes \tb)no \n :",
    "What is your favorite main genre?\na) Electronic \tb) Rap \n \nc) Rock \td) Jazz \n\ne) Classical \n :",
    "Do you like beats or vocals?\na) beats \tb) vocals \n :",
    "What mood do you want to be in?\na) Happy \tb) Sad \n c) Angry \td) Hyped \n e) Relaxed \td) Sensual \n :"]

    answers = []
    response = ''

    for question in questions:
        response = input(question)
        # answers.append(input(question))
        while True:
            if response.upper() == 'A':
                answers.append(1.0)
                break
            elif response.upper() == 'B':
                answers.append(2.0)
                break
            elif response.upper() == 'C':
                answers.append(3.0)
                break
            elif response.upper() == 'D':
                answers.append(4.0)
                break
            elif response.upper() == 'E':
                answers.append(5.0)
                break
            elif response.upper() == 'F':
                answers.append(6.0)
                break
            else:
                print("Invalid response try again")

    print(answers)

    # print(clf.predict_proba([[1.0,2.0,1.0,2.0,1.0]]))
    # print(clf.predict([[1.0,2.0,1.0,2.0,4.0]]))

    # plt.scatter(dataset[:, 0], dataset[:, 1], c=class_lables, s=10, cmap='RdBu');

    # print(clf.predict([answers[0],answers[1],answers[2],answers[3],answers[4]]))

    predicted_song = clf.predict([answers])

    prediction_distrabution = clf.predict_proba([answers])
    print(predicted_song)

    # print(prior_probs)
    print(prediction_distrabution)

    unique = list(unique)
    prediction_distrabution = tuple(prediction_distrabution[0])
    print(type(unique))
    print(type(prediction_distrabution))
    

    y_pos = np.arange(len(unique))
    # Create bars
    plt.bar(y_pos, prediction_distrabution)

    # Create names on the x-axis
    plt.xticks(y_pos, unique)
    
    fig = plt.gcf()
    fig.set_size_inches(18.5, 10.5)
    # Show graphic
    plt.show()




    # for genre in parent_genres:

    # print(prior_probs[bruh][0])
    

    # gnb = GaussianNB()

    # gnb.fit(df,iris.target)
