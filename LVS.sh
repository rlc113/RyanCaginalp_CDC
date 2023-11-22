# First format the synthesized SPICE file so that it has power information
python3 SPICE_Power_Filler.py

# Also eliminate DC sources meant for miscellanous connections (segfaults if we don't do this)
python3 LVS/SPICE_DC_Remover.py

# Use Magic to extract a SPICE file from the GDS
magic -rcfile /home/ryan/MagicTests/SKY130/git_open_pdks/sky130/sky130A/libs.tech/magic/sky130A.magicrc -noconsole -dnull LVS/Magic_Extraction.tcl

# Copy the CDC file into the LVS folder
mv CDC.spice LVS/LayoutExtraction.spice

# The extracted file includes filler cells that must be eliminated
python3 LVS/SPICE_Decap_Remover.py

# Now do LVS
netgen -noconsole source LVS/Netgen_LVS.tcl
