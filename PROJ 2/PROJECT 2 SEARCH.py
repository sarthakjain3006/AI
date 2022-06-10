
from cmath import inf
import random
import pandas as pd
import numpy as np
import math
from math import sqrt
from math import pow
data= np.loadtxt('D:\AI\PROJ 2\CS205_SP_2022_Largetestdata__67.txt')

def leave_one_out_cross_validation(data,current_set_of_features,feature_to_add):
    # print("start cross validation")
    consolidated_list_of_features=[]
    consolidated_list_of_features.append(0)
    for i in current_set_of_features:
        consolidated_list_of_features.append(i)
    consolidated_list_of_features.append(feature_to_add)
    selected_features_data=data[:,consolidated_list_of_features]
    # print ("features are - {0}".format(consolidated_list_of_features))
    number_correctly_classified=0
    for i in range(len(selected_features_data)):
        object_to_classify=selected_features_data[i,1:]
        # print(object_to_classify)
        label_object_to_classify=selected_features_data[i,0]
        nearest_neighbor_distance=inf
        nearest_neighbor_location=inf
        for k in range(len(selected_features_data)):
            if k!= i:
                distance= math.dist(object_to_classify,selected_features_data[k,1:])
                if distance<nearest_neighbor_distance:
                    nearest_neighbor_distance=distance
                    nearest_neighbor_location=k
                    nearest_neighbor_label=data[nearest_neighbor_location,0]
        
        # print('object {0} is class {1}'.format(i,label_object_to_classify))     
        # print('its nearest neighbour is {0} which is in class {1}'.format(nearest_neighbor_location,nearest_neighbor_label))
        if label_object_to_classify==nearest_neighbor_label:
            number_correctly_classified+=1
            # print("number of features classified:{0}".format(number_correctly_classified))
    accuracy= number_correctly_classified/(len(data))
    return accuracy
    
# def isempty(x,y):
#     if y not in x:
#         return True 
def feature_search_demo_forwards(data):

    current_set_of_features=[]
    p=len(data[1])
    print(p)
    best_so_far_accuracy= 0
    for i in range(p):
        print("on the {0} th level of the search".format(i))
        feature_to_add_at_this_level = []
        for k in range(1,p):
            if k not in current_set_of_features:
                # print("considering adding the {0} th feature".format(k))
                accuracy =leave_one_out_cross_validation (data,current_set_of_features,k)
                print(accuracy)
            if accuracy>best_so_far_accuracy:
                best_so_far_accuracy=accuracy
                feature_to_add_at_this_level=k 
        if feature_to_add_at_this_level !=[]:       
            current_set_of_features.append(feature_to_add_at_this_level)
        # print('on level {0} i added feature {1}, tocurrent set'.format(i,feature_to_add_at_this_level))
        print(' {0}'.format(current_set_of_features))
        #return(accuracy,current_set_of_features)

feature_search_demo_forwards(data)