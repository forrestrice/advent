def recurse_fuel(mass):
    fuel_mass = (mass // 3) - 2
    if fuel_mass <= 0:
        return 0
    else:
        return fuel_mass + recurse_fuel(fuel_mass)


with open("mass_input.txt", "r") as masses:
    sum = 0
    for mass in masses:
        sum += (int(mass) // 3) - 2
    print(sum)  # answer 1
    masses.seek(0)
    part2_sum = 0
    for mass in masses:
        part2_sum += recurse_fuel(int(mass))
    print(part2_sum)
