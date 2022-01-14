import numpy as np
import pandas as pd
from sklearn.naive_bayes import GaussianNB
import matplotlib.pyplot as plt
from ordered_set import OrderedSet


def strColumnToInt(class_lables):
    unique_subgenres = OrderedSet(class_lables)
    lookup = dict()
    for i, value in enumerate(unique_subgenres):
        lookup[value] = i
        print('[%s] => %d' % (value, i))
    for i in range(len(class_lables)):
        class_lables[i] = lookup[class_lables[i]]
    return unique_subgenres


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
    song_features = list()
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
        song_features.append([float(songDF['q1'][column]),
                            float(songDF['q2'][column]),
                            float(songDF['q3'][column]),
                            float(songDF['q4'][column]),
                            float(songDF['q5'][column])])

        class_lables.append(songDF['subgenre'][column])
    
    unique_subgenres = strColumnToInt(class_lables)
    
    gaussNetwork = GaussianNB()
    gaussNetwork.fit(song_features,class_lables)
    
    answers = answerQuestions(questions,answers)

    predicted_song = gaussNetwork.predict([answers])
    prediction_distrabution = gaussNetwork.predict_proba([answers])
    print(predicted_song)
    print(prediction_distrabution)

    #Generate the bar graph of subgenre predictions
    y_pos = np.arange(len(list(unique_subgenres)))
    plt.bar(y_pos, tuple(prediction_distrabution[0]))
    plt.xticks(y_pos, list(unique_subgenres))
    fig = plt.gcf()
    fig.set_size_inches(18.5, 10.5)
    plt.show()
