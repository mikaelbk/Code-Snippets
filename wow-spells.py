
from numpy import mean

class Heal_spell:
    def __init__(self, name, mana, heal, cast_time):
        self.name = name
        self.mana = mana
        self.heal = heal
        self.cast_time = cast_time # seconds

    def get_efficiency(self):
        efficiency = self.heal/self.mana
        return efficiency

    def get_efficacy(self):
        efficacy = self.heal/self.cast_time
        return efficacy

    def print_stats(self):
        efficiency = self.get_efficiency()
        efficacy = self.get_efficacy()
        print(f"\t\tEfficiency\tEfficacy")
        print( f"{self.name}\t{efficiency:5.1f}\t\t{efficacy:5.1f}" )




healing_touch = Heal_spell("Healing Touch", 110, mean([202,251]), 2.5)
regrowth = Heal_spell("Regrowth", 205, mean([164,188])+175 , 23.0)
regrowth_burst = Heal_spell("Regrowth", 205, mean([164,188]) , 2.0)
rejuvenation = Heal_spell("Rejuvenation", 75, 116, 12)
lifebloom = Heal_spell("Lifebloom", 85/2, 29+59, 7)
lifebloom3 = Heal_spell("Lifebloomx3", (85*3)/2, 350, 21)


healing_touch.print_stats()
regrowth.print_stats()
regrowth_burst.print_stats()
rejuvenation.print_stats()
lifebloom.print_stats()
lifebloom3.print_stats()