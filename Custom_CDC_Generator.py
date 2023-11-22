import math
import sys

#Desired configuration of CDC - get from command line arguments, if available
chain_length = 8
chain_number = 1
chain_size = 1
if (len(sys.argv) == 4):
    chain_length = int(sys.argv[1])
    chain_number = int(sys.argv[2])
    chain_size = int(sys.argv[3])

#First generate the verilog chain files

source_file = open('Templates/Inverter_Chain_Template.v', 'r')
destination_file = open('HW_CDC_Verilog/Inverter_Chains.v', 'w')

sf_lines = source_file.readlines()
df_lines = []

for line in sf_lines:
    df_lines.append(line)
    if "Normal_Inverter_Chain" in line:
        df_lines.append("\n")

        #Create wires
        for i in range(chain_length): df_lines.append("    wire low_chain" + str(i) + ";\n")

        df_lines.append("\n")

        #Create first inverter(s)
        for j in range(chain_number): df_lines.append("    custom_chainInverter low_chain_inv1_" + str(j+1) + "(.I(I), .O(low_chain1));\n")

        #Create middle inverters
        for i in range(2, chain_length):
            for j in range(chain_number): df_lines.append("    custom_chainInverter low_chain_inv" + str(i) + "_" + str(j+1) + "(.I(low_chain" + str(i-1) + "), .O(low_chain" + str(i) + "));\n")

        #Create final inverter(s)
        for j in range(chain_number): df_lines.append("    custom_chainInverter low_chain_inv" + str(chain_length) + "_" + str(j+1) + "(.I(low_chain" + str(chain_length-1) + "), .O(O));\n")

        df_lines.append("\n")

    if "Cap_Inverter_Chain" in line:
        df_lines.append("\n")

        #Create wires
        for i in range(chain_length): df_lines.append("    wire cap_chain" + str(i) + ";\n")

        df_lines.append("\n")

        #Create first inverter(s)
        for j in range(chain_number): df_lines.append("    custom_chainInverter cap_chain_inv1_" + str(j+1) + "(.I(I), .O(cap_chain1));\n")

        #Create middle inverters
        for i in range(2, chain_length):
            for j in range(chain_number): df_lines.append("    custom_chainInverter cap_chain_inv" + str(i) + "_" + str(j+1) + "(.I(cap_chain" + str(i-1) + "), .O(cap_chain" + str(i) + "));\n")

        #Create final inverter(s)
        for j in range(chain_number): df_lines.append("    custom_chainInverter cap_chain_inv" + str(chain_length) + "_" + str(j+1) + "(.I(cap_chain" + str(chain_length-1) + "), .O(O));\n")

        df_lines.append("\n")

    if "Finish_Inverter_Chain" in line:
        df_lines.append("\n")

        #Create wires
        for i in range(chain_length): df_lines.append("    wire finish_chain" + str(i) + ";\n")

        df_lines.append("\n")

        #Create first inverter(s)
        for j in range(chain_number): df_lines.append("    custom_chainInverter finish_chain_inv1_" + str(j+1) + "(.I(I), .O(finish_chain1));\n")

        #Create middle inverters
        for i in range(2, chain_length - 1):
            for j in range(chain_number): df_lines.append("    custom_chainInverter finish_chain_inv" + str(i) + "_" + str(j+1) + "(.I(finish_chain" + str(i-1) + "), .O(finish_chain" + str(i) + "));\n")

        #Create final inverters
        for j in range(chain_number): df_lines.append("    custom_chainInverter finish_chain_inv" + str(chain_length-1) + "_" + str(j+1) + "(.I(finish_chain" + str(chain_length-2) + "), .O(Ob));\n")
        for j in range(chain_number): df_lines.append("    custom_chainInverter finish_chain_inv" + str(chain_length) + "_" + str(j+1) + "(.I(Ob), .O(O));\n")

        df_lines.append("\n")

destination_file.writelines(df_lines)

source_file.close()
destination_file.close()

#Then generate the verilog gate file
source_file = open('Templates/Physical_Gates_Template.v', 'r')
destination_file = open('HW_CDC_Verilog/Physical_Gates.v', 'w')

sf_lines = source_file.readlines()
df_lines = []

for line in sf_lines:
    df_lines.append(line)
    if "custom_chainInverter" in line: df_lines.append("    sky130_fd_sc_hd__inv_" + str(chain_size) + " cell_INV(.A(I), .Y(O));\n")

destination_file.writelines(df_lines)

source_file.close()
destination_file.close()

#Finally, add the transmission gates to the CDC file
source_file = open('Templates/CDC_Template.v', 'r')
destination_file = open('HW_CDC_Verilog/CDC.v', 'w')

sf_lines = source_file.readlines()
df_lines = []

