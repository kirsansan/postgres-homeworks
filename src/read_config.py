from configparser import ConfigParser


class ConfigReader():

    def __init__(self, path: str):
        self.config_file_name = path
        self.section = None

    def get_data(self, section :str="postgresql") -> dict:
        """:return: all params from section in config file as dictionsry"""

        # create a parser
        parser = ConfigParser()
        # read config file
        parser.read(self.config_file_name)
        tmp_dict = {}
        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                tmp_dict[param[0]] = param[1]
        else:
            raise Exception(
                'Section {0} is not found in the {1} file.'.format(section, self.config_file_name))
        return tmp_dict


if __name__ == '__main__':
    cr = ConfigReader('../config/database.ini')
    params = cr.get_data("postgresql")
    print(params)
