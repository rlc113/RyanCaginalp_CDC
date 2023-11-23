#This file removes the DC connections that preserve wirenames since they crash the LVS tool
source_file = "/content/RyanCaginalp_CDC/LVS/SynthesizedExtraction.spice"
destination_file = "/content/RyanCaginalp_CDC/LVS/SynthesizedExtraction_Without_DC.spice"

sf = open(source_file, "r")
df = open(destination_file, "w")

sf_lines = sf.readlines()
df_lines = []

for l in sf_lines:
  if "DC 0" not in l: df_lines.append(l)


#Also remove last new line and include libraries and transmission_gate simulation files
df_lines[len(df_lines) - 1] = df_lines[len(df_lines) - 1].replace('\n', '')

df_lines.insert(1, '.include "/home/ryan/MagicTests/SKY130/git_open_pdks/sky130/sky130A/libs.ref/sky130_fd_sc_hd/spice/sky130_fd_sc_hd.spice"\n')
df_lines.insert(1, '.include "transmission_gate.spice"\n')

df.writelines(df_lines)

sf.close()
df.close()
