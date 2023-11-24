# Read libraries and design
read_liberty LIB/Skywater.lib

read_lef LEF/sky130_fd_sc_hd.tlef
read_lef LEF/sky130_fd_sc_hd_merged.lef
read_lef LEF/transmission_gate.lef

read_db "Filled.db"

source TCL/make_tracks.tcl
source TCL/setRC.tcl

source TCL/create_routable_power_net.tcl
source TCL/create_custom_connections.tcl

create_routable_power_net V_SENSE
create_custom_connections Other/V_SENSE_Routes.txt

source TCL/fastroute.tcl

global_route -guide_file route.guide -congestion_iterations 100

set_thread_count 8

detailed_route -output_drc post_route_check.rpt \
			   -output_maze maze.log \
			   -save_guide_updates \
			   -bottom_routing_layer met1 \
			   -top_routing_layer met5

write_def Routed.def
write_db Routed.db

exit
