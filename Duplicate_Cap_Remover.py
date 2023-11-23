source_file = open('duplicate_caps.def', 'r')
destination_file = open('fixed_caps.def', 'w')

sf_lines = source_file.readlines()
df_lines = []

unique_coords = {}

for line in sf_lines:
    if "PHY_EDGE" in line:
        C = str((line.split(" ")[len(line.split(" ")) - 5], line.split(" ")[len(line.split(" ")) - 4]))
        if C not in unique_coords.keys():
            unique_coords[C] = 1
            df_lines.append(line)
    else: df_lines.append(line)
    
destination_file.writelines(df_lines)

source_file.close()
destination_file.close()
