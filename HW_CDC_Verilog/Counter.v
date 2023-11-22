`include "Physical_Gates.v"

`ifndef COUNTER_GUARD
`define COUNTER_GUARD

module Counter_Sub(CLK, RST, O);
    input CLK, RST;
    output[15:0] O;

    wire [15:0] D;

    wire RSTb;

    sky130_fd_sc_hd__inv_16 RST_INV(.A(RST), .Y(RSTb));


    custom_normalInverter COUNT_SUB_INV0(.I(O[0]), .O(D[0]));
    custom_normalInverter COUNT_SUB_INV1(.I(O[1]), .O(D[1]));
    custom_normalInverter COUNT_SUB_INV2(.I(O[2]), .O(D[2]));
    custom_normalInverter COUNT_SUB_INV3(.I(O[3]), .O(D[3]));
    custom_normalInverter COUNT_SUB_INV4(.I(O[4]), .O(D[4]));
    custom_normalInverter COUNT_SUB_INV5(.I(O[5]), .O(D[5]));
    custom_normalInverter COUNT_SUB_INV6(.I(O[6]), .O(D[6]));
    custom_normalInverter COUNT_SUB_INV7(.I(O[7]), .O(D[7]));
    custom_normalInverter COUNT_SUB_INV8(.I(O[8]), .O(D[8]));
    custom_normalInverter COUNT_SUB_INV9(.I(O[9]), .O(D[9]));
    custom_normalInverter COUNT_SUB_INV10(.I(O[10]), .O(D[10]));
    custom_normalInverter COUNT_SUB_INV11(.I(O[11]), .O(D[11]));
    custom_normalInverter COUNT_SUB_INV12(.I(O[12]), .O(D[12]));
    custom_normalInverter COUNT_SUB_INV13(.I(O[13]), .O(D[13]));
    custom_normalInverter COUNT_SUB_INV14(.I(O[14]), .O(D[14]));
    custom_normalInverter COUNT_SUB_INV15(.I(O[15]), .O(D[15]));

    custom_DFF COUNT_SUB_DFF0(.CLK(CLK), .D(D[0]), .RSTb(RSTb), .Q(O[0]));
    custom_DFF COUNT_SUB_DFF1(.CLK(O[0]), .D(D[1]), .RSTb(RSTb), .Q(O[1]));
    custom_DFF COUNT_SUB_DFF2(.CLK(O[1]), .D(D[2]), .RSTb(RSTb), .Q(O[2]));
    custom_DFF COUNT_SUB_DFF3(.CLK(O[2]), .D(D[3]), .RSTb(RSTb), .Q(O[3]));
    custom_DFF COUNT_SUB_DFF4(.CLK(O[3]), .D(D[4]), .RSTb(RSTb), .Q(O[4]));
    custom_DFF COUNT_SUB_DFF5(.CLK(O[4]), .D(D[5]), .RSTb(RSTb), .Q(O[5]));
    custom_DFF COUNT_SUB_DFF6(.CLK(O[5]), .D(D[6]), .RSTb(RSTb), .Q(O[6]));
    custom_DFF COUNT_SUB_DFF7(.CLK(O[6]), .D(D[7]), .RSTb(RSTb), .Q(O[7]));
    custom_DFF COUNT_SUB_DFF8(.CLK(O[7]), .D(D[8]), .RSTb(RSTb), .Q(O[8]));
    custom_DFF COUNT_SUB_DFF9(.CLK(O[8]), .D(D[9]), .RSTb(RSTb), .Q(O[9]));
    custom_DFF COUNT_SUB_DFF10(.CLK(O[9]), .D(D[10]), .RSTb(RSTb), .Q(O[10]));
    custom_DFF COUNT_SUB_DFF11(.CLK(O[10]), .D(D[11]), .RSTb(RSTb), .Q(O[11]));
    custom_DFF COUNT_SUB_DFF12(.CLK(O[11]), .D(D[12]), .RSTb(RSTb), .Q(O[12]));
    custom_DFF COUNT_SUB_DFF13(.CLK(O[12]), .D(D[13]), .RSTb(RSTb), .Q(O[13]));
    custom_DFF COUNT_SUB_DFF14(.CLK(O[13]), .D(D[14]), .RSTb(RSTb), .Q(O[14]));
    custom_DFF COUNT_SUB_DFF15(.CLK(O[14]), .D(D[15]), .RSTb(RSTb), .Q(O[15]));
endmodule

module Counter_Main(CLK, RST, O);
    input CLK, RST;
    output[19:0] O;

    wire [19:0] D;

    wire RSTb;

    sky130_fd_sc_hd__inv_16 RST_INV(.A(RST), .Y(RSTb));


    custom_normalInverter COUNT_SUB_INV0(.I(O[0]), .O(D[0]));
    custom_normalInverter COUNT_SUB_INV1(.I(O[1]), .O(D[1]));
    custom_normalInverter COUNT_SUB_INV2(.I(O[2]), .O(D[2]));
    custom_normalInverter COUNT_SUB_INV3(.I(O[3]), .O(D[3]));
    custom_normalInverter COUNT_SUB_INV4(.I(O[4]), .O(D[4]));
    custom_normalInverter COUNT_SUB_INV5(.I(O[5]), .O(D[5]));
    custom_normalInverter COUNT_SUB_INV6(.I(O[6]), .O(D[6]));
    custom_normalInverter COUNT_SUB_INV7(.I(O[7]), .O(D[7]));
    custom_normalInverter COUNT_SUB_INV8(.I(O[8]), .O(D[8]));
    custom_normalInverter COUNT_SUB_INV9(.I(O[9]), .O(D[9]));
    custom_normalInverter COUNT_SUB_INV10(.I(O[10]), .O(D[10]));
    custom_normalInverter COUNT_SUB_INV11(.I(O[11]), .O(D[11]));
    custom_normalInverter COUNT_SUB_INV12(.I(O[12]), .O(D[12]));
    custom_normalInverter COUNT_SUB_INV13(.I(O[13]), .O(D[13]));
    custom_normalInverter COUNT_SUB_INV14(.I(O[14]), .O(D[14]));
    custom_normalInverter COUNT_SUB_INV15(.I(O[15]), .O(D[15]));
    custom_normalInverter COUNT_SUB_INV16(.I(O[16]), .O(D[16]));
    custom_normalInverter COUNT_SUB_INV17(.I(O[17]), .O(D[17]));
    custom_normalInverter COUNT_SUB_INV18(.I(O[18]), .O(D[18]));
    custom_normalInverter COUNT_SUB_INV19(.I(O[19]), .O(D[19]));

    custom_DFF COUNT_SUB_DFF0(.CLK(CLK), .D(D[0]), .RSTb(RSTb), .Q(O[0]));
    custom_DFF COUNT_SUB_DFF1(.CLK(O[0]), .D(D[1]), .RSTb(RSTb), .Q(O[1]));
    custom_DFF COUNT_SUB_DFF2(.CLK(O[1]), .D(D[2]), .RSTb(RSTb), .Q(O[2]));
    custom_DFF COUNT_SUB_DFF3(.CLK(O[2]), .D(D[3]), .RSTb(RSTb), .Q(O[3]));
    custom_DFF COUNT_SUB_DFF4(.CLK(O[3]), .D(D[4]), .RSTb(RSTb), .Q(O[4]));
    custom_DFF COUNT_SUB_DFF5(.CLK(O[4]), .D(D[5]), .RSTb(RSTb), .Q(O[5]));
    custom_DFF COUNT_SUB_DFF6(.CLK(O[5]), .D(D[6]), .RSTb(RSTb), .Q(O[6]));
    custom_DFF COUNT_SUB_DFF7(.CLK(O[6]), .D(D[7]), .RSTb(RSTb), .Q(O[7]));
    custom_DFF COUNT_SUB_DFF8(.CLK(O[7]), .D(D[8]), .RSTb(RSTb), .Q(O[8]));
    custom_DFF COUNT_SUB_DFF9(.CLK(O[8]), .D(D[9]), .RSTb(RSTb), .Q(O[9]));
    custom_DFF COUNT_SUB_DFF10(.CLK(O[9]), .D(D[10]), .RSTb(RSTb), .Q(O[10]));
    custom_DFF COUNT_SUB_DFF11(.CLK(O[10]), .D(D[11]), .RSTb(RSTb), .Q(O[11]));
    custom_DFF COUNT_SUB_DFF12(.CLK(O[11]), .D(D[12]), .RSTb(RSTb), .Q(O[12]));
    custom_DFF COUNT_SUB_DFF13(.CLK(O[12]), .D(D[13]), .RSTb(RSTb), .Q(O[13]));
    custom_DFF COUNT_SUB_DFF14(.CLK(O[13]), .D(D[14]), .RSTb(RSTb), .Q(O[14]));
    custom_DFF COUNT_SUB_DFF15(.CLK(O[14]), .D(D[15]), .RSTb(RSTb), .Q(O[15]));
    custom_DFF COUNT_SUB_DFF16(.CLK(O[15]), .D(D[16]), .RSTb(RSTb), .Q(O[16]));
    custom_DFF COUNT_SUB_DFF17(.CLK(O[16]), .D(D[17]), .RSTb(RSTb), .Q(O[17]));
    custom_DFF COUNT_SUB_DFF18(.CLK(O[17]), .D(D[18]), .RSTb(RSTb), .Q(O[18]));
    custom_DFF COUNT_SUB_DFF19(.CLK(O[18]), .D(D[19]), .RSTb(RSTb), .Q(O[19]));
endmodule

`endif