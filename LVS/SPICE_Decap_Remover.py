#This file removes decap cells from extracted SPICE file as they aren't present in synthesis
source_file = "/home/ryan/openROADTests/LVS/LayoutExtraction.spice"
destination_file = "/home/ryan/openROADTests/LVS/LayoutExtraction_Without_Decap.spice"

sf = open(source_file, "r")
df = open(destination_file, "w")

sf_lines = sf.readlines()
df_lines = []
CDC = False
Plus_Streak = False

for l in sf_lines:

  if l.split(" ")[0] == ".subckt" and l.split(" ")[1] == "CDC":
    l = ""
    CDC = True
    Plus_Streak = True

  elif l.split(" ")[0] == "+" and Plus_Streak:
  	l = ""
  elif l.split(" ")[0] != "+" and Plus_Streak:
    Plus_Streak = False

  elif l == ".ends\n" and CDC:
  	l = ""

  if "sky130_fd_sc_hd__decap_4" not in l.split(" ")[len(l.split(" ")) - 1]:
    df_lines.append(l)

df_lines[len(df_lines) - 1] = df_lines[len(df_lines) - 1].replace('\n', '')

df.writelines(df_lines)

sf.close()
df.close()
