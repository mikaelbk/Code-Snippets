# This is a short script to calculate the mana gained from Moonkin forms Elune's Touch, for various weapons
# Elune's touch is assumed to have a ppm (proc per minute) of 15
# The mana gained from an Elune's Touch proc is 30% of Melee Attack Power (this was tested and confirmed)

# The assumed AP contributions are as follows:
#   Moonkin Form: 150% of lvl (here 70)
#   Druid staff AP contributions (when in form)
#   Strength gained from the weapon
#   Strength gained from improved Mark of the Wild
#   Base Strength

def elunes_touch(weapon_str,weapon_ap,name):
    # Conditions
    ppm = 15 # Elune's touch procs per minute
    boom_ap = 1.5*70 # Boomkin AP at lvl 70
    base_str = 81 # Base strength at lvl 70
    iMotW_str = 18 # Strength gained from improved MotW

    # Calculations
    strength = base_str + iMotW_str + weapon_str # Calculate Strength total
    str_ap = 2*strength-20 # Convert Strength to AP
    ap = boom_ap + str_ap + weapon_ap # Attack Power total
    
    print("\n"+name)
    print("\tAP:\t",ap)
    print("\tM/proc:\t",ap*0.3)
    print("\tMP5:\t",ppm*ap*0.3*5/60)

elunes_touch(38,829,"Terestians Stranglestaff") # tested 31.08.21
elunes_touch(0,0,"Warpstaff of Arcanum (or any staff without str/ap)") # tested 31.08.21
elunes_touch(28,197,"Ursol's Claw")
elunes_touch(31,375,"Staff of Beasts")
elunes_touch(19,46,"Agamaggan's Quill")

# Output:
"""
Terestians Stranglestaff
        AP:      1188.0
        M/proc:  356.4 
        MP5:     445.5 

Warpstaff of Arcanum (or any staff without str/ap)
        AP:      283.0
        M/proc:  84.89999999999999
        MP5:     106.125

Ursol's Claw
        AP:      536.0
        M/proc:  160.79999999999998
        MP5:     201.0

Staff of Beasts
        AP:      720.0
        M/proc:  216.0
        MP5:     270.0

Agamaggan's Quill
        AP:      367.0
        M/proc:  110.1
        MP5:     137.625
"""
