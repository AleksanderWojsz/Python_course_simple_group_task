import argparse
import json
import random
import pathlib

total_time = 0
FILE_NAME = "Dane"

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
    time_of_day = parse_time_of_day(args.p)
    csv_format = args.c
    json_format = args.j

    if args.t: # Create files
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

def parse_time_of_day(time_of_day):
    list_of_time_short = ['r', 'w']
    list_of_time_long = ['rano', 'wieczorem']
    parsed_list = []

    for i in range(len(list_of_time_short)):
        if list_of_time_short[i] in time_of_day:
            parsed_list.append(list_of_time_long[i])

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

def write_to_csv(path_to_file):
    # TODO
    pass

def read_from_csv(path_to_file):
    # TODO
    pass

# Osoba 2
def create_write_paths(months, days, time_of_day, csv_format, json_format):
    paths = []
    for m in months:
        for d_int in days:
            for d in d_int:
                for p in time_of_day:
                    dir = pathlib.Path(f"{m}/{d}/{p}/")
                    try:
                        dir.mkdir(parents=True, exist_ok=True)
                        if json_format:
                            paths.append(dir / f"{FILE_NAME}.json")
                        if csv_format:
                            paths.append(dir / f"{FILE_NAME}.csv")
                    except:
                        pass
    return paths


# Osoba 2
def create_read_paths(months, days, time_of_day, csv_format, json_format):
    paths = []
    for m in months:
        for d_int in days:
            for d in d_int:
                for p in time_of_day:
                    dir = pathlib.Path(f"{m}/{d}/{p}/")

                    if json_format:
                        path_to_file = dir / f"{FILE_NAME}.json"
                        if path_to_file.is_file():
                            paths.append(path_to_file)
                        else:
                            pass # If the file doesn't exist, ignore the path

                    if csv_format:
                        path_to_file = dir / f"{FILE_NAME}.csv"
                        if path_to_file.is_file():
                            paths.append(path_to_file)
                        else:
                            pass # If the file doesn't exist, ignore the path
    return paths

# Osoba 2
def write_to_files(months, days, time_of_day, csv_format, json_format):
    paths = create_write_paths(months, days, time_of_day, csv_format, json_format)
    for path in paths:
        if json_format:
            write_to_json(path)
        if csv_format:
            write_to_csv(path)

# Osoba 2
def read_from_files(months, days, time_of_day, csv_format, json_format):
    paths = create_read_paths(months, days, time_of_day, csv_format, json_format)
    for path in paths:
        if json_format:
            read_from_json(path)
        if csv_format:
            read_from_csv(path)
    print(f"Czas: {total_time}")


if __name__ == "__main__":
    parse_args()

# Examples of execution:
# python <filename.py> -m styczen luty -d pn-wt pt -p r w -t -c
