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

set V_HIGH_WIDTH 30
set V_HIGH_HEIGHT 21

set V_HIGH_TRX [expr $V_HIGH_BLX + $V_HIGH_WIDTH]
set V_HIGH_TRY [expr $V_HIGH_BLY + $V_HIGH_HEIGHT]

set V_SENSE_BLX 60
set V_SENSE_BLY 140

set V_SENSE_WIDTH 50
set V_SENSE_HEIGHT 5

set V_SENSE_TRX [expr $V_SENSE_BLX + $V_SENSE_WIDTH]
set V_SENSE_TRY [expr $V_SENSE_BLY + $V_SENSE_HEIGHT]

set V_HIGH_DOMAIN_AREA "$V_HIGH_BLX $V_HIGH_BLY $V_HIGH_TRX $V_HIGH_TRY"
set V_SENSE_DOMAIN_AREA "$V_SENSE_BLX $V_SENSE_BLY $V_SENSE_TRX $V_SENSE_TRY"

create_voltage_domain V_HIGH_DOMAIN -area $V_HIGH_DOMAIN_AREA
create_voltage_domain V_SENSE_DOMAIN -area $V_SENSE_DOMAIN_AREA

initialize_floorplan -die_area "0 0 200 210" -core_area "30 30 170 180" -site unithd

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

# Power network creation
set block [ord::get_db_block]
set all_insts [$block getInsts]
set caps_sense {}
set caps_high {}
set caps_core {}
foreach inst $all_insts {
  if {[[$inst getMaster] getName] eq "sky130_fd_sc_hd__tapvpwrvgnd_1" || \
      [[$inst getMaster] getName] eq "sky130_fd_sc_hd__decap_4"} {
    set box [$inst getBBox]

    if { [$box xMin] >= $V_SENSE_BLX && [$box xMax] <= $V_SENSE_TRX \
      && [$box yMin] >= $V_SENSE_BLY && [$box yMax] <= $V_SENSE_TRY} {
		lappend caps_sense $inst
	} elseif { [$box xMin] >= $V_HIGH_BLX && [$box xMax] <= $V_HIGH_TRX \
      && [$box yMin] >= $V_HIGH_BLY && [$box yMax] <= $V_HIGH_TRY} {
		lappend caps_high $inst
	} else {
		lappend caps_core $inst
	}
  }
}

add_global_connection -net V_LOW -inst_pattern {.*} -pin_pattern {VPWR|VPB} -power
add_global_connection -net V_SENSE -inst_pattern {CAP_CHAIN.*} -pin_pattern {VPWR|VPB} -power
add_global_connection -net V_HIGH -inst_pattern {HIGH_RESET_INV} -pin_pattern {VPWR|VPB} -power
add_global_connection -net V_GND -inst_pattern {.*} -pin_pattern {VGND|VNB} -ground

foreach inst $caps_sense {
  add_global_connection -net V_SENSE -inst_pattern [$inst getName] -pin_pattern {VPWR|VPB} -power
}
foreach inst $caps_high {
  add_global_connection -net V_HIGH -inst_pattern [$inst getName] -pin_pattern {VPWR|VPB} -power
}
foreach inst $caps_core {
  add_global_connection -net V_LOW -inst_pattern [$inst getName] -pin_pattern {VPWR|VPB} -power
}

global_connect

set_voltage_domain -name CORE -power V_LOW -ground V_GND
set_voltage_domain -region V_HIGH_DOMAIN -power V_HIGH -ground V_GND
set_voltage_domain -region V_SENSE_DOMAIN -power V_SENSE -ground V_GND

# Define V_LOW power grid
define_pdn_grid -name stdcell -pins met5 -starts_with POWER -voltage_domains CORE

# Create V_LOW standard cell rails
add_pdn_stripe -grid stdcell -layer met1 -width 0.49 -pitch 6.66 -offset 0 -extend_to_core_ring -followpins

# Create V_LOW power ring
add_pdn_ring -grid stdcell -layer {met4 met5} -widths {5.0 5.0} -spacings {2.0 2.0} -core_offsets {2.0 2.0}

# Connect all grounds horizontally
add_pdn_stripe -grid stdcell -layer met5 -width 1.6 -pitch 10 -extend_to_core_ring -starts_with GROUND -nets V_GND

# Connect V_LOW ring together and V_LOW ring to standard cells
add_pdn_connect -grid stdcell -layers {met4 met5}
add_pdn_connect -grid stdcell -layers {met1 met4}

# Define V_HIGH power grid
define_pdn_grid -name V_HIGH_GRID -pins met3 -starts_with POWER -voltage_domains V_HIGH_DOMAIN

# Create V_HIGH power ring
add_pdn_ring -grid V_HIGH_GRID -layer {met4 met3} -widths {5.0 5.0} -spacings {2.0 2.0} -core_offsets {2.0 2.0}

# Create V_HIGH standard cell rails
add_pdn_stripe -grid V_HIGH_GRID -layer met1 -width 0.49 -pitch 6.66 -offset 0 -extend_to_core_ring -followpins

# Connect V_HIGH standard cell rails to power ring
add_pdn_stripe -grid V_HIGH_GRID -layer met4 -width 1.6 -offset 0 -pitch 10 -extend_to_core_ring -starts_with GROUND

# Connect standard cells to power ring, ring together, and ring grounds together for V_LOW and V_HIGH
add_pdn_connect -grid V_HIGH_GRID -layers {met1 met4}
add_pdn_connect -grid V_HIGH_GRID -layers {met3 met4}
add_pdn_connect -grid V_HIGH_GRID -layers {met4 met5}

# Define V_SENSE power grid
define_pdn_grid -name V_SENSE_GRID -pins met3 -starts_with GROUND -voltage_domains V_SENSE_DOMAIN

# Create V_SENSE power ring
add_pdn_ring -grid V_SENSE_GRID -layer {met4 met3} -widths {5.0 5.0} -spacings {2.0 2.0} -core_offsets {2.0 2.0}

# Create V_SENSE standard cell rails
add_pdn_stripe -grid V_SENSE_GRID -layer met1 -width 0.49 -pitch 6.66 -offset 0 -extend_to_core_ring -followpins

# Connect V_SENSE standard cell rails to power ring
add_pdn_stripe -grid V_SENSE_GRID -layer met4 -width 1.6 -offset 0 -pitch 10 -extend_to_core_ring -starts_with GROUND

# Connect standard cells to power ring, ring together, and ring grounds together for V_LOW and V_SENSE
add_pdn_connect -grid V_SENSE_GRID -layers {met1 met4}
add_pdn_connect -grid V_SENSE_GRID -layers {met3 met4}
add_pdn_connect -grid V_SENSE_GRID -layers {met4 met5}

pdngen

write_def output.def
write_db Floorplanned.db

exit
