import csv
import numpy as np
import math

#This function tells us which input capacitances to use and how long we expect the measurement time to take
def SimInterpolation(filename, size, length):
    #First check the inputs - If it isn't possible, return -1
    if size not in [1, 2, 4, 6, 8, 12, 16]: return -1
    if length % 2 != 0 or length < 8 or length > 20: return -1

    T_dict = {}
    with open(filename, mode ='r') as file:
        csvFile = csv.reader(file)
        for i,lines in enumerate(csvFile):
            if i != 0:
                if lines[0] not in T_dict.keys(): T_dict[lines[0]] = {}
                if lines[1] not in T_dict[lines[0]].keys(): T_dict[lines[0]][lines[1]] = []
                T_dict[lines[0]][lines[1]].append((float(lines[2]), float(lines[3])))

    #These vectors contain the sizes and lengths that we simulated
    Valid_Sizes = [1, 2, 4, 8, 16]    
    Valid_Lengths = [8, 12, 16]

    #First case - The size and length were already simulated - we can just return the times and capacitances
    if size in Valid_Sizes and length in Valid_Lengths:
        cap1 = T_dict[str(size)][str(length)][0][0]
        time1 = T_dict[str(size)][str(length)][0][1]
        cap2 = T_dict[str(size)][str(length)][1][0]
        time2 = T_dict[str(size)][str(length)][1][1]

        return cap1, time1, cap2, time2 

    #Second case - We have a valid size but not a valid length.
    if size in Valid_Sizes and length not in Valid_Lengths:
        #First, we want to find the two values closest to the given length such that we can "interpolate" from those values linearly
        dist = np.array(Valid_Lengths) - length
        closest_length_index = np.argmin(abs(dist))

        dist_without_closest = np.delete(dist, closest_length_index)
        second_closest_dist = dist_without_closest[np.argmin(abs(dist_without_closest))]
        second_closest_length_index = np.where(dist == second_closest_dist)[0][0]

        closest_length = Valid_Lengths[closest_length_index]
        second_closest_length = Valid_Lengths[second_closest_length_index]

        #Get the values for cap and time
        closest_cap1, closest_time1, closest_cap2, closest_time2 = SimInterpolation("Time_Data.csv", size, closest_length)
        second_closest_cap1, second_closest_time1, second_closest_cap2, second_closest_time2 = SimInterpolation("Time_Data.csv", size, second_closest_length)

        #Get the slope between these
        cap1_slope = (closest_cap1 - second_closest_cap1)/(closest_length - second_closest_length)
        time1_slope = (closest_time1 - second_closest_time1)/(closest_length - second_closest_length)
        cap2_slope = (closest_cap2 - second_closest_cap2)/(closest_length - second_closest_length)
        time2_slope = (closest_time2 - second_closest_time2)/(closest_length - second_closest_length)

        #Calculate the interpolated values
        cap1_interpolated = second_closest_cap1 + cap1_slope * (length - second_closest_length)
        time1_interpolated = second_closest_time1 + time1_slope * (length - second_closest_length)
        cap2_interpolated = second_closest_cap2 + cap2_slope * (length - second_closest_length)
        time2_interpolated = second_closest_time2 + time2_slope * (length - second_closest_length)

        #Return the interpolated values
        return cap1_interpolated, time1_interpolated, cap2_interpolated, time2_interpolated

    #Third case - We have a valid length but not a valid size.
    if size not in Valid_Sizes and length in Valid_Lengths:
        #First, we want to find the two values closest to the given size such that we can "interpolate" from those values linearly
        dist = np.array(Valid_Sizes) - size
        closest_size_index = np.argmin(abs(dist))

        dist_without_closest = np.delete(dist, closest_size_index)
        second_closest_dist = dist_without_closest[np.argmin(abs(dist_without_closest))]
        second_closest_size_index = np.where(dist == second_closest_dist)[0][0]

        closest_size = Valid_Sizes[closest_size_index]
        second_closest_size = Valid_Sizes[second_closest_size_index]

        #Get the values for cap and time
        closest_cap1, closest_time1, closest_cap2, closest_time2 = SimInterpolation("Time_Data.csv", closest_size, length)
        second_closest_cap1, second_closest_time1, second_closest_cap2, second_closest_time2 = SimInterpolation("Time_Data.csv", second_closest_size, length)

        #Get the slope between these
        cap1_slope = (closest_cap1 - second_closest_cap1)/(closest_size - second_closest_size)
        time1_slope = (closest_time1 - second_closest_time1)/(closest_size - second_closest_size)
        cap2_slope = (closest_cap2 - second_closest_cap2)/(closest_size - second_closest_size)
        time2_slope = (closest_time2 - second_closest_time2)/(closest_size - second_closest_size)

        #Calculate the interpolated values
        cap1_interpolated = second_closest_cap1 + cap1_slope * (size - second_closest_size)
        time1_interpolated = second_closest_time1 + time1_slope * (size - second_closest_size)
        cap2_interpolated = second_closest_cap2 + cap2_slope * (size - second_closest_size)
        time2_interpolated = second_closest_time2 + time2_slope * (size - second_closest_size)

        #Return the interpolated values
        return cap1_interpolated, time1_interpolated, cap2_interpolated, time2_interpolated


    #Fourth case - We have neither a valid length nor a valid size.
    if size not in Valid_Sizes and length not in Valid_Lengths:
        #First, we want to find the two values closest to the given size such that we can "interpolate" from those values linearly
        dist = np.array(Valid_Sizes) - size
        closest_size_index = np.argmin(abs(dist))

        dist_without_closest = np.delete(dist, closest_size_index)
        second_closest_dist = dist_without_closest[np.argmin(abs(dist_without_closest))]
        second_closest_size_index = np.where(dist == second_closest_dist)[0][0]

        closest_size = Valid_Sizes[closest_size_index]
        second_closest_size = Valid_Sizes[second_closest_size_index]

        #Get the values for cap and time
        closest_cap1, closest_time1, closest_cap2, closest_time2 = SimInterpolation("Time_Data.csv", closest_size, length)
        second_closest_cap1, second_closest_time1, second_closest_cap2, second_closest_time2 = SimInterpolation("Time_Data.csv", second_closest_size, length)

        #Get the slope between these
        cap1_slope = (closest_cap1 - second_closest_cap1)/(closest_size - second_closest_size)
        time1_slope = (closest_time1 - second_closest_time1)/(closest_size - second_closest_size)
        cap2_slope = (closest_cap2 - second_closest_cap2)/(closest_size - second_closest_size)
        time2_slope = (closest_time2 - second_closest_time2)/(closest_size - second_closest_size)

        #Calculate the interpolated values
        cap1_interpolated = second_closest_cap1 + cap1_slope * (size - second_closest_size)
        time1_interpolated = second_closest_time1 + time1_slope * (size - second_closest_size)
        cap2_interpolated = second_closest_cap2 + cap2_slope * (size - second_closest_size)
        time2_interpolated = second_closest_time2 + time2_slope * (size - second_closest_size)

        #Return the interpolated values
        return cap1_interpolated, time1_interpolated, cap2_interpolated, time2_interpolated
    
