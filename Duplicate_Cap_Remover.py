source_file = open('duplicate_taps.def', 'r')
destination_file = open('fixed_taps.def', 'w')

sf_lines = source_file.readlines()
df_lines = []

for line in sf_lines:
    print(line)
    exit()
    df_lines.append(line)

destination_file.writelines(df_lines)

source_file.close()
destination_file.close()