#Figure out how many transmission gates we need
transmission_gate_number = max(5, math.ceil(5 * chain_length * chain_number * chain_size / 16.0))

for line in sf_lines:
    df_lines.append(line)
    if "sky130_fd_sc_hd__inv_16 HIGH_RESET_INV" in line:
        for i in range(transmission_gate_number):
            df_lines.append("    transmission_gate CDC_TRANSMISSION_GATE" + str(i+1) + "(.G(Reset), .GN(ResetB), .O(V_SENSE));\n")

destination_file.writelines(df_lines)

source_file.close()
destination_file.close()

#Then generate the chain driver file
source_file = open('Templates/Chain_Driver_Template.v', 'r')
destination_file = open('HW_CDC_Verilog/Chain_Driver.v', 'w')

sf_lines = source_file.readlines()
df_lines = []

last_inverter_number = 0

for line in sf_lines:
    df_lines.append(line)
    if "chain_driver" in line:
        #First figure out how big our load is
        chain_capacitance = 2 * chain_number * chain_size

        #Overshoot to the next power of 2.
        i = 0
        while (pow(2, i) < chain_capacitance): i += 1

        #Get the target size for the final inverter in our driver chain
        last_inverter_size = pow(2, i)

        #Also save the last number of inverters for future reference
        last_inverter_number = round(pow(2, i)/16)
        if (last_inverter_number == 0): last_inverter_number += 1

        #Now start generating our chain - first figure out how many inverters we need (this is just i rounded up to the nearest power of 2)
        inverter_number = i + (i % 2)

        df_lines.append("\n")

        #Define the wires in between first
        for i in range(1, inverter_number): df_lines.append("    wire chain_driver" + str(pow(2, i)) + ";\n")

        df_lines.append("\n")

        #Do the first inverter
        df_lines.append("    custom_Inverter2 chain_driver_inv2(.I(Next_Edge_LowV), .O(chain_driver2));\n")

        #Do the middle inverters
        for i in range(2, inverter_number):
            if pow(2, i) > 16:
                for j in range(round(pow(2, i)/16)):
                    df_lines.append("    custom_Inverter16 chain_driver_inv" + str(pow(2, i)) + "_" + str(j+1) + "(.I(chain_driver" + str(pow(2, i-1)) + "), .O(chain_driver" + str(pow(2,i)) + "));\n")
            else: df_lines.append("    custom_Inverter" + str(pow(2, i)) + " chain_driver_inv" + str(pow(2, i)) + "(.I(chain_driver" + str(pow(2, i-1)) + "), .O(chain_driver" + str(pow(2,i)) + "));\n")

        #Do the final inverter
        if last_inverter_size > 16:
            for j in range(round(last_inverter_size/16)):
                df_lines.append("    custom_Inverter16 chain_driver_last_inv_" + str(j+1) + "(.I(chain_driver" + str(pow(2, inverter_number - 1)) + "), .O(Next_Edge_HighV));\n")
        else: df_lines.append("    custom_Inverter" + str(last_inverter_size) + " chain_driver_last_inv(.I(chain_driver" + str(pow(2, inverter_number - 1)) + "), .O(Next_Edge_HighV));\n")

        df_lines.append("\n")

destination_file.writelines(df_lines)

source_file.close()
destination_file.close()

#Next up are the domain lists - starting with V_HIGH
destination_file = open('Other/V_HIGH_INSTANCES.txt', 'w')

#Add in gates we know will be there
df_lines = []
df_lines.append("HIGH_RESET_INV\n")
for i in range(transmission_gate_number): df_lines.append("CDC_TRANSMISSION_GATE" + str(i+1) + "\n")

#Add in the last gates of the chain drivers
if last_inverter_number == 1: df_lines.append("\CDC_CHAIN_DRIVER.chain_driver_last_inv.cell_INV\n")
else:
    for i in range(last_inverter_number): df_lines.append("\CDC_CHAIN_DRIVER.chain_driver_last_inv_" + str(i+1) + ".cell_INV\n")

#Remove last newline
df_lines[len(df_lines) - 1] = df_lines[len(df_lines) - 1].replace("\n", "")

destination_file.writelines(df_lines)
destination_file.close()

#Next do V_SENSE
destination_file = open('Other/V_SENSE_INSTANCES.txt', 'w')
df_lines = []

#Add in the inverter chain inverters
for i in range(chain_length):
    for j in range(chain_number):
        df_lines.append("\CAP_CHAIN.cap_chain_inv" + str(i+1) + "_" + str(j+1) + ".cell_INV\n")

#Remove last newline
df_lines[len(df_lines) - 1] = df_lines[len(df_lines) - 1].replace("\n", "")

destination_file.writelines(df_lines)
destination_file.close()

#Finally add in some routing stuff to make sure that transmission gates can be connected to V_SENSE
destination_file = open('Other/V_SENSE_Routes.txt', 'w')
df_lines = []

