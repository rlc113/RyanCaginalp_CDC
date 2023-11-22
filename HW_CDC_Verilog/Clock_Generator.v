`include "Physical_Gates.v"

`ifndef CLOCKGEN_GUARD
`define CLOCKGEN_GUARD

module clock_generator(input Done_Rising,
                       input Done_Falling,
                       input Finish_Delay,
                       input Reset,
                       input Finish,
                       output OE_Rising,
                       output OE_Falling,
                       output Next_Edge,
                       output Conv_Finish);

    wire FinishB_Delay, Set_OE, Reset_OE, ResetB, Sense, CLKb;

    custom_NAND NAND_DR(.A(Done_Rising), .B(Finish_Delay), .O(Reset_OE));
    custom_normalInverter INV_F (.I(Finish_Delay), .O(FinishB_Delay));
    custom_NAND NAND_DF(.A(Done_Falling), .B(FinishB_Delay), .O(Set_OE));

    custom_SR_b SR_OE(.Sb(Set_OE), .Rb(Reset_OE), .Q(OE_Falling));

    custom_normalInverter INV_OE (.I(OE_Falling), .O(OE_Rising));

    custom_normalInverter INV_R (.I(Reset), .O(ResetB));
    custom_SR_b SR_Op(.Sb(Finish), .Rb(ResetB), .Q(Conv_Finish));

    custom_NOR NOR_CLK(.A(Reset), .B(Conv_Finish), .O(Sense));

    custom_NAND NAND_CLK(.A(OE_Falling), .B(Sense), .O(CLKb));
    custom_normalInverter NOT_CLK(.I(CLKb), .O(Next_Edge));
endmodule

`endif