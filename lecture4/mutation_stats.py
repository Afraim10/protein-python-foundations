# Afraim10 biopractice of CS50P: lecture4
import sys
import random
import statistics


def main():
    bases = ['A', 'C', 'T', 'G']
    while True:
        try:
            sequence = input("Enter DNA sequence: ").replace(" ", "").upper()
            mutations_number = input(
                "Number of mutations to simulate: ").replace(" ", "")
            while mutations_number.isalpha() and (int(mutations_number)/float(mutations_number)) != 0 and mutations_number <= 0:
                print("Invalid: Only positive digits allowed.")
                mutations_number = input(
                    "Number of mutations to simulate: ").replace(" ", "")
            else:
                mutations_number = int(mutations_number)

            while sequence.isnumeric():
                print("Invalid: Only DNA bases are allowed.")
                sequence = input("Enter DNA sequence: ").replace(
                    " ", "").upper()

            for i in range(len(sequence)):
                if sequence[i] not in bases:
                    print("Invalid: Only DNA bases are allowed.")
                    sys.exit()

            mutation(sequence, mutations_number)
            break
        except ValueError:
            pass


def mutation(seq, numb):
    bases = ['A', 'C', 'T', 'G']
    firsthalf = 0
    secondhalf = 0
    positions_mutations = []
    for i in range(numb):
        position = random.randint(0, ((len(seq))-1))
        newbase = random.choice(bases)
        if position >= 0 and position <= ((len(seq))//2):
            firsthalf += 1
            positions_mutations.append(position)
        elif position >= (((len(seq))//2)+1) and position <= ((len(seq))-1):
            secondhalf += 1
            positions_mutations.append(position)
    print(f"First half: {firsthalf}, Second half: {secondhalf}")
    print(f"Mean position: {round(statistics.mean(positions_mutations),2)}")
    print(
        f"Standard deviation: {round(statistics.stdev(positions_mutations),2)}")


main()
