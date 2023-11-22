# First configure a new custom design
python3 Custom_CDC_Generator.py 16 1 16

# Next run the flow to create a GDSII file
./Fabrication.sh

# Then, extract the SPICE file from the design using MAGIC
magic -rcfile /home/ryan/MagicTests/SKY130/git_open_pdks/sky130/sky130A/libs.tech/magic/sky130A.magicrc -noconsole -dnull NgSpice/Magic_Extraction.tcl

# Fix the port order so our simulation will work properly
python3 NgSpice/SPICE_Port_Fixer.py

# Configure our simulation
python3 NgSpice/Simulation_Configuration.py 450 400 60 80

# Run a basic simulation
ngspice -b NgSpice/CDC_PEX_Test.cir -o NgSpice/Test.log

# Use Python to figure out what the outputs are
python3 NgSpice/Data_Reader.py
