import argparse
import json
import random

total_time = 0

# Osoba 1
def parse_args():
    parser = argparse.ArgumentParser(description="Skrypt do tworzenia i czytania plikow", epilog="Przykladowe uzycie: python <filename.py> -m styczen luty -d pn-wt pt -p r w -t -c")

    parser.add_argument("-m", nargs="+", required=True, help="Miesiace") # nargs="+" means a list of args
    parser.add_argument("-d", nargs="+", required=True, help="Dni")
    parser.add_argument("-p", nargs="+", default=["r"], help="Pora dnia") # r - rano
    parser.add_argument("-t", action="store_true", help="Tworz pliki") # action is used when a flag takes no parameters. Otherwise, default should be used
    parser.add_argument("-o", action="store_true", help="Czytaj pliki")
    parser.add_argument("-c", action="store_true", help="Format CSV")
    parser.add_argument("-j", action="store_true", help="Format JSON")

    args = parser.parse_args()
    months = args.m
    days = parse_days(args.d)
    time_of_day = args.p
    csv_format = args.c
    json_format = args.j

    if args.t: # Create files
        create_paths(months, days, time_of_day, csv_format, json_format)
        write_to_files(months, days, time_of_day, csv_format, json_format)
    if args.o: # Read files
        read_from_files(months, days, time_of_day, csv_format, json_format)

# Osoba 1
def parse_days(days):
    list_of_days_short = ['pn', 'wt', 'sr', 'czw', 'pt', 'sb', 'nd']
    list_of_days_full = ['poniedzialek', 'wtorek', 'sroda', 'czwartek', 'piatek', 'sobota', 'niedziela']
    parsed_list = []

    for interval in days:
        if '-' in interval:
            start_day, end_day = interval.split('-')
            start_index = list_of_days_short.index(start_day)
            end_index = list_of_days_short.index(end_day)
            if start_index <= end_index:
                parsed_list.append(list_of_days_full[start_index:end_index + 1])
            else:
                parsed_list.append(list_of_days_full[start_index:] + list_of_days_full[0:end_index + 1])
        else:
            parsed_list.append([list_of_days_full[list_of_days_short.index(interval)]])

    return parsed_list


# Osoba 4
def write_to_json(path_to_file):
    data = {
        "Model": random.choice(["A", "B", "C"]),
        "Wynik": random.randint(0, 1000),
        "Czas": str(random.randint(0, 1000)) + "s",
    }

    try:
        with open(path_to_file, "w") as file:
            json.dump(data, file)
    except:  # In case of an error, ignore this file
        pass

# Osoba 4
def read_from_json(path_to_file):
    try:
        with open(path_to_file, "r") as file:
            data = json.load(file)
            if data["Model"] == "A":
                global total_time
                time = data["Czas"]
                total_time += int(time[:len(time) - 1])
    except:  # In case of an error, ignore this file
        pass


def create_paths(months, days, time_of_day, csv_format, json_format):
    # TODO
    pass


def write_to_files(months, days, time_of_day, csv_format, json_format):
    # TODO. Use write_to_json
    pass


def read_from_files(months, days, time_of_day, csv_format, json_format):
    # TODO. Use read_from_json
    pass


if __name__ == "__main__":
    parse_args()

# Examples of execution:
# python <filename.py> -m styczen luty -d pn-wt pt -p r w -t -c
