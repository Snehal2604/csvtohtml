# !usr/bin/python3
# import modules
import csv, operator
from prettytable import from_csv

def main():
    """Read dataset from csv imported from web of hubstuff and generate a HTML Table."""


    #x = PrettyTable(["Work", "Member", "Time"])

    # with open('dataset_hubstuff.csv') as csvarchivo:
    #     entrada = csv.reader(csvarchivo)
    with open("dataset_hubstuff.csv", "r") as fp:
        x = from_csv(fp)
    print(x)
    # table_html = x.get_html_string()
    # html_file=open('table.html','w')
    # html_file=html_file.write(table_html)

if __name__ == '__main__':
    main()