df_lines.append("r_V_SENSE\n")

#Add in the inverter chain inverters
for i in range(transmission_gate_number):
    df_lines.append("CDC_TRANSMISSION_GATE" + str(i+1) + " O\n")

#Remove last newline
df_lines[len(df_lines) - 1] = df_lines[len(df_lines) - 1].replace("\n", "")

destination_file.writelines(df_lines)
destination_file.close()

#Next, we should process the TCL files - make sure that they have the right information for the process

#First is floorplanning - before we edit the file, we need to calculate some sizes

#Figure out the heights first

#The V_HIGH region should always have 6 rows for a height of 21, so nothing needs to be changed for it

#The V_SENSE region should have as many rows as it has chains - the height will reflect that
V_SENSE_Height = 7
if chain_number == 2: V_SENSE_Height = 10
elif chain_number == 3: V_SENSE_Height = 12
elif chain_number == 4: V_SENSE_Height = 14

#The chip height will fit snugly to the two voltage regions
core_height = 160
die_height = 190

#Now figure out the widths

#Define some widths that will aid us with calculation
inv_1_width = 1.38
inv_2_width = 1.38
inv_4_width = 2.30
inv_6_width = 3.22
inv_8_width = 4.14
inv_12_width = 5.98
inv_16_width = 7.36
transmission_gate_width = 3.22

#Calculate the V_SENSE region width first
V_SENSE_Width = inv_1_width * chain_length * 2
if (chain_size == 4): V_SENSE_Width = inv_4_width * chain_length * 2
if (chain_size == 6): V_SENSE_Width = inv_6_width * chain_length * 2
if (chain_size == 8): V_SENSE_Width = inv_8_width * chain_length * 2
if (chain_size == 12): V_SENSE_Width = inv_12_width * chain_length * 2
if (chain_size == 16): V_SENSE_Width = inv_16_width * chain_length * 2

#Then calculate the V_HIGH region width
V_HIGH_Width = transmission_gate_number * transmission_gate_width + inv_16_width
if (last_inverter_size == 2): V_HIGH_Width += inv_2_width
elif (last_inverter_size == 4): V_HIGH_Width += inv_4_width
elif (last_inverter_size == 8): V_HIGH_Width += inv_8_width
elif (last_inverter_size == 16): V_HIGH_Width += inv_16_width
else: V_HIGH_Width += inv_16_width * last_inverter_size/16.0
V_HIGH_Width *= 0.75

#print(V_SENSE_Width)
#print(V_HIGH_Width)

#Finally calculate the chip width
core_width = max(V_SENSE_Width, V_HIGH_Width) * 1.2 + 100 + 30
die_width = core_width + 30

source_file = open('Templates/Floorplanning_Template.tcl', 'r')
destination_file = open('Floorplanning.tcl', 'w')

sf_lines = source_file.readlines()
df_lines = []

for line in sf_lines:

    if "set V_HIGH_WIDTH" in line:
        words = line.split(" ")
        words[2] = str(math.ceil(V_HIGH_Width)) + "\n"
        line = " ".join(words)
    elif "set V_SENSE_WIDTH" in line:
        words = line.split(" ")
        words[2] = str(math.ceil(V_SENSE_Width)) + "\n"
        line = " ".join(words)
    elif "set V_SENSE_HEIGHT" in line:
        words = line.split(" ")
        words[2] = str(math.ceil(V_SENSE_Height)) + "\n"
        line = " ".join(words)
    elif "initialize_floorplan -die_area" in line: line = 'initialize_floorplan -die_area "0 0 ' + str(math.ceil(die_width)) + ' 190" -core_area "30 30 ' + str(math.ceil(core_width)) + ' 160" -site unithd'

    df_lines.append(line)

    if "add_global_connection -net V_SENSE -inst_pattern {CAP_CHAIN.*}" in line:
        if last_inverter_number == 1: df_lines.append("add_global_connection -net V_HIGH -inst_pattern {CDC_CHAIN_DRIVER.chain_driver_last_inv.cell_INV} -pin_pattern {VPWR|VPB} -power\n")
        else:
            for i in range(last_inverter_number): df_lines.append("add_global_connection -net V_HIGH -inst_pattern {CDC_CHAIN_DRIVER.chain_driver_last_inv_" + str(i+1) + ".cell_INV} -pin_pattern {VPWR|VPB} -power\n")

    if "add_global_connection -net V_HIGH -inst_pattern {HIGH_RESET_INV}" in line:
       for i in range(transmission_gate_number):
           df_lines.append("add_global_connection -net V_HIGH -inst_pattern {CDC_TRANSMISSION_GATE" + str(i+1) + "} -pin_pattern {VPWR|VPB} -power\n")

destination_file.writelines(df_lines)

source_file.close()
destination_file.close()
