# Set this variable to true if you wish the tool to consider 
# interpolated designs (i.e.) those that weren't simulated,
# but whose properties were linearly interpolated from existing
# data. If set to False, only directly simulated designs will
# be considered. 
interpolated = True

# If this variable is true, then the tool will return the five designs
# that are as close to the targeted value given below. If false, then
# the the tool will attempt to maximize an FoM that is returned by the
# FoM function below
targeted_true_FoM_false = True

# If the target variable is true, then we must specify a target type
# and value. The type can either be "Energy", "Time", or "Res":
#
# "Energy" - Conversion Energy per Input Capacitance
# "Time" - Conversion Time per Input Capacitance
# "Res" - Output Step Size. (A rise in the input capacitance by this amount will cause the output to rise by 1)
#
# To choose, simply uncomment the line associated with target type
# of your choice. If the target type is set to a string that is
# not one of these three, then the tool will throw an error

#target_type = "Energy"
#target_type = "Time"
target_type = "Res"

# The target value is the value the tool will aim for.
# Units and recommended ranges for each variable is given below (It's also recommended to look at the "Data.csv" file in the same folder to get an idea of the spread of the CDC properties)
# Energy - Joules/Farad (Range of 6-17 for non-interpolated, )
# Time - Seconds/MilliFarad (Range of 2-40 for non-interpolated, )
# Output Step Size - picoFarads (Range of 0.1-2.5 for non-interpolated, )
# If the target variable is true, then one and only one of these
# target variables must be positive. Otherwise, the tool will throw
# an error.
target_value = 0.3 

# This is our FoM function - E is conversion energy per input capacitance,
# T is conversion time per input capacitance, and R is output step size.
# All three have the same units as the target variable. Please bear in
# mind that we prefer all three properties to be as low as possible when
# building your own FoM function
def FoM(E, T, R):
    return (1/(E * T * R))

# When this variable is true, all of our designs are subject to a
# restriction, set by the below restriction function. In other words,
# any design the tool returns must satisfy the restriction
restricted = False

# This is our restriction function - E, T, and R are the same as they were for
# the FoM function. When the function returns true, it means the design passes
# the restriction. If it returns false, the design does not pass
def Restriction(E, T, R):
    return (E < 10)