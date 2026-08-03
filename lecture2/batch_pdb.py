# Afraim10 biopractice of CS50P: lecture2
def main():
    raw_id = input("Enter a PDB ID: ")
    format_pdb_id(raw_id)


# updated the check list system
def format_pdb_id(raw_id):
    formatted = raw_id.upper().replace(" ", "")
    lenerror = "Invalid PDB IDs are always 4 characters"
    digit_alpha_error = "Invalid PDB IDs must contain digits and alphabetics"
    firstdigit = "Invalid PDB IDs must start with a digit."
    for n in formatted.split(","):
        if n.isalpha() == True or n.isdigit() == True:
            print(f"{n}: {digit_alpha_error}")
        elif len(n) != 4:
            print(f"{n}: {lenerror}")
        elif n[0].isdigit() == False:
            print(f"{n}: {firstdigit}")
        else:
            print(f"{n}: valid, alphanumeric: {n.isalnum()}")


main()
