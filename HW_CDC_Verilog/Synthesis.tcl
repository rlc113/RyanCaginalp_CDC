read_liberty -lib Skywater.lib
read_verilog -defer Physical_Gates.v

hierarchy -top CDC
flatten

hilomap -hicell sky130_fd_sc_hd__conb HI -lowcell sky130_fd_sc_hd__conb LO

write_verilog -noattr -noexpr "Synthesized.v"
