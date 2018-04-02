"""
-----------------------------------------------------------------------------

Rowan Computer Science Dept Spring 2018 Software Engineering Team Ostriches
Predictive Maintenance System for ASRC Federal Mission Solutions Engineering

Team Ostriches Members:
Product Owner:  Craig Wert
 Scrum Master:  John Stranahan
    Developer:  Tapan Soni
    Developer:  Michael Matthews
    Developer:  Joshua Jackson
    Developer:  Nicholas La Sala

-----------------------------------------------------------------------------

Description:



-----------------------------------------------------------------------------
"""

import random
import numpy as np

trainingData = []
trainingTags = []
validationData = []
validationTags = []

#Splits the data into 2 datasets one for training and the other for validation
#Parameters are as follows
#   - The whole entire data set
#   - The tags
#   - The percentage of rows that you want to go to the validation set
def split(whole_data_set,tags, percentage):

    index = 0

    import math

    average = 0

    x = []

    #Randomly puts 40% of the data into valdation sequencly
    while (len(validationData)) < math.floor((whole_data_set.size//30)* percentage) and (len(trainingData) < math.floor((whole_data_set.size//30)* 1-percentage)): #change .4 to whichever percentage you'd like togo to valadation set
        if(random.random()<percentage):
            validationData.append(whole_data_set[index])
            validationTags.append(tags[index])
            average += index
            x.append(index)
        else:
            trainingData.append(whole_data_set[index])
            trainingTags.append(tags[index])
        index += 1

    #This loop finishes going through the whole dataset and adding each row to training set

    if (len(validationData)) < math.floor((whole_data_set.size//30)* percentage):
        while(index < whole_data_set.size//30):
            trainingData.append(whole_data_set[index])
            trainingTags.append(tags[index])
            index += 1
    else:
        while (index < whole_data_set.size // 30):
            validationData.append(whole_data_set[index])
            validationTags.append(tags[index])
            index += 1


    # print(x[len(validationTags)-1])

    print("Validation is this percentage: ", len(validationTags)/(len(validationTags)+len(trainingTags)))


def getTrainingData():
    return trainingData

def getTrainingTags():
    return trainingTags

def getValidationData():
    return validationData

def getValidationTags():
    return validationTags
