class ReaderSQLCommandFile:
    def __init__(self):
        self.result = ""

    #@staticmethod
    def get_from_sql(self, path: str) -> str:
        """
        read *.sql file without comments which mark with '--' at the beginning
        ::return:: multistring with command """
        tmp_line = ''
        try:
            with open(path, encoding='utf-8', newline='\n') as commandfile:
                for line in commandfile:
                    first_part = line.strip().split('--')[0]
                    if first_part != "":
                        tmp_line += " " + first_part + "\n"
        except FileNotFoundError:
            raise FileNotFoundError(f"file {path} does not exist or bad directory")
        self.result = tmp_line
        return tmp_line


if __name__ == '__main__':
    reader = ReaderSQLCommandFile()
    print(reader.get_from_sql('../homework-5/fill_db.sql'))
