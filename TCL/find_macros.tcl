proc find_macros {} {
  set macros ""

  set db [::ord::get_db]
  set block [[$db getChip] getBlock]
  foreach inst [$block getInsts] {
    set inst_master [$inst getMaster]

    # BLOCK means MACRO cells
    if { [string match [$inst_master getType] "BLOCK"] } {
      set terminals [$inst_master getMTerms]
      foreach term $terminals {
      	puts [$term getName]
      }
      append macros " " $inst
    }
  }
  return $macros
}
