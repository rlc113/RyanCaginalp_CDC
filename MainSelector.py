from Interpolation import *

def MainSelector(interpolated, targeted_true_FoM_false, target_type, target_value, FoM, restricted, Restriction):

    #Set up lengths and sizes variables for iteration
    non_interpolated_lengths = [8, 12, 16]
    non_interpolated_sizes = [1, 2, 4, 8, 16]
    
    interpolated_lengths = [8, 10, 12, 14, 16, 18, 20]
    interpolated_sizes = [1, 2, 4, 6, 8, 12, 16]
    
    
    #Final variables for selected size and length
    selected_size = 0
    selected_length = 0
    
    #Check if we have an illegal target
    if (target_type != "Energy" and target_type != "Time" and target_type != "Res"):
        print('The target variable type is invalid. Please make sure that target_type is one of "Energy", "Time", or "Res" in the input.py file')
    
    #Variable to keep track of our targeted feature for each combination
    feature_list = []
    
    #Iterate over non-interpolated lengths and sizes if we aren't doing interpolation
    if not Interpolation:
        for s in non_interpolated_sizes:
            for l in non_interpolated_lengths:
                E, T, R = Interpolation("Data.csv", s, l)
                F = 0
    
                #If we are targeting a value, then get the type we should target and get the distance from the target value
                if (targeted_true_FoM_false):
                    if (target_type == "Energy"): F = E
                    if (target_type == "Time"): F = T
                    if (target_type == "Res"): F = R
                    F = abs(F - target_value)
                
                #Otherwise get the FoM
                else: F = FoM(E, T, R)
                
                #If we don't have a restriction, just add it to the feature list
                if not restricted: feature_list.append((s, l, F))
                
                #Otherwise, we should only add it if it satisfies our restriction
                else:
                    if Restriction(E, T, R): feature_list.append((s, l, F))
    
    #Otherwise, also iterate over interpolated lengths and sizes
    if Interpolation:
        for s in interpolated_sizes:
            for l in interpolated_lengths:
                E, T, R = Interpolation("Data.csv", s, l)
                F = 0
    
                #If we are targeting a value, then get the type we should target and get the distance from the target value
                if (targeted_true_FoM_false):
                    if (target_type == "Energy"): F = E
                    if (target_type == "Time"): F = T
                    if (target_type == "Res"): F = R
                    F = abs(F - target_value)
                
                #Otherwise get the FoM
                else: F = FoM(E, T, R)
                
                #If we don't have a restriction, just add it to the feature list
                if not restricted: feature_list.append((s, l, F))
                
                #Otherwise, we should only add it if it satisfies our restriction
                else:
                    if Restriction(E, T, R): feature_list.append((s, l, F))
    
    #Now that we have our list, sort it (minimum first if we are doing targetting, maximum first for FoM)
    if targeted_true_FoM_false: sorted_feature_list = sorted(feature_list, key=lambda tup: tup[2])
    else: sorted_feature_list = sorted(feature_list, key=lambda tup: tup[2], reverse = True)
    
    #Print out the top five designs and their features, and more if the user wishes
    selected = False
    num_selections = 5
    while not selected:
        #If we are targetting, then print accordingly
        if targeted_true_FoM_false:
            print("The " + str(num_selections) + " designs closest to the target variable are shown below:")
            for i in range(num_selections):
                E, T, R = Interpolation("Data.csv", sorted_feature_list[i][0], sorted_feature_list[i][1])
                print("(" + str(i + 1) + ") Inverter Size = " + str(sorted_feature_list[i][0]) + ", Inverter Length = " + str(sorted_feature_list[i][1])
                    + ": Energy per Input Capacitance (J/F): " + str(E)
                    + ", Time per Input Capacitance (S/mF): " + str(T)
                    + ", Output Step Size (pF): " + str(R))
    
        #Otherwise, we are using FoM, and print accordingly
        else:
            print("The " + str(num_selections) + " designs with the highest FoM are shown below:")
            for i in range(num_selections):
                E, T, R = Interpolation("Data.csv", sorted_feature_list[i][0], sorted_feature_list[i][1])
                print("(" + str(i + 1) + ") Inverter Size = " + str(sorted_feature_list[i][0]) + ", Inverter Length = " + str(sorted_feature_list[i][1])
                    + ": FoM: " + str(FoM(E, T, R))
                    + ", Energy per Input Capacitance (J/F): " + str(E)
                    + ", Time per Input Capacitance (S/mF): " + str(T)
                    + ", Output Step Size (pF): " + str(R))
    
        print("Please enter a number to select a design, or a higher number to see that number of designs: ", end = "")
    
        acceptingInput = True
        while acceptingInput:
            user_input = input()
            if not user_input.isdigit():
                print("Please enter a positive whole number to select a design: ", end = "")
            elif int(user_input) > 0 and int(user_input) <= num_selections:
                acceptingInput = False
                selected = True
                selected_size = sorted_feature_list[int(user_input) - 1][0]
                selected_length = sorted_feature_list[int(user_input) - 1][1]
                print("Design " + user_input + " Selected.")
            elif int(user_input) <= len(sorted_feature_list):
                acceptingInput = False
                num_selections = int(user_input)
            else:
                acceptingInput = False
                print("Warning: The number of selections requested was more than the total number of designs supported. We will display all designs instead.")
                num_selections = len(sorted_feature_list)
    
    return selected_size, selected_length
