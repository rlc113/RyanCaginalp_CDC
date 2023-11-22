echo "---------------------------------------------------------------"
echo "Synthesis:"

yosys -c Synthesis.tcl

echo
echo "---------------------------------------------------------------"
echo "Floorplanning:"

openroad Floorplanning.tcl

echo
echo "---------------------------------------------------------------"
echo "Placement:"

openroad Placement.tcl

echo
echo "---------------------------------------------------------------"
echo "Filler Cell Insertion:"

openroad FillerInsertion.tcl

echo
echo "---------------------------------------------------------------"
echo "Routing:"

openroad Routing.tcl

echo
echo "---------------------------------------------------------------"
echo "Output Generation:"

./Finishing.sh

echo
echo $"---------------------------------------------------------------"
echo $"DRC:"

./DRC.sh

echo
echo $"---------------------------------------------------------------"
echo $"LVS:"

./LVS.sh
