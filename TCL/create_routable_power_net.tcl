
proc create_routable_power_net {source_net_name} {
    set block [ord::get_db_block]
    set tech [ord::get_db_tech]

    # Get objects from source net
    set net [$block findNet $source_net_name]
    set bterm [$net getBTerms]
    set bpin [$bterm getBPins]

    # Create routable net in the database
    set r_pin "r_$source_net_name"
    set r_net [odb::dbNet_create $block $r_pin]

    # Create block terminal for routable net
    set r_bterm [odb::dbBTerm_create $r_net $r_pin]
    set r_bpin [odb::dbBPin_create $r_bterm]
    $r_bpin setPlacementStatus "FIRM"

    # Set to r_VIN the same physical box as that of VIN (its ring)
    foreach box [$bpin getBoxes] {
        set layer [$box getTechLayer] ;# get metal layer
        odb::dbBox_create $r_bpin $layer [$box xMin] [$box yMin] \
            [$box xMax] [$box yMax] ;# create physical box for net
    }
}
