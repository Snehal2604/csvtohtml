#! /usr/bin/env python

if __name__ == "__main__":
    """Alternative solution"""
    html_string = "<html><body><table>"
    first_line = True
    with open('dataset.csv') as f:
        for line in f:
            html_string += '<tr>'
            if first_line:
                cell_begin = '<th>'
                cell_end = '</th>'

            else:
                cell_begin = '<td>'
                cell_end = '</td>'

            for elem in line.split(','):
                html_string += '{0}{1}{2}'.format(cell_begin, elem.replace('"', ''), cell_end)

            first_line = False
            html_string += '</tr>'

        html_string += '</table></body></html>'

    with open('table.html', 'w') as f:
        f.write(html_string)