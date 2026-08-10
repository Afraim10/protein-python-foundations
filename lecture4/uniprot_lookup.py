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
        extracted_name = process_prot_data(prot_info)
    except requests.exceptions.ConnectionError:
        print("ConnectionError: No internet acess.")
    except protein_info(accession).status_code:
        print("Non-200 status code: bad accession ID.")
    print(f"Protein name: {extracted_name}")


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
