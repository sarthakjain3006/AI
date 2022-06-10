import numpy as np
data= np.loadtxt('D:\AI\PROJ 2\CS205_CalibrationData__1.txt')
def backwardsearch(data):
    current_set_of_features =[]
    for i in range(p,1,-1):
        current_set_of_features=p
    print (current_set_of_features)
    # best_so_far_accuracy= 0
    # for i in range(p):
    #     print("on the {0} th level of the search".format(i))
    #     feature_to_delete_at_this_level = []
    #     for k in range(1,p):
    #         if k not in current_set_of_features:
    #             # print("considering adding the {0} th feature".format(k))
    #             accuracy =leave_one_out_cross_validation (data,current_set_of_features,k)
    #             print(accuracy)
    #         if accuracy>best_so_far_accuracy:
    #             best_so_far_accuracy=accuracy
    #             feature_to_add_at_this_level=k 
    #     if feature_to_add_at_this_level !=[]:       
    #         current_set_of_features.append(feature_to_add_at_this_level)
    #     # print('on level {0} i added feature {1}, tocurrent set'.format(i,feature_to_add_at_this_level))
    #     print(' {0}'.format(current_set_of_features))
