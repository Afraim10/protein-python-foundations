def main():
    c1 = float(input("Stock concenteration (uM): "))
    c2 = float(input("Desired concenteration (uM): "))
    v2 = float(input("Desired final volume (uL): "))
    v1 = volume_needed(c1, c2, v2)
    print(f"Volume of stock needed: {v1:.2f} uL")


def volume_needed(c1, c2, v2):
    finalv1 = (c2*v2) / c1
    finalv1 = float(finalv1)
    return finalv1


main()
