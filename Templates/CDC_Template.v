`include "Physical_Gates.v"
`include "Inverter_Chains.v"
`include "Chain_Driver.v"
`include "Delay_Comp.v"
`include "Counter.v"
`include "Clock_Generator.v"

module CDC(input Reset,
           output [15:0] D_SUB1,
           output [15:0] D_SUB2,
           output [19:0] D_MAIN,
           output Conversion_Finished);
    wire Next_Edge_LowV, Next_Edge_LowV_b, Next_Edge_HighV;
    wire Falling_Low, Falling_Cap, Falling_Output_Enable, Falling_Done, Falling_Y;
    wire Falling_Cap1, Falling_Cap2, Falling_Cap3;
    wire Rising_Low, Rising_Cap, Rising_Output_Enable, Rising_Done, Rising_Y;
    wire Finish_Low, Finish_Delay, Finish, ResetB;

    //Inverter chains
    Normal_Inverter_Chain LOW_CHAIN(.I(Next_Edge_HighV), .O(Falling_Low));
    Cap_Inverter_Chain CAP_CHAIN(.I(Next_Edge_HighV), .O(Falling_Cap));    
    custom_normalInverter INV_RISING_LOW(.I(Falling_Low), .O(Rising_Low));
    custom_normalInverter INV_RISING_CAP(.I(Falling_Cap), .O(Rising_Cap));
    Finish_Inverter_Chain FINISH_CHAIN(.I(Rising_Low), .Ob(Finish_Delay), .O(Finish_Low));

    //Falling edge comparison stuff
    delay_comp FALLING_COMP(.D_Plus(Falling_Cap), .D_Minus(Falling_Low), .Output_Enable(Falling_Output_Enable), .Done(Falling_Done), .Y(Falling_Y));
    Counter_Sub FALLING_COUNTER(.CLK(Falling_Y), .RST(Reset), .O(D_SUB2));

    //Rising edge comparison stuff
    delay_comp RISING_COMP(.D_Plus(Rising_Cap), .D_Minus(Rising_Low), .Output_Enable(Rising_Output_Enable), .Done(Rising_Done), .Y(Rising_Y));
    Counter_Sub RISING_COUNTER(.CLK(Rising_Y), .RST(Reset), .O(D_SUB1));

    //Finish comparator
    delay_comp FINISH_COMP(.D_Plus(Rising_Cap), .D_Minus(Finish_Low), .Output_Enable(Rising_Output_Enable), .Y(Finish));

    //Next edge generator and counter
    clock_generator CLOCK_GEN(.Done_Rising(Rising_Done), .Done_Falling(Falling_Done), .Finish_Delay(Finish_Delay),
                              .Reset(Reset), .Finish(Finish), .OE_Rising(Rising_Output_Enable), .OE_Falling(Falling_Output_Enable),
                              .Next_Edge(Next_Edge_LowV), .Conv_Finish(Conversion_Finished));
    Counter_Main FULL_COUNTER(.CLK(Next_Edge_LowV), .RST(Reset), .O(D_MAIN));

    //Level converter and transmission gates
    chain_driver CDC_CHAIN_DRIVER(.Next_Edge_LowV(Next_Edge_LowV), .Next_Edge_HighV(Next_Edge_HighV));

	sky130_fd_sc_hd__inv_16 HIGH_RESET_INV(.A(Reset), .Y(ResetB));
endmodule
