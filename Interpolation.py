import csv
import numpy as np
import math

def TimeInterpolation(filename, size, length, capacitance):
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

    #First case - The size and length were already simulated
    if size in Valid_Sizes and length in Valid_Lengths:
        #Get the capacitances and use it to get the slope
        T_slope = (T_dict[str(size)][str(length)][1][1] - T_dict[str(size)][str(length)][0][1])/(T_dict[str(size)][str(length)][1][0] - T_dict[str(size)][str(length)][0][0])

        #Then we can predict the time
        T_interpolated = T_dict[str(size)][str(length)][0][1] + T_slope * (capacitance - T_dict[str(size)][str(length)][0][0])
        return T_interpolated

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

        #Next, get the interpolated time for each length
        closest_length_T = TimeInterpolation(filename, size, closest_length, capacitance)
        second_closest_length_T = TimeInterpolation(filename, size, second_closest_length, capacitance)

        #Get the slope between these lengths
        T_slope = (closest_length_T - second_closest_length_T)/(closest_length - second_closest_length)

        #Calculate interpolated time
        T_interpolated = second_closest_length_T + T_slope * (length - second_closest_length)

        #Return the interpolated time
        return T_interpolated
    
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

        #Next, get the interpolated time for each length
        closest_size_T = TimeInterpolation(filename, closest_size, length, capacitance)
        second_closest_size_T = TimeInterpolation(filename, second_closest_size, length, capacitance)

        #Get the slope between these lengths
        T_slope = (closest_size_T - second_closest_size_T)/(closest_size - second_closest_size)

        #Calculate interpolated time
        T_interpolated = second_closest_size_T + T_slope * (size - second_closest_size)

        #Return the interpolated time
        return T_interpolated

    #Fourth case - neither length nor size was simulated
    if size not in Valid_Sizes and length not in Valid_Lengths:
        #First, we want to find the two values closest to the given size
        dist = np.array(Valid_Sizes) - size
        closest_size_index = np.argmin(abs(dist))

        dist_without_closest = np.delete(dist, closest_size_index)
        second_closest_dist = dist_without_closest[np.argmin(abs(dist_without_closest))]
        second_closest_size_index = np.where(dist == second_closest_dist)[0][0]

        closest_size = Valid_Sizes[closest_size_index]
        second_closest_size = Valid_Sizes[second_closest_size_index]

        #Next, get the interpolated time for each length
        closest_size_T = TimeInterpolation(filename, closest_size, length, capacitance)
        second_closest_size_T = TimeInterpolation(filename, second_closest_size, length, capacitance)

        #Get the slope between these lengths
        T_slope = (closest_size_T - second_closest_size_T)/(closest_size - second_closest_size)

        #Calculate interpolated time
        T_interpolated = second_closest_size_T + T_slope * (size - second_closest_size)

        #Return the interpolated time
        return T_interpolated

    
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

#E, T, R = Interpolation("Data.csv", 6, 10)
#T = TimeInterpolation("Time_Data.csv", 6, 10, 12.5)