def Interpolation(filename, size, length):
    #First check the inputs - If it isn't possible, return all -1s
    if size not in [1, 2, 4, 6, 8, 12, 16]: return -1, -1, -1
    if length % 2 != 0 or length < 8 or length > 20: return -1, -1, -1

    #Read in the CSV file and fill out a dictionary of properties
    E_dict = {}
    T_dict = {}
    R_dict = {}
    with open(filename, mode ='r') as file:
        csvFile = csv.reader(file)
        for i,lines in enumerate(csvFile):
                if i != 0:
                    if lines[0] not in E_dict.keys():
                        E_dict[lines[0]] = {}
                        T_dict[lines[0]] = {}
                        R_dict[lines[0]] = {}
                    E_dict[lines[0]][lines[1]] = float(lines[2])
                    T_dict[lines[0]][lines[1]] = float(lines[3])
                    R_dict[lines[0]][lines[1]] = float(lines[4])

    #These vectors contain the sizes and lengths that we simulated
    Valid_Sizes = [1, 2, 4, 8, 16]    
    Valid_Lengths = [8, 12, 16]

    #First case - We already have the value and we should just return it
    if size in Valid_Sizes and length in Valid_Lengths: return E_dict[str(size)][str(length)], T_dict[str(size)][str(length)], R_dict[str(size)][str(length)]

    #Second case - We have a valid size but not a valid length.
    if size in Valid_Sizes and length not in Valid_Lengths:
        #First, we want to find the two values closest to the given length such that we can "interpolate" from those values linearly
        dist = np.array(Valid_Lengths) - length
        closest_length_index = np.argmin(abs(dist))

        dist_without_closest = np.delete(dist, closest_length_index)
        second_closest_dist = dist_without_closest[np.argmin(abs(dist_without_closest))]
        second_closest_length_index = np.where(dist == second_closest_dist)[0][0]

        closest_length = Valid_Lengths[closest_length_index]
        second_closest_length = Valid_Lengths[second_closest_length_index]

        #Next, get the slopes between the lengths
        E_slope = (E_dict[str(size)][str(closest_length)] - E_dict[str(size)][str(second_closest_length)])/(closest_length - second_closest_length)
        T_slope = (T_dict[str(size)][str(closest_length)] - T_dict[str(size)][str(second_closest_length)])/(closest_length - second_closest_length)
        R_slope = (R_dict[str(size)][str(closest_length)] - R_dict[str(size)][str(second_closest_length)])/(closest_length - second_closest_length)

        #Now, interpolate from the closest length
        E_interpolated = E_slope * (length - closest_length) + E_dict[str(size)][str(closest_length)]
        T_interpolated = T_slope * (length - closest_length) + T_dict[str(size)][str(closest_length)]
        R_interpolated = R_slope * (length - closest_length) + R_dict[str(size)][str(closest_length)]

        #Return the interpolated values
        return E_interpolated, T_interpolated, R_interpolated
    
    #Third case - We have a valid length but not a valid size.
    if size not in Valid_Sizes and length in Valid_Lengths:
        #First, we want to find the two values closest to the given size such that we can "interpolate" from those values linearly
        dist = np.array(Valid_Sizes) - size
        closest_size_index = np.argmin(abs(dist))

        dist_without_closest = np.delete(dist, closest_size_index)
        second_closest_dist = dist_without_closest[np.argmin(abs(dist_without_closest))]
        second_closest_size_index = np.where(dist == second_closest_dist)[0][0]

        closest_size = Valid_Sizes[closest_size_index]
        second_closest_size = Valid_Sizes[second_closest_size_index]

        #Next, get the slopes between the sizes
        E_slope = (E_dict[str(closest_size)][str(length)] - E_dict[str(second_closest_size)][str(length)])/(closest_size - second_closest_size)
        T_slope = (T_dict[str(closest_size)][str(length)] - T_dict[str(second_closest_size)][str(length)])/(closest_size - second_closest_size)
        R_slope = (R_dict[str(closest_size)][str(length)] - R_dict[str(second_closest_size)][str(length)])/(closest_size - second_closest_size)

        #Now, interpolate from the closest sizes
        E_interpolated = E_slope * (size - closest_size) + E_dict[str(closest_size)][str(length)]
        T_interpolated = T_slope * (size - closest_size) + T_dict[str(closest_size)][str(length)]
        R_interpolated = R_slope * (size - closest_size) + R_dict[str(closest_size)][str(length)]

        #Return the interpolated values
        return E_interpolated, T_interpolated, R_interpolated
    
    #Fourth case - Both length and size were not valid
    if size not in Valid_Sizes and length not in Valid_Lengths:
        #First, we want to find the two values closest to the given size
        dist = np.array(Valid_Sizes) - size
        closest_size_index = np.argmin(abs(dist))

        dist_without_closest = np.delete(dist, closest_size_index)
        second_closest_dist = dist_without_closest[np.argmin(abs(dist_without_closest))]
        second_closest_size_index = np.where(dist == second_closest_dist)[0][0]

        closest_size = Valid_Sizes[closest_size_index]
        second_closest_size = Valid_Sizes[second_closest_size_index]

        #Now, interpolate between lengths first to give us two sets of values - one for each size

        #We do this by just calling the same function twice for the closest two sizes, and interpolate between them
        closest_size_E, closest_size_T, closest_size_R = Interpolation(filename, closest_size, length)
        second_closest_size_E, second_closest_size_T, second_closest_size_R = Interpolation(filename, second_closest_size, length)

        E_slope = (closest_size_E - second_closest_size_E)/(closest_size - second_closest_size)
        T_slope = (closest_size_T - second_closest_size_T)/(closest_size - second_closest_size)
        R_slope = (closest_size_R - second_closest_size_R)/(closest_size - second_closest_size)

        E_interpolated = E_slope * (size - closest_size) + closest_size_E
        T_interpolated = T_slope * (size - closest_size) + closest_size_T
        R_interpolated = R_slope * (size - closest_size) + closest_size_R

        #Return the interpolated values
        return E_interpolated, T_interpolated, R_interpolated

#time1, cap1, time2, cap2 = SimInterpolation("Time_Data.csv", 6, 10)
#E, T, R = Interpolation("Data.csv", 6, 10)
#T = TimeInterpolation("Time_Data.csv", 6, 10, 12.5)
