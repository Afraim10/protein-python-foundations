def main():
    raw_id = input("Enter a PDB ID: ")
    formatted = format_pdb_id(raw_id)
    print("Formatted:", formatted)
    length = len(formatted)
    print("Length:", length)
    isalphanum = formatted.isalnum()
    print("Alphanumeric:", isalphanum)


def format_pdb_id(raw_id):
    return raw_id.replace(" ", "").upper()


main()
