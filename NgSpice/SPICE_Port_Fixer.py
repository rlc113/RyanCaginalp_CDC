#Notation is misleading - both have PEX done on them, this file just fixes the port order
source_file = "/content/RyanCaginalp_CDC/NgSpice/CDC.spice"
destination_file = "/content/RyanCaginalp_CDC/NgSpice/CDC_PEX.spice"

sf = open(source_file, "r")
df = open(destination_file, "w")

sf_lines = sf.readlines()
df_lines = []
CDC = False
Plus_Streak = False

for l in sf_lines:

  if l.split(" ")[0] == ".subckt" and l.split(" ")[1] == "CDC":
    l = ".subckt CDC Reset Conversion_Finished V_GND V_LOW V_HIGH V_SENSE D_SUB1[0] D_SUB1[1] D_SUB1[2] D_SUB1[3] D_SUB1[4] D_SUB1[5] D_SUB1[6] D_SUB1[7] D_SUB1[8] D_SUB1[9] D_SUB1[10] D_SUB1[11] D_SUB1[12] D_SUB1[13] D_SUB1[14] D_SUB1[15] D_SUB2[0] D_SUB2[1] D_SUB2[2] D_SUB2[3] D_SUB2[4] D_SUB2[5] D_SUB2[6] D_SUB2[7] D_SUB2[8] D_SUB2[9] D_SUB2[10] D_SUB2[11] D_SUB2[12] D_SUB2[13] D_SUB2[14] D_SUB2[15] D_MAIN[0] D_MAIN[1] D_MAIN[2] D_MAIN[3] D_MAIN[4] D_MAIN[5] D_MAIN[6] D_MAIN[7] D_MAIN[8] D_MAIN[9] D_MAIN[10] D_MAIN[11] D_MAIN[12] D_MAIN[13] D_MAIN[14] D_MAIN[15] D_MAIN[16] D_MAIN[17] D_MAIN[18] D_MAIN[19]\n"
    CDC = True
    Plus_Streak = True

  elif l.split(" ")[0] == "+" and Plus_Streak:
  	l = ""
  elif l.split(" ")[0] != "+" and Plus_Streak:
    Plus_Streak = False

  if (l != ""): df_lines.append(l)

df_lines[len(df_lines) - 1] = df_lines[len(df_lines) - 1].replace('\n', '')

df.writelines(df_lines)

sf.close()
df.close()
