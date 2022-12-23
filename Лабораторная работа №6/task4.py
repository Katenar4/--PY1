import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter=',', new_line='\n') -> list[dict]:
    with open(filename) as f:
        list_dict = []
        for index, line in enumerate(f):
            fields = line.strip(new_line).split(delimiter)
            if index == 0:
                heads = fields
                continue

            list_dict.append({})

            for i, _ in enumerate(heads):
                list_dict[-1][heads[i]] = fields[i]
    return list_dict


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))

