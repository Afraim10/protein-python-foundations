# Afraim10 biopractice of CS50P: lecture4
import sys
import requests
import json


def main():
    try:
        accession = input("UniProt accession: ").replace(" ", "").upper()
        while accession.isnumeric() or accession.isalpha():
            print("Invalid accession code.")
            accession = input("UniProt accession: ").replace(" ", "").upper()

        prot_info = protein_info(accession)
        if prot_info.status_code != 200:
            print("Error: invalid accession ID.")
            raise ValueError
        extracted_name = process_prot_data(prot_info)
        print(f"Protein name: {extracted_name}")

    except requests.exceptions.ConnectionError:
        print("ConnectionError: No internet access.")
    except ValueError:
        pass


def protein_info(accession):
    info = requests.get(f"https://rest.uniprot.org/uniprotkb/{accession}.json")
    return info


def process_prot_data(info):
    dictionariated = info.json()
    raw = dictionariated['proteinDescription']
    recom_name = raw['recommendedName']
    fullname = recom_name['fullName']
    name_value = fullname['value']
    return name_value


main()
