# Afraim10 biopractice of CS50P: lecture1
# Complex upgraded pdb_formatter
def main():
    raw_id = input("Enter a PDB ID: ")
    formatted = format_pdb_id(raw_id)
    print(formatted)
    match formatted:
        case "Invlaid: PDB IDs are always 4 charachters" | "Invalid: PDB IDs must contain digits and alphabetics" | "Invalid: PDB IDs must start with a digit.":
            return
    length = len(formatted)
    print("Length:", length)
    isalphanum = formatted.isalnum()
    print("Alphanumeric:", isalphanum)


def format_pdb_id(raw_id):
    n = "1", "2", "3", "4", "5", "6", "7", "8", "9"
    formatted = raw_id.replace(" ", "").upper()
    if len(formatted) != 4:
        return "Invlaid: PDB IDs are always 4 charachters"
    elif formatted.isdigit() == True or formatted.isalpha() == True:
        return "Invalid: PDB IDs must contain digits and alphabetics"
    elif formatted.startswith(n) == False:
        return "Invalid: PDB IDs must start with a digit."
    else:
        return formatted


main()

# After revising this throughly, main() shouldn'tcompare listera text or error messages to control flow
# Correct to use functions to validate and another function what to say about it
