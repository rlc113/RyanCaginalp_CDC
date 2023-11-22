`include "Physical_Gates.v"

`ifndef CHAIN_DRIVER_GUARD
`define CHAIN_DRIVER_GUARD

module chain_driver(input Next_Edge_LowV, output Next_Edge_HighV);

    wire chain_driver2;
    wire chain_driver4;
    wire chain_driver8;
    wire chain_driver16;
    wire chain_driver32;

    custom_Inverter2 chain_driver_inv2(.I(Next_Edge_LowV), .O(chain_driver2));
    custom_Inverter4 chain_driver_inv4(.I(chain_driver2), .O(chain_driver4));
    custom_Inverter8 chain_driver_inv8(.I(chain_driver4), .O(chain_driver8));
    custom_Inverter16 chain_driver_inv16(.I(chain_driver8), .O(chain_driver16));
    custom_Inverter16 chain_driver_inv32_1(.I(chain_driver16), .O(chain_driver32));
    custom_Inverter16 chain_driver_inv32_2(.I(chain_driver16), .O(chain_driver32));
    custom_Inverter16 chain_driver_last_inv_1(.I(chain_driver32), .O(Next_Edge_HighV));
    custom_Inverter16 chain_driver_last_inv_2(.I(chain_driver32), .O(Next_Edge_HighV));

endmodule

`endif