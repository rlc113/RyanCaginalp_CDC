# Read libraries and design
read_liberty LIB/Skywater.lib

read_lef LEF/sky130_fd_sc_hd.tlef
read_lef LEF/sky130_fd_sc_hd_merged.lef
read_lef LEF/transmission_gate.lef

read_db "Placed.db"

source TCL/make_tracks.tcl
source TCL/setRC.tcl

filler_placement "sky130_fd_sc_hd__fill_1 sky130_fd_sc_hd__fill_2 sky130_fd_sc_hd__fill_4 sky130_fd_sc_hd__fill_8"
check_placement

write_def output.def
write_db Filled.db

exit
