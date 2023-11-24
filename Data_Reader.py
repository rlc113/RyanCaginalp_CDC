#This function gets us the results of a simulation
def data_reader(source_file, reset_time, precision):

    sf = open(source_file, "r")

    sf_lines = sf.readlines()
    
    ds1_binary = [];
    ds2_binary = [];
    dm_binary = [];

    stage = 0;
    index = 0;
    stop_time = -1.0;

    low_power_before_reset = 0;
    low_power_after_reset = 0;
    high_power_before_reset = 0;
    high_power_after_reset = 0;

    #This loops over every line in the log file
    for l in sf_lines:
        #This checks if operation has completed - if so, then we record the stop time
        if (stop_time < 0):
            if "Index" in l and "time" in l and "cf" in l: stage = 1;
            elif (l.split("\t")[0] == str(index)):
                if (stage == 1 and float(l.split("\t")[2]) > 1.3): stop_time = float(l.split("\t")[1])
                else: index += 1

        #This reads the binary outputs of the counters
        if "ds1" == l.split(".")[0]: ds1_binary.append(float(l.split(" ")[len(l.split(" ")) - 1]) > 0.7)
        if "ds2" == l.split(".")[0]: ds2_binary.append(float(l.split(" ")[len(l.split(" ")) - 1]) > 0.7)
        if "dm" == l.split(".")[0]: dm_binary.append(float(l.split(" ")[len(l.split(" ")) - 1]) > 0.7)

        #This reads the various powers (combinations of low/high voltage and before/after reset) 
        if "plbr" == l.split(" ")[0]:
            eqmatch = False;
            for i in range(len(l.split(" "))):
                if (l.split(" ")[i] == "="): eqmatch = True
                elif eqmatch and l.split(" ")[i] != '':
                    low_power_before_reset = float(l.split(" ")[i])
                    eqmatch = False
        if "plar" == l.split(" ")[0]:
            eqmatch = False;
            for i in range(len(l.split(" "))):
                if (l.split(" ")[i] == "="): eqmatch = True
                elif eqmatch and l.split(" ")[i] != '':
                    low_power_after_reset = float(l.split(" ")[i])
                    eqmatch = False
        if "phbr" == l.split(" ")[0]:
            eqmatch = False;
            for i in range(len(l.split(" "))):
                if (l.split(" ")[i] == "="): eqmatch = True
                elif eqmatch and l.split(" ")[i] != '':
                    high_power_before_reset = float(l.split(" ")[i])
                    eqmatch = False
        if "phar" == l.split(" ")[0]:
            eqmatch = False;
            for i in range(len(l.split(" "))):
                if (l.split(" ")[i] == "="): eqmatch = True
                elif eqmatch and l.split(" ")[i] != '':
                    high_power_after_reset = float(l.split(" ")[i])
                    eqmatch = False

    #Average powers and get energy
    low_power = (low_power_before_reset * reset_time + (low_power_after_reset * (stop_time - reset_time)))/stop_time
    high_power = (high_power_before_reset * reset_time + (high_power_after_reset * (stop_time - reset_time)))/stop_time
    total_energy = (low_power + high_power) * stop_time

    #Finally convert binary outputs into decimal ones

    ds1 = 0;
    ds2 = 0;
    dm = 0;
    
    for i, x in enumerate(ds1_binary):
        if x: ds1 += pow(2, i)

    for i, x in enumerate(ds2_binary):
        if x: ds2 += pow(2, i)

    for i, x in enumerate(dm_binary):
        if x: dm += pow(2, i)

    sf.close()
    
    return low_power, high_power, stop_time, total_energy, ds1, ds2, dm
