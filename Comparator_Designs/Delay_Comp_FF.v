`include "Physical_Gates.v"

`ifndef DELAY_GUARD
`define DELAY_GUARD

module delay_comp(input D_Plus,
                  input D_Minus,
                  input Output_Enable,
                  output Done,
                  output Y);

    wire Db_Plus, Db_Minus, Q, Qb, Q_b, Qb_b;

    custom_normalInverter INV_DP (.I(D_Plus), .O(Db_Plus));
    custom_normalInverter INV_DM (.I(D_Minus), .O(Db_Minus));

    custom_SR_b SR_MEM(.Sb(Db_Plus), .Rb(Db_Minus), .Q(Q), .Qb(Qb));

    custom_normalInverter INV_Q (.I(Q), .O(Q_b));
    custom_normalInverter INV_Qb (.I(Qb), .O(Qb_b));

    custom_NAND NAND2_COMP (.A(D_Plus), .B(D_Minus), .O(Done));
    //custom_XOR XOR_COMP (.A(Q_b), .B(Qb_b), .O(Done)); (Doesn't work bc can't start properly)
    custom_NAND3 NAND3_COMP (.A(Qb_b), .B(Db_Plus), .C(Output_Enable), .O(Y));
endmodule

`endif