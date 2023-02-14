import csv
import statistics as st

# statistics module do python
# https://www.w3schools.com/python/module_statistics.asp


def analyze_log(path_to_file):
    if not path_to_file.endswith(".csv"):
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")
    try:
        with open(path_to_file) as text:
            file = list(csv.reader(text))

            maria_most_consumed = st.mode(
                [item[1] for item in file if item[0] == "maria"]
            )

            arnaldo_hamburguers = len(
                [
                    item[1]
                    for item in file
                    if item[0] == "arnaldo" and item[1] == "hamburguer"
                ]
            )

            items = set([item[1] for item in file])

            joao_not_consumed = items.difference(
                set([item[1] for item in file if item[0] == "joao"])
            )

            days = set([item[2] for item in file])

            joao_not_days = days.difference(
                set([item[2] for item in file if item[0] == "arnaldo"])
            )

            with open("data/mkt_campaign.txt", "w") as result:
                result.write(f"{maria_most_consumed}\n")
                result.write(f"{arnaldo_hamburguers}\n")
                result.write(f"{joao_not_consumed}\n")
                result.write(f"{joao_not_days}")
            return result
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")
