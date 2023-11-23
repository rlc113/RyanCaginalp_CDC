# Read the GDS file
gds read "/content/RyanCaginalp_CDC/Final.gds"

# Load the CDC
load CDC

# Extract the CDC to an .ext file
extract

# Configure the ext2spice command for LVS (no PEX)
ext2spice LVS

# Extract the CDC to a SPICE file
ext2spice CDC

# Terminate
exit
