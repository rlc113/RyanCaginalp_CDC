#Notation is misleading - both have PEX done on them, this file just fixes the port order
source_file = "/home/ryan/openROADTests/NgSpice/CDC.spice"
destination_file = "/home/ryan/openROADTests/NgSpice/CDC_PEX.spice"

sf = open(source_file, "r")
df = open(destination_file, "w")

sf_lines = sf.readlines()
df_lines = []
CDC = False
Plus_Streak = False

for l in sf_lines:

  if l.split(" ")[0] == ".subckt" and l.split(" ")[1] == "CDC":
    l = ".subckt CDC Reset CLOCK_GEN.SR_Op.Q V_GND V_LOW V_HIGH V_SENSE RISING_COUNTER.COUNT_SUB_DFF0.Q RISING_COUNTER.COUNT_SUB_DFF1.Q RISING_COUNTER.COUNT_SUB_DFF2.Q RISING_COUNTER.COUNT_SUB_DFF3.Q RISING_COUNTER.COUNT_SUB_DFF4.Q RISING_COUNTER.COUNT_SUB_DFF5.Q RISING_COUNTER.COUNT_SUB_DFF6.Q RISING_COUNTER.COUNT_SUB_DFF7.Q RISING_COUNTER.COUNT_SUB_DFF8.Q RISING_COUNTER.COUNT_SUB_DFF9.Q RISING_COUNTER.COUNT_SUB_DFF10.Q RISING_COUNTER.COUNT_SUB_DFF11.Q RISING_COUNTER.COUNT_SUB_DFF12.Q RISING_COUNTER.COUNT_SUB_DFF13.Q RISING_COUNTER.COUNT_SUB_DFF14.Q RISING_COUNTER.COUNT_SUB_DFF15.Q FALLING_COUNTER.COUNT_SUB_DFF0.Q FALLING_COUNTER.COUNT_SUB_DFF1.Q FALLING_COUNTER.COUNT_SUB_DFF2.Q FALLING_COUNTER.COUNT_SUB_DFF3.Q FALLING_COUNTER.COUNT_SUB_DFF4.Q FALLING_COUNTER.COUNT_SUB_DFF5.Q FALLING_COUNTER.COUNT_SUB_DFF6.Q FALLING_COUNTER.COUNT_SUB_DFF7.Q FALLING_COUNTER.COUNT_SUB_DFF8.Q FALLING_COUNTER.COUNT_SUB_DFF9.Q FALLING_COUNTER.COUNT_SUB_DFF10.Q FALLING_COUNTER.COUNT_SUB_DFF11.Q FALLING_COUNTER.COUNT_SUB_DFF12.Q FALLING_COUNTER.COUNT_SUB_DFF13.Q FALLING_COUNTER.COUNT_SUB_DFF14.Q FALLING_COUNTER.COUNT_SUB_DFF15.Q FULL_COUNTER.COUNT_SUB_DFF0.Q FULL_COUNTER.COUNT_SUB_DFF1.Q FULL_COUNTER.COUNT_SUB_DFF2.Q FULL_COUNTER.COUNT_SUB_DFF3.Q FULL_COUNTER.COUNT_SUB_DFF4.Q FULL_COUNTER.COUNT_SUB_DFF5.Q FULL_COUNTER.COUNT_SUB_DFF6.Q FULL_COUNTER.COUNT_SUB_DFF7.Q FULL_COUNTER.COUNT_SUB_DFF8.Q FULL_COUNTER.COUNT_SUB_DFF9.Q FULL_COUNTER.COUNT_SUB_DFF10.Q FULL_COUNTER.COUNT_SUB_DFF11.Q FULL_COUNTER.COUNT_SUB_DFF12.Q FULL_COUNTER.COUNT_SUB_DFF13.Q FULL_COUNTER.COUNT_SUB_DFF14.Q FULL_COUNTER.COUNT_SUB_DFF15.Q FULL_COUNTER.COUNT_SUB_DFF16.Q FULL_COUNTER.COUNT_SUB_DFF17.Q FULL_COUNTER.COUNT_SUB_DFF18.Q FULL_COUNTER.COUNT_SUB_DFF19.Q\n"
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