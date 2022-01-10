# Project Muzyka
### By Robert Pace and Allen Rivas
## Overview

The general premise of this project consisted of a software application that can
recommended subgenres to an end user based on questions that they answer. They would be
prompted with five questions: “Do you like pop?”, “Do you like foreign music outside the United
States?”, “What is your favorite main genre?”, “Do you like beats or vocals?”, and “What mood
do you want to be in?”. The answers to these questions would be an input as features into a
naive Bayesian Network, which would output the most likely subgenre as the class label. The
reasoning behind outputting subgenres and not main genres of music was that the main genres
are too broad in terms of the moods that they hold. It's only when you get to the sublevel that
you can start to associate genres with certain moods that people would have.
