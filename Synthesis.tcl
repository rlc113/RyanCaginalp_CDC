yosys -import
read_liberty -lib HW_CDC_Verilog/Skywater.lib
read_verilog -defer HW_CDC_Verilog/CDC.v

hierarchy -top CDC
flatten

hilomap -hicell sky130_fd_sc_hd__conb_1 HI -locell sky130_fd_sc_hd__conb_1 LO

write_verilog -noattr -noexpr "Synthesized.v"

write_spice "SynthesizedExtraction.spice"
