# Afraim10 biopractice of CS50P: lecture1
# Upgraded more complex version of dilution.py
def main():
    c1 = float(input("Stock concenteration (uM): "))
    c2 = float(input("Desired concenteration (uM): "))
    v2 = float(input("Desired final volume (uL): "))
    v1 = volume_needed(c1, c2, v2)
    print(v1)


def volume_needed(c1, c2, v2):
    finalv1 = (c2*v2) / c1
    finalv1 = float(finalv1)
    if c2 > c1:
        return "Error: Desired concentration exceeds stock concentration — dilution not possible."
    elif finalv1 > v2:
        return "Error: Computed volume is greater than desired final volume — physically impossible"
    else:
        return finalv1


main()
