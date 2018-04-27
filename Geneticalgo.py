#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 21:45:01 2018

@author: tauro
"""

from tpot import TPOTClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

#load the data
telescope = pd.read_csv("MAGIC Gamma Telescope Data.csv")

#shuffle the data
telescope_shuffle = telescope.iloc[np.random.permutation(len(telescope))]

#reset indices
tele = telescope_shuffle.reset_index(drop=True)

#Encode classes as 0 and 1
tele['Class'] = tele['Class'].map({'g': 1, 'h': 0})
tele_class = tele['Class'].values

#Data split

training_indices, validation_indices = training_indices, testing_indices = train_test_split(
tele,train_size = 0.75, test_size = 0.25, stratify=tele_class)

tpot_classifier = TPOTClassifier(generations=100, population_size = 100, verbosity=2)

tpot_classifier.fit(tele.drop('Class', axis=1).loc[training_indices,:].values,
                    tele.loc[training_indices, 'Class'].values)
                    
tpot_classifier.score(tele.drop('Class', axis=1).loc[validation_indices,:].values,
                     tele.loc[validation_indices, 'Class'].values)

tpot_classifier.export('pipeline.py')

