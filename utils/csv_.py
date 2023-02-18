import csv


class HandleCSV:
    filename = "employees.csv/acbb2271e66c10a5b73aacf82ca82784-e38afe62e088394d61ed30884dd50a6826eee0a8/employees.csv"
    @classmethod
    def read_entire_csv(cls):
        data = []
        with open(cls.filename, "r") as foo:
            reader = csv.DictReader(foo)
            for lines in reader:
                data.append(lines)
        return data

    @classmethod
    def read_csv_line_by_line(cls):
        with open(cls.filename) as bar:
            yield bar.readline()


if __name__ == "__main__":

    task1 = HandleCSV()
    print(task1.read_entire_csv())





