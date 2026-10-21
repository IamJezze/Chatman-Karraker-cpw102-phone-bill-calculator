"""
def main():
    gb_used = float(input("How much data was used (in GB)? : "))
    base_cost = float(input("What is the base cost of the plan? : "))

    total_cost = base_cost
    if gb_used < 10:
        print("GB used is below the maximum limit of 10 GB. No extra charges incurred.")
    elif gb_used == 10:
        print("At max limit. Extra charges will be incurred per GB used.")
    else:
        total_cost = base_cost + (gb_used - 10) * 2
        print(f"You are {gb_used - 10} over the limit of 10 GB.")
        print(f"Extra charges: ${(gb_used - 10) * 2:.2f}")
    print(f"Total cost: ${total_cost:.2f}")

main()
"""
"""
def main():
    gb_used = float(input("How much data was used (in GB)? : "))
    base_cost = float(input("What is the base cost of the plan? : "))

    total_cost = base_cost
    if gb_used < 9:
        print("GB used is below the maximum limit of 10 GB. No extra charges incurred.")
        if gb_used == 10:
            print("At max limit. Extra charges will be incurred per GB used.")
        elif gb_used in range(11, 15):
            print("You are within the moderate overage range. Extra charges are incurred per GB used.")
            
    else:
        total_cost = base_cost + (gb_used - 10) * 2
        print(f"You are {gb_used - 10} over the limit of 10 GB.")
        print(f"Extra charges: ${(gb_used - 10) * 2:.2f}")
    print(f"Total cost: ${total_cost:.2f}")

main()
"""



def main():
    gb_used = float(input("How much data was used (in GB)? : "))
    base_cost = float(input("What is the base cost of the plan? : "))

    total_cost = base_cost

    if gb_used <= 10:
        if gb_used < 10:
            print("Usage status: WITHIN LIMIT.")
            print("No extra charges incurred.")
        else:
            print("Usage status: AT LIMIT.")
            print("You have reached the 10 GB limit.")

    else:
        if gb_used <= 15:
            print("Usage status: MODERATE OVERAGE.")
        else:
            print("Usage status: HIGH OVERAGE.")

        extra_charges = (gb_used - 10) * 2
        total_cost = base_cost + extra_charges

        print(f"You are {gb_used - 10:.2f} GB over the limit.")
        print(f"Extra charges: ${extra_charges:.2f}")

    print(f"Total cost: ${total_cost:.2f}")


main()

