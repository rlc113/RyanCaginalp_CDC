#This file allows the user to modify simulation files to create custom simulations
import sys

source_file = "/content/RyanCaginalp_CDC/NgSpice/CDC_PEX_1_Test.cir"
destination_file = "/content/RyanCaginalp_CDC/NgSpice/CDC_PEX_Test.cir"

#Desired parameters for simulation - simulation_time should overshoot, while execution_time should undershoot
#These values are obtained through the input arguments, if present
simulation_time = 140
execution_time = 100
reset_time = 60
capacitance = 1.25
if (len(sys.argv) == 5):
    simulation_time = int(sys.argv[1])
    execution_time = int(sys.argv[2])
    reset_time = int(sys.argv[3])
    capacitance = float(sys.argv[4])

sf = open(source_file, "r")
df = open(destination_file, "w")

sf_lines = sf.readlines()
df_lines = []
CDC = False
Plus_Streak = False

#Loop over all lines in file
for l in sf_lines:
    #This modifies the test capacitance
    if "C0 V_SENSE" in l:
        split_l = l.split(" ")
        split_l[3] = str(capacitance) + "pF\n"
        l = " ".join(split_l)
    #These modify the lines that depend on simulation_time (run time, counter measurements)
    elif ".tran" in l:
        split_l = l.split(" ")
        split_l[2] = str(simulation_time) + "ns"
        l = " ".join(split_l)   
    elif "find" in l:
        split_l = l.split(" ")
        split_l[9] = "at=" + str(simulation_time) + "ns\n"
        l = " ".join(split_l)
    #These modify the lines that depend on reset_time (reset pulse, power measurements before/after reset)
    elif "V3 R" in l:
        split_l = l.split(" ")
        split_l[6] = str(reset_time) + "ns"
        l = " ".join(split_l) 
    elif "meas tran PLBR" in l:
        split_l = l.split(" ")
        split_l[10] = "to=" + str(reset_time-1) + "ns\n"
        l = " ".join(split_l)               
    elif "meas tran PHBR" in l:
        split_l = l.split(" ")
        split_l[10] = "to=" + str(reset_time-1) + "ns\n"
        l = " ".join(split_l)
    #These modify the lines that depend on execution_time (power measurement after reset)     
    elif "meas tran PLAR" in l:
        split_l = l.split(" ")
        split_l[9] = "from=" + str(reset_time+1) + "ns"
        split_l[10] = "to=" + str(execution_time) + "ns\n"
        l = " ".join(split_l)               
    elif "meas tran PHAR" in l:
        split_l = l.split(" ")
        split_l[9] = "from=" + str(reset_time+1) + "ns"
        split_l[10] = "to=" + str(execution_time) + "ns\n"
        l = " ".join(split_l)               
    df_lines.append(l)

df_lines[len(df_lines) - 1] = df_lines[len(df_lines) - 1].replace('\n', '')

df.writelines(df_lines)

sf.close()
df.close()
