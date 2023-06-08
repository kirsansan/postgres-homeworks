import csv

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
