# Read libraries and design
read_liberty LIB/Skywater.lib

read_lef LEF/sky130_fd_sc_hd.tlef
read_lef LEF/sky130_fd_sc_hd_merged.lef
read_lef LEF/transmission_gate.lef

read_db "Floorplanned.db"

source TCL/make_tracks.tcl
source TCL/setRC.tcl

global_placement -skip_io -density 0.6 -pad_left 1 -pad_right 1

place_pins -hor_layers "met3" \
	   -ver_layers "met2" \
	   
source TCL/fastroute.tcl

global_placement -skip_io -density 0.6 -pad_left 1 -pad_right 1

set_placement_padding -global -left 0 -right 0

detailed_placement
optimize_mirroring

write_def output.def
write_db Placed.db

exit
