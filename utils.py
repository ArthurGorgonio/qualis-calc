import csv


def csv_to_dict(filename) -> dict:
    with open(filename) as f:
        d = dict(filter(None, csv.reader(f)))
    f.close()
    return d


