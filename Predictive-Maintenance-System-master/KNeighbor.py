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

# Knearest neighbor is taken extremely long now that our datasize has double see if this can be improved
import pickle
from sklearn.neighbors import KNeighborsClassifier

def classify(neighbor,trainingData,trainingTags,validationData,validationTags, predict):
    print("Kneighbor:")
    # classy = KNeighborsClassifier(n_neighbors=neighbor);
    # classy = classy.fit(trainingData, trainingTags) #change name of classy
    #output = open("classy.pkl", 'wb') #open output file
    #pickle.dump(classy, output) #pickle classifier
    pkl_file = open('classy.pkl', 'rb') #open input file

    classy = pickle.load(pkl_file) #unpickle pickled file
    print(classy.score(validationData,validationTags)) #how successful the test was

    #output.close() #close output file
    pkl_file.close() #close input file

    return classy.predict(predict)