source_file = "Comp.spice"
destination_file = "Comp_Power.spice"

sf = open(source_file, "r")
df = open(destination_file, "w")

sf_lines = sf.readlines()
df_lines = []

for l in sf_lines:
  if "sky130_fd_sc_hd__inv_" in l:
    if "CAP_CHAIN" in l.split(" ")[2]:
      ports = l.split(" ")
      ports.insert(2, "V_GND")
      ports.insert(3, "V_GND")
      ports.insert(4, "V_SENSE")
      ports.insert(5, "V_SENSE")
      l = " ".join(ports)
    elif ("Next_Edge_LowV_b" in l) or (" ResetB" in l):
      ports = l.split(" ")
      ports.insert(2, "V_GND")
      ports.insert(3, "V_GND")
      ports.insert(4, "V_HIGH")
      ports.insert(5, "V_HIGH")
      l = " ".join(ports)
    else:
      ports = l.split(" ")
      ports.insert(2, "V_GND")
      ports.insert(3, "V_GND")
      ports.insert(4, "V_LOW")
      ports.insert(5, "V_LOW")
      l = " ".join(ports)
  if ("sky130_fd_sc_hd__nand2_" in l) or ("sky130_fd_sc_hd__nor2_" in l):
    ports = l.split(" ")
    ports.insert(3, "V_GND")
    ports.insert(4, "V_GND")
    ports.insert(5, "V_LOW")
    ports.insert(6, "V_LOW")
    l = " ".join(ports)
  if ("sky130_fd_sc_hd__nand3_" in l):
    ports = l.split(" ")
    ports.insert(4, "V_GND")
    ports.insert(5, "V_GND")
    ports.insert(6, "V_LOW")
    ports.insert(7, "V_LOW")
    ports[3], ports[8] = ports[8], ports[3]
    l = " ".join(ports)
  if "sky130_fd_sc_hd__conb_1" in l:
    ports = l.split(" ")
    ports.insert(1, "V_GND")
    ports.insert(2, "V_GND")
    ports.insert(3, "V_LOW")
    ports.insert(4, "V_LOW")
    l = " ".join(ports)
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
  df_lines.append(l)

df_lines[len(df_lines) - 1] = df_lines[len(df_lines) - 1].replace('\n', '')

df.writelines(df_lines)

sf.close()
df.close()
