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

def strColumnToInt(song_dataset, column):
    class_values = [row[column] for row in song_dataset]
    unique = OrderedSet(class_values)
    lookup = dict()
    for i, value in enumerate(unique):
        lookup[value] = i
        print('[%s] => %d' % (value, i))
    for row in song_dataset:
        row[column] = lookup[row[column]]
    # return lookup
    return unique

def answerQuestions(questions,answers):
    for question in questions:
        while True:
            response = input(question)
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
                print("Invalid response try again \n")
    return answers

if __name__ == "__main__":
    songDF = pd.read_csv('datasets/csv_data/song_data.csv')
    song_dataset = list()
    class_lables = list()
    
    questions = [
    "Do you like pop?\na) yes \tb)no \n :",
    "Do you like foreign music outside of the United States?\na) yes \tb)no \n :",
    "What is your favorite main genre?\na) Electronic \tb) Rap \n \nc) Rock \td) Jazz \n\ne) Classical \n :",
    "Do you like beats or vocals?\na) beats \tb) vocals \n :",
    "What mood do you want to be in?\na) Happy \tb) Sad \n c) Angry \td) Hyped \n e) Relaxed \td) Sensual \n :"]

    answers = []
    response = ''

    for column in range(songDF.shape[0]): #shape[0] returns the size of rows in the sheet
        song_dataset.append([float(songDF['q1'][column]),
                            float(songDF['q2'][column]),
                            float(songDF['q3'][column]),
                            float(songDF['q4'][column]),
                            float(songDF['q5'][column]),
                            songDF['subgenre'][column]])

    # convert class labels to integers
    unique = strColumnToInt(song_dataset, len(song_dataset[0])-1)
    
    #Seperate the class label from the
    for i in range(len(song_dataset)):
        class_lables.append(song_dataset[i][5])
        song_dataset[i].pop(5)

    # print(class_lables)
    # print(song_dataset)

    clf = GaussianNB()
    clf.fit(song_dataset,class_lables)
    
    answers = answerQuestions(questions,answers)

    predicted_song = clf.predict([answers])
    prediction_distrabution = clf.predict_proba([answers])
    print(predicted_song)
    print(prediction_distrabution)

    #Generate the bar graph of subgenre predictions
    y_pos = np.arange(len(list(unique)))
    plt.bar(y_pos, tuple(prediction_distrabution[0]))
    plt.xticks(y_pos, list(unique))
    fig = plt.gcf()
    fig.set_size_inches(18.5, 10.5)
    plt.show()
