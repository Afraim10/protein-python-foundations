# Afraim10 biopractice of CS50P: lecture3
def main():
    while True:
        try:
            start = float(
                input("Starting concentration (uM): ").replace(" ", ""))
            dil_fact = input("Dilution factor: ").replace(" ", "")
            if dil_fact.isalpha():
                print("Invalid: not a number.")
                raise ValueError
            elif float(dil_fact) <= 0:
                print("Invalid: dilution factor must be greater than 0.")
                raise ValueError
            numb_step = int(input("Number of steps: "))
            if numb_step < 1:
                print("Invalid number of steps.")
                raise ValueError
            calculate(start, dil_fact, numb_step)
            break
        except ValueError:
            pass


def calculate(s, d, n):
    d = float(d)
    for i in range(n):
        print(f"Step {i+1}: {round((s/d), 2)}")
        s = s/d


main()
