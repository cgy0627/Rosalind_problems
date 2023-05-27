aa_mass = {}
with open("aa_mass.txt", "r") as file:
    lines = file.readlines()

    for line in lines:
        aa, mass = line.strip().split()
        aa_mass[aa] = float(mass)
    
def calc_mass(s):
    total = 0
    for aa in s:
        total += aa_mass[aa]
    
    print(total)

calc_mass("SKADYEK")

