# Read libraries and design
read_liberty LIB/Skywater.lib

read_lef LEF/sky130_fd_sc_hd.tlef
read_lef LEF/sky130_fd_sc_hd_merged.lef
read_lef LEF/transmission_gate.lef

read_verilog "Synthesized.v"
link_design CDC

source TCL/setRC.tcl

# Create basic floorplan
set V_HIGH_BLX 60
set V_HIGH_BLY 60

set V_HIGH_WIDTH 19
set V_HIGH_HEIGHT 21

set V_HIGH_TRX [expr $V_HIGH_BLX + $V_HIGH_WIDTH]
set V_HIGH_TRY [expr $V_HIGH_BLY + $V_HIGH_HEIGHT]

set V_SENSE_BLX 60
set V_SENSE_BLY 140

set V_SENSE_WIDTH 45
set V_SENSE_HEIGHT 7

set V_SENSE_TRX [expr $V_SENSE_BLX + $V_SENSE_WIDTH]
set V_SENSE_TRY [expr $V_SENSE_BLY + $V_SENSE_HEIGHT]

set V_HIGH_DOMAIN_AREA "$V_HIGH_BLX $V_HIGH_BLY $V_HIGH_TRX $V_HIGH_TRY"
set V_SENSE_DOMAIN_AREA "$V_SENSE_BLX $V_SENSE_BLY $V_SENSE_TRX $V_SENSE_TRY"

create_voltage_domain V_HIGH_DOMAIN -area $V_HIGH_DOMAIN_AREA
create_voltage_domain V_SENSE_DOMAIN -area $V_SENSE_DOMAIN_AREA

initialize_floorplan -die_area "0 0 213 190" -core_area "30 30 183 160" -site unithd
source TCL/read_domain_instances.tcl
read_domain_instances V_HIGH_DOMAIN Other/V_HIGH_INSTANCES.txt
read_domain_instances V_SENSE_DOMAIN Other/V_SENSE_INSTANCES.txt

source TCL/make_tracks.tcl

# Pin Initialization
place_pins -hor_layers "met3" \
	   -ver_layers "met2" \
	   -random

# Tap cell stuff
tapcell \
	-endcap_cpp "2" \
	-distance 14 \
	-tapcell_master "sky130_fd_sc_hd__tapvpwrvgnd_1" \
	-endcap_master "sky130_fd_sc_hd__decap_4"

write_def duplicate_caps.def
exit