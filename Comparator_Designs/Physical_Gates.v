`ifndef PHYSICAL_GATE_GUARD
`define PHYSICAL_GATE_GUARD

module custom_capInverter(input I,
                          output O);
    sky130_fd_sc_hd__inv_1 cell_INV(.A(I), .Y(O));
endmodule

module custom_normalInverter(input I,
                             output O);
    sky130_fd_sc_hd__inv_1 cell_INV(.A(I), .Y(O));
endmodule

module custom_NAND(input A,
                   input B,
                   output O);
    sky130_fd_sc_hd__nand2_1 cell_NAND2(.A(A), .B(B), .Y(O));
endmodule          

module custom_NAND3(input A,
                    input B,
                    input C,
                    output O);
    sky130_fd_sc_hd__nand3_1 cell_NAND3(.A(A), .B(B), .C(C), .Y(O));
endmodule 

module custom_NOR(input A,
                  input B,
                  output O);
    sky130_fd_sc_hd__nor2_1 cell_NOR(.A(A), .B(B), .Y(O));
endmodule          

module custom_XOR(input A,
                  input B,
                  output O);
    sky130_fd_sc_hd__xor2_1 cell_XOR(.A(A), .B(B), .Y(O));
endmodule

module custom_SR_b(input Sb,
                   input Rb,
                   output Q,
                   output Qb);
    sky130_fd_sc_hd__nand2_8 NANDQ (.A(Sb), .B(Qb), .Y(Q));
    sky130_fd_sc_hd__nand2_8 NANDQb (.A(Rb), .B(Q), .Y(Qb));
endmodule

module custom_SR(input S,
                 input R,
                 output Q,
                 output Qb);

    wire Sb, Rb;

    custom_normalInverter INVS (.I(S), .O(Sb));
    custom_normalInverter INVR (.I(R), .O(Rb));

    custom_SR_b SRlatch(.Sb(Sb), .Rb(Rb), .Q(Q), .Qb(Qb));
endmodule

module custom_DFF(input CLK,
                  input D,
                  input RSTb,
                  output Q,
                  output Qb);
    wire TIED_HIGH;
   	sky130_fd_sc_hd__conb_1 cell_TIHI(.HI(TIED_HIGH));
    sky130_fd_sc_hd__dfbbn_1 cell_DFF(.CLK_N(CLK), .D(D), .RESET_B(RSTb), .SET_B(TIED_HIGH), .Q(Q), .Q_N(Qb));
endmodule

(* blackbox *)
module SLC(input IN,
           input INb,
           input VOUT);
endmodule

(* blackbox *)
module transmission_gate(input G,
                         input GN,
                         output O);
endmodule
`endif
