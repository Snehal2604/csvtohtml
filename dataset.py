#!/usr/bin/python3
from prettytable import from_csv, PrettyTable

def main():
    """ It's script which trasnlate csv to HTML table.

    """
    with open("dataset.csv", "r") as fp:
        x = from_csv(fp)
        y = PrettyTable.get_html_string(x)
        table_html = y
        html_file=open('table.html','w')
        html_file=html_file.write(table_html)

if __name__ == '__main__':
    main()