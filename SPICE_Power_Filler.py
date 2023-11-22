#This script modifies the SPICE file outputted by YoSys so that they have power ports - it also reshuffles some ports that were incorrectly modified
source_file = "/home/ryan/openROADTests/SynthesizedExtraction.spice"
destination_file = "/home/ryan/openROADTests/LVS/SynthesizedExtraction.spice"

sf = open(source_file, "r")
df = open(destination_file, "w")

sf_lines = sf.readlines()
df_lines = []

#Loop through every line of the input file
for l in sf_lines:
  #This if statement is for an inverter
  if "sky130_fd_sc_hd__inv_" in l:
    #If this inverter is in the capacitance chain, attach it to V_SENSE (We ascertain this by looking at the output)
    if "CAP_CHAIN" in l.split(" ")[2]:
      ports = l.split(" ")
      ports.insert(2, "V_GND")
      ports.insert(3, "V_GND")
      ports.insert(4, "V_SENSE")
      ports.insert(5, "V_SENSE")
      l = " ".join(ports)
    #The last inverter in the chain driver should be powered by V_HIGH for the sensed capacitance - same for the reset inverter
    elif ("chain_driver_last_inv" in l.split(" ")[2] and ".O" in l.split(" ")[2]) or (" ResetB" in l):
      ports = l.split(" ")
      ports.insert(2, "V_GND")
      ports.insert(3, "V_GND")
      ports.insert(4, "V_HIGH")
      ports.insert(5, "V_HIGH")
      l = " ".join(ports)
    #Everything else receives V_LOW
    else:
      ports = l.split(" ")
      ports.insert(2, "V_GND")
      ports.insert(3, "V_GND")
      ports.insert(4, "V_LOW")
      ports.insert(5, "V_LOW")
      l = " ".join(ports)
  #NAND2 all receive V_LOW
  if ("sky130_fd_sc_hd__nand2_" in l) or ("sky130_fd_sc_hd__nor2_" in l):
    ports = l.split(" ")
    ports.insert(3, "V_GND")
    ports.insert(4, "V_GND")
    ports.insert(5, "V_LOW")
    ports.insert(6, "V_LOW")
    l = " ".join(ports)
  #NAND3 all receive V_LOW, but for some reason O and C are switched for YoSys output...
  if ("sky130_fd_sc_hd__nand3_" in l):
    ports = l.split(" ")
    ports.insert(4, "V_GND")
    ports.insert(5, "V_GND")
    ports.insert(6, "V_LOW")
    ports.insert(7, "V_LOW")
    ports[3], ports[8] = ports[8], ports[3]
    l = " ".join(ports)
  #TiHi Cells receive V_LOW
  if "sky130_fd_sc_hd__conb_1" in l:
    ports = l.split(" ")
    ports.insert(1, "V_GND")
    ports.insert(2, "V_GND")
    ports.insert(3, "V_LOW")
    ports.insert(4, "V_LOW")
    l = " ".join(ports)
  #DFF ports were completely and utterly butchered by YoSys, so they need to be reshuffled - also they all get V_LOW
  if "sky130_fd_sc_hd__dfbbn_" in l:
    ports_LIB = l.split(" ")
    ports_SPICE = []

    ports_SPICE.append(ports_LIB[0])
    ports_SPICE.append(ports_LIB[3])
    ports_SPICE.append(ports_LIB[2])
    ports_SPICE.append(ports_LIB[5])
    ports_SPICE.append(ports_LIB[6])
    ports_SPICE.append(ports_LIB[1])
    ports_SPICE.append(ports_LIB[4])
    ports_SPICE.append(ports_LIB[7])

    ports_SPICE.insert(5, "V_GND")
    ports_SPICE.insert(6, "V_GND")
    ports_SPICE.insert(7, "V_LOW")
    ports_SPICE.insert(8, "V_LOW")
    l = " ".join(ports_SPICE)
  #Transmission gates will always have a certain form, so replace the line altogether
  if "transmission_gate" in l.split(" ")[len(l.split(" ")) - 1]:
  	l = l.split(" ")[0] + " V_SENSE Reset V_HIGH V_GND ResetB transmission_gate\n"

  df_lines.append(l)

df_lines[len(df_lines) - 1] = df_lines[len(df_lines) - 1].replace('\n', '')

df.writelines(df_lines)

sf.close()
df.close()
