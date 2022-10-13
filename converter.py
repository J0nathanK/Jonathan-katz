import argparse
import json
import csv

parser = argparse.ArgumentParser(description='This program convert the format of file [Json -> Csv or Csv ->Json]')
parser.add_argument('-F', '--file_path', type=str, metavar=' ', required=True, help='Enter the path of the file ')
parser.add_argument('-C', '--format', type=str, metavar=' ', required=True, help='Enter to which format to convert[json/csv]')
parser.add_argument('--separator', type=str, metavar=' ', help='If you convert json file please enter which separator')
parser.add_argument('--file_name', type=str, metavar=' ', help='Enter name for file ')
args = parser.parse_args()


def csv_json(file_path, file_name, separator):
    with open(file_path, "r") as csv_file:
        reader = csv.reader(csv_file, delimiter=separator)
        columnNames = []
        data = []

        rowNumber = 0
        for row in reader:
            if rowNumber == 0:
                columnNames.extend(row)
            else:
                i = 0
                itemDictionary = {}
                while i < len(row):
                    itemDictionary[columnNames[i]] = row[i]
                    i += 1
                data.append(itemDictionary)
            rowNumber += 1

        with open('{}.json'.format(file_name), "w") as f:
            json.dump(data, f, indent=4)


def json_csv(file_path, file_name):
    headers = []
    with open(file_path, "r") as json_file:
        data = json.load(json_file)
        headers.extend(data[0].keys())

    with open('{}.csv'.format(file_name), "w") as f:
        writer = csv.DictWriter(f, headers)
        writer.writeheader()
        for i in data:
            writer.writerow(i)


if __name__ == '__main__':

    if args.file_name is None:
        full_name = args.file_path
        file_name = full_name.split(".")[0]
    else:
        file_name = args.file_name

    if args.format == "json":
        if args.separator is None:
            args.separator = ','
            csv_json(args.file_path, file_name, args.separator)
        else:
            csv_json(args.file_path, file_name, args.separator)
    elif args.format == "csv":
        json_csv(args.file_path, file_name)
    else:
        print("Invalid Format")