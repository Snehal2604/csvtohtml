#!/usr/bin/python3
from prettytable import from_csv, PrettyTable

def main():
    """ It's script which trasnlate csv to HTML table.
    """
    with open("dataset.csv", "r") as fp:
        x = from_csv(fp) # read from csv by PT
        y = PrettyTable.get_html_string(x) # translate to html, PT
        table_html = y # store in var
        html_file=open('table.html','w') # create and write
        html_file=html_file.write(table_html) # add var html

if __name__ == '__main__':
    main()