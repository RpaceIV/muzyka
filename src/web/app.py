from ordered_set import OrderedSet
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from flask import Flask, request, render_template
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.naive_bayes import GaussianNB
import seaborn as sns
sns.set(color_codes=True)

app = Flask(__name__, template_folder='templates')


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
    return lookup


@app.route('/')
def index():
    html = render_template('index.html')
    return html
    # return "Hello World"


@app.route('/', methods=['POST'])
def my_form_post():

    dataframe = pd.read_csv('datasets/csv_data/song_dataset.csv')
    # print(dataset['song'])

    # Make a prediction with Naive Bayes on Iris Dataset
    dataset = list()
    itty_tracker = 0
    class_lables = list()
    prior_probs = list()
    parent_genres = list()

    for column in range(1268):
        dataset.append([float(dataframe['q1'][column]), float(dataframe['q2'][column]), float(dataframe['q3'][column]), float(
            dataframe['q4'][column]), float(dataframe['q5'][column]), dataframe['subgenre'][column]])
        parent_genres.append(dataframe['genre'][column])
        # itty_tracker += 1
        # if itty_tracker%3 == 0:
        #     prior_probs.append([dataframe['subgenre'][column],dataframe['prior_prob'][column]])

    parent_genres = OrderedSet(parent_genres)

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

    # print(dataset)
    clf.fit(dataset, class_lables)

    qOne = request.form['q1']
    qTwo = request.form['q2']
    qThree = request.form['q3']
    qFour = request.form['q4']
    qFive = request.form['q5']
    qs = [qOne, qTwo, qThree, qFour, qFive]

    answers = []
    # response = ''

    for question in qs:
        # response = input(question)
        # answers.append(input(question))
        while True:
            if question.upper() == 'A':
                answers.append(1.0)
                break
            elif question.upper() == 'B':
                answers.append(2.0)
                break
            elif question.upper() == 'C':
                answers.append(3.0)
                break
            elif question.upper() == 'D':
                answers.append(4.0)
                break
            elif question.upper() == 'E':
                answers.append(5.0)
                break
            elif question.upper() == 'F':
                answers.append(6.0)
                break
            else:
                print("Invalid response try again")

    # muzykastart.response = qs

    # muzykastart.response = [qOne, qTwo, qThree, qFour, qFive]
    # subgenre = muzykastart.predicted_song

    # subgenre = df['subgenre']
    # html = render_template(
    #     'subgenre.html', qOne=df['q1'], qTwo=df['q2'], qThree=df['q3'], qFour=df['q4'], qFive=df['q5'], subgenre=subgenre)
    predicted_song = clf.predict([answers])
    prediction_distrabution = clf.predict_proba([answers])

    subgenre_names = pd.read_csv(
        'datasets/csv_data/curated_subgenres_data.csv')
    # subgenre_name.index.values[int(predicted_song)+2]
    # print(subgenre_names.iloc[int(predicted_song)]['Name'])
    subgenre_nm = subgenre_names.iloc[int(predicted_song)]['Name']
    # subgenre_names.iloc[int(predicted_song)]['Name']

    print(predicted_song)
    # print(prediction_distrabution)

    # html = render_template(
    #     'subgenre.html', subgenre=subgenre_nm, ps=predicted_song, pd=prediction_distrabution)
    html = render_template(
        'subgenre.html', subgenre=subgenre_nm)
    return html


if __name__ == "__main__":
    app.run(debug=True)
