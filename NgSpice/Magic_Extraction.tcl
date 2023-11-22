# Read the GDS file
gds read "/home/ryan/openROADTests/Final.gds"

# Load the CDC
load CDC

# Extract the CDC to an .ext file
extract

# Configure the ext2spice command for PEX
ext2spice LVS
ext2spice rthresh 0
ext2spice cthresh 0

# Extract the CDC to a SPICE file
ext2spice -o /home/ryan/openROADTests/NgSpice/CDC.spice

# Terminate
exit
