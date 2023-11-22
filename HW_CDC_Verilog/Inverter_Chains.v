`include "Physical_Gates.v"

`ifndef INVCHAIN_GUARD
`define INVCHAIN_GUARD

module Normal_Inverter_Chain(input I, output O);

    wire low_chain0;
    wire low_chain1;
    wire low_chain2;
    wire low_chain3;
    wire low_chain4;
    wire low_chain5;
    wire low_chain6;
    wire low_chain7;
    wire low_chain8;
    wire low_chain9;
    wire low_chain10;
    wire low_chain11;
    wire low_chain12;
    wire low_chain13;
    wire low_chain14;
    wire low_chain15;

    custom_chainInverter low_chain_inv1_1(.I(I), .O(low_chain1));
    custom_chainInverter low_chain_inv2_1(.I(low_chain1), .O(low_chain2));
    custom_chainInverter low_chain_inv3_1(.I(low_chain2), .O(low_chain3));
    custom_chainInverter low_chain_inv4_1(.I(low_chain3), .O(low_chain4));
    custom_chainInverter low_chain_inv5_1(.I(low_chain4), .O(low_chain5));
    custom_chainInverter low_chain_inv6_1(.I(low_chain5), .O(low_chain6));
    custom_chainInverter low_chain_inv7_1(.I(low_chain6), .O(low_chain7));
    custom_chainInverter low_chain_inv8_1(.I(low_chain7), .O(low_chain8));
    custom_chainInverter low_chain_inv9_1(.I(low_chain8), .O(low_chain9));
    custom_chainInverter low_chain_inv10_1(.I(low_chain9), .O(low_chain10));
    custom_chainInverter low_chain_inv11_1(.I(low_chain10), .O(low_chain11));
    custom_chainInverter low_chain_inv12_1(.I(low_chain11), .O(low_chain12));
    custom_chainInverter low_chain_inv13_1(.I(low_chain12), .O(low_chain13));
    custom_chainInverter low_chain_inv14_1(.I(low_chain13), .O(low_chain14));
    custom_chainInverter low_chain_inv15_1(.I(low_chain14), .O(low_chain15));
    custom_chainInverter low_chain_inv16_1(.I(low_chain15), .O(O));

endmodule


module Cap_Inverter_Chain(input I, output O);

    wire cap_chain0;
    wire cap_chain1;
    wire cap_chain2;
    wire cap_chain3;
    wire cap_chain4;
    wire cap_chain5;
    wire cap_chain6;
    wire cap_chain7;
    wire cap_chain8;
    wire cap_chain9;
    wire cap_chain10;
    wire cap_chain11;
    wire cap_chain12;
    wire cap_chain13;
    wire cap_chain14;
    wire cap_chain15;

    custom_chainInverter cap_chain_inv1_1(.I(I), .O(cap_chain1));
    custom_chainInverter cap_chain_inv2_1(.I(cap_chain1), .O(cap_chain2));
    custom_chainInverter cap_chain_inv3_1(.I(cap_chain2), .O(cap_chain3));
    custom_chainInverter cap_chain_inv4_1(.I(cap_chain3), .O(cap_chain4));
    custom_chainInverter cap_chain_inv5_1(.I(cap_chain4), .O(cap_chain5));
    custom_chainInverter cap_chain_inv6_1(.I(cap_chain5), .O(cap_chain6));
    custom_chainInverter cap_chain_inv7_1(.I(cap_chain6), .O(cap_chain7));
    custom_chainInverter cap_chain_inv8_1(.I(cap_chain7), .O(cap_chain8));
    custom_chainInverter cap_chain_inv9_1(.I(cap_chain8), .O(cap_chain9));
    custom_chainInverter cap_chain_inv10_1(.I(cap_chain9), .O(cap_chain10));
    custom_chainInverter cap_chain_inv11_1(.I(cap_chain10), .O(cap_chain11));
    custom_chainInverter cap_chain_inv12_1(.I(cap_chain11), .O(cap_chain12));
    custom_chainInverter cap_chain_inv13_1(.I(cap_chain12), .O(cap_chain13));
    custom_chainInverter cap_chain_inv14_1(.I(cap_chain13), .O(cap_chain14));
    custom_chainInverter cap_chain_inv15_1(.I(cap_chain14), .O(cap_chain15));
    custom_chainInverter cap_chain_inv16_1(.I(cap_chain15), .O(O));

endmodule


module Finish_Inverter_Chain(input I, output Ob, output O);

    wire finish_chain0;
    wire finish_chain1;
    wire finish_chain2;
    wire finish_chain3;
    wire finish_chain4;
    wire finish_chain5;
    wire finish_chain6;
    wire finish_chain7;
    wire finish_chain8;
    wire finish_chain9;
    wire finish_chain10;
    wire finish_chain11;
    wire finish_chain12;
    wire finish_chain13;
    wire finish_chain14;
    wire finish_chain15;

    custom_chainInverter finish_chain_inv1_1(.I(I), .O(finish_chain1));
    custom_chainInverter finish_chain_inv2_1(.I(finish_chain1), .O(finish_chain2));
    custom_chainInverter finish_chain_inv3_1(.I(finish_chain2), .O(finish_chain3));
    custom_chainInverter finish_chain_inv4_1(.I(finish_chain3), .O(finish_chain4));
    custom_chainInverter finish_chain_inv5_1(.I(finish_chain4), .O(finish_chain5));
    custom_chainInverter finish_chain_inv6_1(.I(finish_chain5), .O(finish_chain6));
    custom_chainInverter finish_chain_inv7_1(.I(finish_chain6), .O(finish_chain7));
    custom_chainInverter finish_chain_inv8_1(.I(finish_chain7), .O(finish_chain8));
    custom_chainInverter finish_chain_inv9_1(.I(finish_chain8), .O(finish_chain9));
    custom_chainInverter finish_chain_inv10_1(.I(finish_chain9), .O(finish_chain10));
    custom_chainInverter finish_chain_inv11_1(.I(finish_chain10), .O(finish_chain11));
    custom_chainInverter finish_chain_inv12_1(.I(finish_chain11), .O(finish_chain12));
    custom_chainInverter finish_chain_inv13_1(.I(finish_chain12), .O(finish_chain13));
    custom_chainInverter finish_chain_inv14_1(.I(finish_chain13), .O(finish_chain14));
    custom_chainInverter finish_chain_inv15_1(.I(finish_chain14), .O(Ob));
    custom_chainInverter finish_chain_inv16_1(.I(Ob), .O(O));

endmodule

`endif