import sys

import numpy as np
import pandas as pd
from sklearn.naive_bayes import GaussianNB
import matplotlib.pyplot as plt
from ordered_set import OrderedSet

#Fancy Output Libaries
from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint 
from pyfiglet import figlet_format


def strColumnToInt(class_lables):
    unique_subgenres = OrderedSet(class_lables)
    lookup = dict()
    for i, value in enumerate(unique_subgenres):
        lookup[value] = i
        if(i%3 == 0):
            print('[%s] => %d' % (value, i), end= '\t')
        elif(i%2 == 0):
            print('[%s] => %d' % (value, i), end= '\t')
        else:
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
    print("=================================================================================")
    cprint(figlet_format('muzyka', font='isometric1', width = 100 ),
       'white', attrs=['bold'])
    print("=================================================================================")

    songDF = pd.read_csv('datasets/csv_data/song_data.csv')
    song_features = list()
    class_lables = list()
    
    questions = [
    "\n\nDo you like pop?\na) yes \tb)no \n :",
    "\nDo you like foreign music outside of the United States?\na) yes \tb)no \n :",
    "\nWhat is your favorite main genre?\na) Electronic \tb) Rap \nc) Rock \td) Jazz \ne) Classical \n :",
    "\nDo you like beats or vocals?\na) beats \tb) vocals \n :",
    "\nWhat mood do you want to be in?\na) Happy \tb) Sad \n c) Angry \td) Hyped \n e) Relaxed \td) Sensual \n :"]

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
    
    print('\n ----------------------------')
    print('| Your Subgenre is: ',unique_subgenres[int(predicted_song)],'! |')
    print(' ----------------------------\n\n')

    print('Subgenre Distrabution: \n',prediction_distrabution)

    #Generate the bar graph of subgenre predictions
    y_pos = np.arange(len(list(unique_subgenres)))
    plt.bar(y_pos, tuple(prediction_distrabution[0]))
    plt.xticks(y_pos, list(unique_subgenres))
    fig = plt.gcf()
    fig.set_size_inches(18.5, 10.5)
    plt.show()
