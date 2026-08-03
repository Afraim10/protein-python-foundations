# Afraim10 biopractice of CS50P: lecture2
def main():
    start = float(input("Starting concentration (uM): "))
    dil_fact = float(input("Dilution factor: "))
    while dil_fact <= 0:
        print("Invalid dilution factor")
        dil_fact = float(input("Dilution factor: "))
    numb_step = int(input("Number of steps: "))
    calculate(start, dil_fact, numb_step)


def calculate(s, d, n):
    for i in range(n):
        print(f"Step {i+1}: {round((s/d), 2)}")
        s = s/d


main()
