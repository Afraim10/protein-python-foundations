# Afraim10 biopractice: pandas
import pandas as pd
import requests
import json


def main(accession):
    try:
        req_response = protein_info(accession)
        if req_response.status_code != 200:
            print("Error: invalid accession ID.")
            raise ValueError
    except requests.exceptions.ConnectionError:
        print("ConnectionError: No internet access.")
    req_response.raise_for_status()
    with open(f"{accession}.json", "w") as file:
        json.dump(req_response.json(), file)

    with open(f"{accession}.json") as file:
        protein_data = json.load(file)
    prot_data_parsing(protein_data)


def protein_info(accession):
    accession = accession.strip().upper()
    info = requests.get(f"https://rest.uniprot.org/uniprotkb/{accession}.json")
    return info


def prot_data_parsing(prot_data):
    features = prot_data["features"]
    ft_df = pd.json_normalize(features)
    ft_df = ft_df[["type", "description",
                   "location.start.value", "location.end.value"]]
    ft_df = ft_df.sort_values("location.start.value")
    print(ft_df)


if __name__ == "__main__":
    main("P11387")
