sed /OR_DEFAULT/d LEF/sky130_fd_sc_hd.tlef > Klayout_Files/klayout_tech.lef
sed 's,<lef-files>.*</lef-files>,<lef-files>Klayout_Files/klayout_tech.lef</lef-files> <lef-files>LEF/sky130_fd_sc_hd_merged.lef</lef-files> <lef-files>LEF/transmission_gate.lef</lef-files>,g' LYT/sky130hd.lyt > Klayout_Files/klayout.lyt

klayout -zz -rd design_name="CDC" \
		-rd in_def="Routed.def" \
		-rd in_files="GDS/sky130_fd_sc_hd.gds GDS/transmission_gate.gds" \
		-rd config_file="JSON/fill.json" \
		-rd seal_file="" \
		-rd out_file="Final.gds" \
		-rd tech_file="Klayout_Files/klayout.lyt" \
		-rd layer_map= \
		-r PYTHON/def2stream.py
