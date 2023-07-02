import csv
import json

class InstantiateCSVError(Exception):
    pass

class FieldsDescriptionError(Exception):
    pass

class Reader:

    @staticmethod
    def print_from_csv(path: str, fields_name : tuple):
        """
        we are going print all-items from csv file with fields fields_name"""
        if fields_name is None:
            raise FieldsDescriptionError("empty fields descriptions are not supported")
        try:
            with open(path, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                try:
                    for row in reader:
                        data_from_file = tuple([row[fields_name[x]] for x in range(0, len(fields_name))])
                        print(data_from_file)
                except KeyError:
                    raise InstantiateCSVError(f"{path} file is corrupted")
        except FileNotFoundError:
            raise FileNotFoundError(f"file {path} does not exist or bad directory")

    @staticmethod
    def get_from_csv(path: str) -> list[tuple]:
        """
        we are going to get all-items from csv file and return as list of tuples
        ::return:: list of tuples in order as wrote in file """
        data_list = []
        try:
            with open(path, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    tmp_row = []
                    [tmp_row.append(item) for item in row.values()]
                    data_list.append(tuple(tmp_row))
        except FileNotFoundError:
            raise FileNotFoundError(f"file {path} does not exist or bad directory")
        return data_list

    @staticmethod
    def get_from_json(path: str) -> list[dict]:
        """
        we are going to get all data  from JSON file
        ::return:: dict with data """
        try:
            with open(path, 'r', encoding='utf-8') as jsonfile:
                data = json.load(jsonfile)
                #data = data.encode('utf-8')
        except FileNotFoundError:
            raise FileNotFoundError(f"file {path} does not exist or bad directory")
        return data

if __name__ == '__main__':
    r = Reader()
    r_data = r.get_from_json('../homework-5/suppliers.json')
    print(r_data)