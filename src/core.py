from calc import create_author_dict
from calc import calc_pub
from utils import csv_to_dict


def points(author_data, conference, journal):
    author_pubs = csv_to_dict(author_data)
    author = create_author_dict()
    for k, v in author_pubs.items():
        if k in conference.keys():
            author[conference.get(k)] += int(v)
        elif k in journal.keys():
            author[journal.get(k)] += int(v) * 2
        else:
            print("This {author_data.get(k)} does not exists!",
                  "\nPlease correct the input file")
    result = calc_pub(author)
    return result


def run(author_list, conference, journal):
    author_names = list()
    author_results = list()
    while author_list:
        author_pubs = author_list.pop()
        author_names.append(author_pubs.split('/')[-1].split('.csv')[0])
        author_results.append(points(author_pubs, conference, journal))
    ranked_authors_points = list(zip(author_names, author_results))
    ranked_authors_points.sort(key=lambda x: x[1], reverse=True)
    for i, j in ranked_authors_points:
        print(f'{i:25} total of points {j:9.2f}')
