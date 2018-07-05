########################### Imorting Liabraries ###############################
from sklearn.neural_network import MLPClassifier
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import metrics
import numpy as np
import pandas as pd

def BIMLP(noOfNeuronstr):
    ############################# Data Analysis ###################################
    data = pd.read_csv('train800.csv')
    #data = pd.read_csv('train11.csv')
    data=data.drop(['Unnamed: 0'],1)
    print(data.shape)
    ##################################
    testdata = pd.read_csv('test1gui.csv')
    #testdata = pd.read_csv('train11.csv')
    testdata=testdata.drop(['Unnamed: 0'],1)
    #testdata=testdata[7:8] #7no row select kore
    #testy=[1]
    ##################################
    label = pd.read_csv('label800.csv')
    y = label['target']
    y = list(y)
    #y=[1,2,3,4,5,6,7,8,9,10,11]
    ##########
    
    #X_train, X_test, y_train, y_test = train_test_split(data, y, test_size=0.21, random_state=33)
    
    X_train = data
    y_train = y
    print (X_train.shape)
    X_test = testdata
    #y_test = [0]
    print (X_test.shape)
    #####################Preperaing Data For Training And Testing##################
    
    scaler = StandardScaler().fit(X_train)
    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)
    
    
    #print("Actual:")
    #print(y_test)
    
    ###############################################################################
    noOfNeuron = noOfNeuronstr.split(',')
    
    #print("Print Neuron Str1 and str1 : "+noOfNeuron[0]+" "+noOfNeuron[1]+" ",len(noOfNeuron))
    
    if len(noOfNeuron)==1:
        print("one hidden layer")
        h1 = int(noOfNeuron[0])
        clf = MLPClassifier(solver='adam',hidden_layer_sizes=(h1),alpha=1e-04)
        clf.fit(X_train, y_train)
        
        y_train_predMLP=clf.predict(X_train)
        y_predMLP = clf.predict(X_test)
        print("Predicted:")
        print(y_predMLP)
        
        return y_predMLP
        
    elif len(noOfNeuron)==2:
        print("two hidden layer")
        h1 = int(noOfNeuron[0])
        h2 = int(noOfNeuron[1])
        clf = MLPClassifier(solver='adam',hidden_layer_sizes=(h1,h2),alpha=1e-04)
        clf.fit(X_train, y_train)
        
        y_train_predMLP=clf.predict(X_train)
        y_predMLP = clf.predict(X_test)
        
        ##############
        
        #y_train_predMLP=clf.predict(X_train)

        #print("Asif Train Actual : ",y_train)
        #print("Asif Train Accuracy : ",y_train_predMLP)
        
        ##############
        
        
        print("Predicted:")
        print(y_predMLP)
        
        return y_predMLP
    else:
        y_predMLP=[[-1]]
        return y_predMLP
    ######################### Multi-layer Perceptron ##############################
    '''
    clf = MLPClassifier(solver='adam',hidden_layer_sizes=(250),alpha=1e-04)
    clf.fit(X_train, y_train)
    
    y_train_predMLP=clf.predict(X_train)
    y_predMLP = clf.predict(X_test)
    print("Predicted:")
    print(y_predMLP)
    '''
    acc_MLP=metrics.accuracy_score(y_predMLP, y_test)
    acc_MLP_train=metrics.accuracy_score(y_train, y_train_predMLP)
    
    print("Training Acccuracy : ",acc_MLP_train)
    print("Testing Acccuracy : ",acc_MLP)
    '''
    return y_predMLP
    '''
    '''
    ######################### Multi-layer Perceptron ##############################
    clf = MLPClassifier(solver='adam',hidden_layer_sizes=(250,120),alpha=1e-04)
    clf.fit(X_train, y_train)
    
    y_train_predMLP=clf.predict(X_train)
    y_predMLP = clf.predict(X_test)
    print("Predicted:")
    print(y_predMLP)
    acc_MLP=metrics.accuracy_score(y_predMLP, y_test)
    acc_MLP_train=metrics.accuracy_score(y_train, y_train_predMLP)
    
    print("Training Acccuracy : ",acc_MLP_train)
    print("Testing Acccuracy : ",acc_MLP)
    '''
    
