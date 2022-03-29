# 강준서 식물생산과학부 2022-14673
# physics.py
# define methods to solve physical problem

# mass1 : mass of the object 1 (unit: kg)
# mass2 : mass of the object 2 (unit: kg)
# distance : distance between the centers (unit: m)
def force(mass1, mass2, distance):
    return (6.67408*(10**(-11))) * (mass1*mass2) / distance**2

