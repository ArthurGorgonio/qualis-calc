def calc_pub(author_dict):
    pub = 1.00 * author_dict.get('A1') + \
          0.90 * author_dict.get('A2') + \
          0.80 * author_dict.get('A3') + \
          0.70 * author_dict.get('A4') + \
          0.50 * author_dict.get('B1') + \
          0.35 * author_dict.get('B2') + \
          0.20 * author_dict.get('B3') + \
          0.05 * author_dict.get('B4')
    return pub


def create_author_dict():
    publications = {
        'A1': 0,
        'A2': 0,
        'A3': 0,
        'A4': 0,
        'B1': 0,
        'B2': 0,
        'B3': 0,
        'B4': 0,
    }
    return publications
